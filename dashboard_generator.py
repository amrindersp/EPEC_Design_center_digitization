"""
=============================================================================
ONGC - Engineering and Projects Excellence Centre (EPEC)
Project Dashboard Generator
=============================================================================

HOW TO USE THIS SCRIPT:
1. Run this script using Python: python dashboard_generator.py
2. It will generate all HTML files in a folder called "dashboard_output"
3. Open "dashboard_output/index.html" in your browser to view the Dashboard

HOW TO ADD/REMOVE PROJECTS:
- Open the file "projects_data.py" in the same folder
- Follow the instructions there to add, remove, or edit projects

HOW TO LINK PROJECT FOLDERS:
- In "projects_data.py", find the project you want to link
- Replace the path "" with the actual folder path on your computer
  Example (Windows): "C:/Users/YourName/Projects/OffshoreWorks/2015/ProjectName"
  Example (Mac/Linux): "/home/username/Projects/OffshoreWorks/2015/ProjectName"

HOW TO ADD A BACKGROUND IMAGE:
- Place your image file in the same folder as this script
- In the SETTINGS section below, change:
  BACKGROUND_IMAGE = ""  →  BACKGROUND_IMAGE = "your_image_filename.jpg"

=============================================================================
"""

import os
import json
import webbrowser

# ─────────────────────────────────────────────────────────────────────────────
# SETTINGS — Change these values to customize the Dashboard
# ─────────────────────────────────────────────────────────────────────────────

COMPANY_NAME       = "ONGC"
DEPARTMENT_NAME    = "Engineering and Projects Excellence Centre"
DEPARTMENT_SHORT   = "EPEC"
OUTPUT_FOLDER      = "dashboard_output"

# To add a background image: replace "" with your image filename
# Example: BACKGROUND_IMAGE = "background.jpg"
BACKGROUND_IMAGE   = ""

ABOUT_TEXT = (
    "This Dashboard has been made to enable structured access, systematic compilation, "
    "effective data management, and long-term preservation of legacy engineering and project "
    "information pertaining to all Onshore and Offshore projects executed over the past few years."
)

# Years range for projects
YEAR_START = 2010
YEAR_END   = 2026

# ─────────────────────────────────────────────────────────────────────────────
# IMPORT PROJECT DATA
# ─────────────────────────────────────────────────────────────────────────────

from projects_data import DIVISIONS


# ─────────────────────────────────────────────────────────────────────────────
# HTML TEMPLATES
# ─────────────────────────────────────────────────────────────────────────────

def get_common_styles(bg_image=""):
    """
    Returns the CSS styles used across all pages.
    The background image is set here — if no image is provided, a dark gradient is used.
    """
    if bg_image:
        bg_css = f"""
        background-image: url('../{bg_image}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        """
    else:
        # Default professional dark gradient (used when no image is set)
        bg_css = """
        background: linear-gradient(135deg, #0a1628 0%, #0d2137 40%, #0a2e1f 100%);
        """

    return f"""
        /* ── Reset & Base ── */
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
            min-height: 100vh;
            {bg_css}
            color: #e8e8e8;
        }}

        /* Dark overlay on top of background for readability */
        body::before {{
            content: '';
            position: fixed;
            inset: 0;
            background: rgba(5, 15, 30, 0.72);
            z-index: 0;
        }}

        /* All content sits above the overlay */
        .page-wrapper {{
            position: relative;
            z-index: 1;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}

        /* ── Header ── */
        .header {{
            background: linear-gradient(90deg, rgba(0,60,120,0.95) 0%, rgba(0,100,60,0.90) 100%);
            border-bottom: 3px solid #f0a500;
            padding: 18px 40px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }}

        .header-left {{
            display: flex;
            align-items: center;
            gap: 18px;
        }}

        .ongc-logo-img {{
            width: 64px;
            height: 64px;
            object-fit: contain;
            flex-shrink: 0;
        }}

        .header-title h1 {{
            font-size: 22px;
            font-weight: 800;
            letter-spacing: 3px;
            color: #f0a500;
            text-transform: uppercase;
        }}

        .header-title h2 {{
            font-size: 13px;
            font-weight: 400;
            color: #b0c8e0;
            letter-spacing: 1.5px;
            margin-top: 3px;
        }}

        .header-badge {{
            background: rgba(240,165,0,0.15);
            border: 1px solid rgba(240,165,0,0.4);
            border-radius: 20px;
            padding: 6px 18px;
            font-size: 12px;
            color: #f0a500;
            letter-spacing: 2px;
            font-weight: 600;
        }}

        /* ── Nav Breadcrumb ── */
        .breadcrumb {{
            background: rgba(0,0,0,0.3);
            padding: 10px 40px;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            font-size: 13px;
            color: #7a9ab8;
        }}

        .breadcrumb a {{
            color: #7a9ab8;
            text-decoration: none;
            transition: color 0.2s;
        }}

        .breadcrumb a:hover {{ color: #f0a500; }}
        .breadcrumb span {{ color: #b0c8e0; margin: 0 8px; }}

        /* ── Main Content ── */
        .main-content {{
            flex: 1;
            padding: 50px 40px;
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
        }}

        .section-title {{
            text-align: center;
            margin-bottom: 50px;
        }}

        .section-title h3 {{
            font-size: 28px;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}

        .section-title .underline {{
            width: 80px;
            height: 3px;
            background: linear-gradient(90deg, #f0a500, #00a86b);
            margin: 12px auto 0;
            border-radius: 2px;
        }}

        .section-title p {{
            color: #7a9ab8;
            font-size: 14px;
            margin-top: 10px;
            letter-spacing: 1px;
        }}

        /* ── Cards Grid ── */
        .cards-grid {{
            display: flex;
            flex-wrap: wrap;
            gap: 28px;
            justify-content: center;
        }}

        /* ── Division Card (Home page) ── */
        .division-card {{
            background: linear-gradient(145deg, rgba(0,40,80,0.85), rgba(0,25,50,0.90));
            border: 1px solid rgba(240,165,0,0.25);
            border-radius: 16px;
            padding: 40px 30px;
            width: 300px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            color: inherit;
            display: block;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }}

        .division-card:hover {{
            transform: translateY(-8px);
            border-color: #f0a500;
            box-shadow: 0 16px 48px rgba(240,165,0,0.2);
            background: linear-gradient(145deg, rgba(0,60,120,0.90), rgba(0,40,80,0.95));
        }}

        .division-card .icon {{
            font-size: 52px;
            margin-bottom: 18px;
            display: block;
        }}

        .division-card h4 {{
            font-size: 18px;
            font-weight: 700;
            color: #f0a500;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}

        .division-card p {{
            font-size: 13px;
            color: #7a9ab8;
            line-height: 1.6;
        }}

        .division-card .project-count {{
            margin-top: 16px;
            background: rgba(240,165,0,0.1);
            border: 1px solid rgba(240,165,0,0.3);
            border-radius: 20px;
            padding: 5px 14px;
            font-size: 12px;
            color: #f0a500;
            display: inline-block;
        }}

        /* ── Year Card ── */
        .year-card {{
            background: linear-gradient(145deg, rgba(0,40,80,0.80), rgba(0,25,50,0.85));
            border: 1px solid rgba(100,160,220,0.25);
            border-radius: 12px;
            padding: 22px 28px;
            width: 140px;
            text-align: center;
            cursor: pointer;
            transition: all 0.25s ease;
            text-decoration: none;
            color: inherit;
            display: block;
            box-shadow: 0 4px 16px rgba(0,0,0,0.3);
        }}

        .year-card:hover {{
            transform: translateY(-5px);
            border-color: #f0a500;
            box-shadow: 0 10px 30px rgba(240,165,0,0.2);
        }}

        .year-card .year-number {{
            font-size: 26px;
            font-weight: 800;
            color: #f0a500;
            letter-spacing: 1px;
        }}

        .year-card .project-count {{
            font-size: 12px;
            color: #7a9ab8;
            margin-top: 6px;
        }}

        .year-card.no-projects {{
            opacity: 0.45;
            cursor: default;
            pointer-events: none;
        }}

        /* ── Project Card ── */
        .project-card {{
            background: linear-gradient(145deg, rgba(0,50,30,0.75), rgba(0,30,60,0.80));
            border: 1px solid rgba(0,168,107,0.25);
            border-radius: 14px;
            padding: 28px 24px;
            width: 260px;
            text-align: center;
            transition: all 0.3s ease;
            text-decoration: none;
            color: inherit;
            display: block;
            box-shadow: 0 6px 24px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
        }}

        .project-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 3px;
            background: linear-gradient(90deg, #00a86b, #f0a500);
        }}

        .project-card:hover {{
            transform: translateY(-6px);
            border-color: #00a86b;
            box-shadow: 0 14px 40px rgba(0,168,107,0.2);
            cursor: pointer;
        }}

        .project-card .icon {{
            font-size: 38px;
            margin-bottom: 14px;
            display: block;
        }}

        .project-card h5 {{
            font-size: 15px;
            font-weight: 700;
            color: #e8e8e8;
            line-height: 1.4;
            margin-bottom: 8px;
        }}

        .project-card .year-tag {{
            font-size: 12px;
            color: #00a86b;
            font-weight: 600;
        }}

        .project-card.no-link {{
            opacity: 0.7;
        }}

        .project-card.no-link:hover {{
            cursor: not-allowed;
        }}

        .link-status {{
            margin-top: 10px;
            font-size: 11px;
            padding: 3px 10px;
            border-radius: 10px;
            display: inline-block;
        }}

        .link-status.linked {{
            background: rgba(0,168,107,0.15);
            color: #00a86b;
            border: 1px solid rgba(0,168,107,0.3);
        }}

        .link-status.not-linked {{
            background: rgba(255,100,0,0.1);
            color: #ff8040;
            border: 1px solid rgba(255,100,0,0.2);
        }}

        /* ── Bottom Nav Buttons ── */
        .nav-buttons {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            background: rgba(0,0,0,0.3);
            border-top: 1px solid rgba(255,255,255,0.08);
            margin-top: auto;
        }}

        .btn {{
            padding: 10px 28px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            border: none;
            letter-spacing: 1px;
            transition: all 0.2s;
            text-decoration: none;
            display: inline-block;
        }}

        .btn-back {{
            background: rgba(255,255,255,0.08);
            color: #b0c8e0;
            border: 1px solid rgba(255,255,255,0.15);
        }}

        .btn-back:hover {{
            background: rgba(255,255,255,0.15);
            color: white;
        }}

        .btn-home {{
            background: linear-gradient(90deg, #003c78, #005a40);
            color: white;
            border: 1px solid rgba(240,165,0,0.3);
        }}

        .btn-home:hover {{
            background: linear-gradient(90deg, #004e9a, #007a55);
            box-shadow: 0 4px 15px rgba(240,165,0,0.2);
        }}

        /* ── Modal (About) ── */
        .modal-overlay {{
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.75);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }}

        .modal-overlay.active {{ display: flex; }}

        .modal-box {{
            background: linear-gradient(145deg, #0a1e3a, #0a2e1f);
            border: 1px solid rgba(240,165,0,0.4);
            border-radius: 16px;
            padding: 40px;
            max-width: 600px;
            width: 90%;
            position: relative;
            box-shadow: 0 24px 80px rgba(0,0,0,0.6);
        }}

        .modal-box h3 {{
            font-size: 20px;
            color: #f0a500;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px solid rgba(240,165,0,0.2);
        }}

        .modal-box p {{
            font-size: 15px;
            color: #b0c8e0;
            line-height: 1.8;
        }}

        .modal-close {{
            position: absolute;
            top: 15px; right: 20px;
            background: none;
            border: none;
            color: #7a9ab8;
            font-size: 24px;
            cursor: pointer;
            transition: color 0.2s;
        }}

        .modal-close:hover {{ color: #f0a500; }}

        /* ── Footer ── */
        .footer {{
            text-align: center;
            padding: 14px;
            font-size: 11px;
            color: rgba(255,255,255,0.25);
            border-top: 1px solid rgba(255,255,255,0.05);
            letter-spacing: 1px;
        }}

        /* ── Empty State ── */
        .empty-state {{
            text-align: center;
            padding: 60px 20px;
            color: #7a9ab8;
        }}

        .empty-state .icon {{ font-size: 48px; display: block; margin-bottom: 16px; }}
        .empty-state p {{ font-size: 15px; }}
    """


def build_header_html(show_about=True):
    """
    Returns the HTML for the top header bar.
    'show_about' controls whether the About button is shown.
    """
    about_btn = ""
    if show_about:
        about_btn = """
            <button class="btn btn-home" onclick="document.getElementById('aboutModal').classList.add('active')"
                    style="background: linear-gradient(90deg, #a07000, #006040); font-size:13px;">
                ℹ️ About
            </button>
        """

    return f"""
        <div class="header">
            <div class="header-left">
                <img src="ongc_logo.png" class="ongc-logo-img">
                <div class="header-title">
                    <h1>{COMPANY_NAME}</h1>
                    <h2>{DEPARTMENT_NAME} &mdash; {DEPARTMENT_SHORT}</h2>
                </div>
            </div>
            <div style="display:flex; gap:12px; align-items:center;">
                {about_btn}
                <div class="header-badge">{DEPARTMENT_SHORT}</div>
            </div>
        </div>
    """


def build_about_modal_html():
    """Returns the HTML for the About popup modal."""
    return f"""
        <div class="modal-overlay" id="aboutModal">
            <div class="modal-box">
                <button class="modal-close" onclick="document.getElementById('aboutModal').classList.remove('active')">✕</button>
                <h3>About This Dashboard</h3>
                <p>{ABOUT_TEXT}</p>
            </div>
        </div>
    """


def build_footer_html():
    """Returns the HTML footer."""
    return f"""
        <div class="footer">
            {COMPANY_NAME} &bull; {DEPARTMENT_NAME} ({DEPARTMENT_SHORT}) &bull; Project Information Dashboard
        </div>
    """


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 1: HOME PAGE (index.html)
# Shows: About button + Projects button → Divisions
# ─────────────────────────────────────────────────────────────────────────────

def generate_home_page():
    """
    Generates the main home page (index.html).
    Shows two sections: "About" button and Division cards under "Projects".
    """

    # Count total projects per division (for the badge on each card)
    def count_projects(division_key):
        total = 0
        for year_data in DIVISIONS[division_key]["projects"].values():
            total += len(year_data)
        return total

    # ── Division Cards ──
    # Each division gets a card. Add/remove divisions here in the same block pattern.
    division_cards_html = ""

    # ── Loop through each division defined in projects_data.py ──
    for div_key, div_info in DIVISIONS.items():
        count   = count_projects(div_key)
        icon    = div_info.get("icon", "🏗️")
        name    = div_info["name"]
        desc    = div_info.get("description", "")
        page    = f"division_{div_key}.html"

        division_cards_html += f"""
            <a href="{page}" class="division-card">
                <span class="icon">{icon}</span>
                <h4>{name}</h4>
                <p>{desc}</p>
                <span class="project-count">{count} Projects</span>
            </a>
        """

    # ── Full Page HTML ──
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ONGC EPEC — Project Dashboard</title>
    <style>
        {get_common_styles(BACKGROUND_IMAGE)}

        /* Home-page specific: big welcome title */
        .welcome-banner {{
            text-align: center;
            padding: 50px 20px 30px;
        }}
        .ongc-logo-img {{
            width: 64px;
            height: 64px;
            object-fit: contain;
            flex-shrink: 0;
        }}
        .welcome-banner h2 {{
            font-size: 38px;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: 4px;
            text-transform: uppercase;
        }}

        .welcome-banner h2 span {{
            color: #f0a500;
        }}

        .welcome-banner p {{
            margin-top: 12px;
            font-size: 15px;
            color: #7a9ab8;
            letter-spacing: 1.5px;
        }}

        .section-separator {{
            width: 100%;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(240,165,0,0.3), transparent);
            margin: 40px 0;
        }}

        /* "PROJECTS" section heading */
        .projects-section-label {{
            text-align: center;
            font-size: 13px;
            letter-spacing: 4px;
            color: #7a9ab8;
            text-transform: uppercase;
            margin-bottom: 30px;
        }}
    </style>
</head>
<body>
    <div class="page-wrapper">

        {build_header_html(show_about=True)}
        {build_about_modal_html()}

        <div class="main-content">

            <!-- Welcome Banner -->
            <div class="welcome-banner">
                <h2>Project <span>Dashboard</span></h2>
                <p>Select a Division to browse projects by year</p>
            </div>

            <div class="section-separator"></div>

            <!-- Division Cards -->
            <div class="projects-section-label">📁 Select Division</div>

            <div class="cards-grid">
                {division_cards_html}
            </div>

        </div>

        {build_footer_html()}
    </div>

    <script>
        // Close modal when clicking outside the box
        document.getElementById('aboutModal').addEventListener('click', function(e) {{
            if (e.target === this) this.classList.remove('active');
        }});
    </script>
</body>
</html>"""

    return html


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 2: DIVISION PAGE (division_<key>.html)
# Shows: Years from 2010–2026 for a selected division
# ─────────────────────────────────────────────────────────────────────────────

def generate_division_page(div_key):
    """
    Generates the Year-selection page for one division.
    Years that have projects are clickable; others are dimmed.
    """
    div_info = DIVISIONS[div_key]
    div_name = div_info["name"]
    projects  = div_info["projects"]

    year_cards_html = ""

    # ── One card per year from YEAR_START to YEAR_END ──
    for year in range(YEAR_START, YEAR_END + 1):
        year_str = str(year)
        count    = len(projects.get(year_str, []))

        if count > 0:
            # Year has projects → clickable link
            page = f"projects_{div_key}_{year_str}.html"
            year_cards_html += f"""
                <a href="{page}" class="year-card">
                    <div class="year-number">{year}</div>
                    <div class="project-count">{count} project{"s" if count != 1 else ""}</div>
                </a>
            """
        else:
            # No projects → greyed out, not clickable
            year_cards_html += f"""
                <div class="year-card no-projects">
                    <div class="year-number">{year}</div>
                    <div class="project-count">No projects</div>
                </div>
            """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ONGC EPEC — {div_name}</title>
    <style>
        {get_common_styles(BACKGROUND_IMAGE)}
    </style>
</head>
<body>
    <div class="page-wrapper">

        {build_header_html(show_about=False)}

        <!-- Breadcrumb navigation -->
        <div class="breadcrumb">
            <a href="index.html">🏠 Home</a>
            <span>›</span>
            {div_name}
        </div>

        <div class="main-content">
            <div class="section-title">
                <h3>{div_name}</h3>
                <div class="underline"></div>
                <p>Select a year to view projects completed in that year</p>
            </div>

            <div class="cards-grid">
                {year_cards_html}
            </div>
        </div>

        <!-- Bottom navigation buttons -->
        <div class="nav-buttons">
            <a href="index.html" class="btn btn-back">← Back to Home</a>
            <a href="index.html" class="btn btn-home">🏠 Home</a>
        </div>

        {build_footer_html()}
    </div>
</body>
</html>"""

    return html


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 3: PROJECTS PAGE (projects_<div_key>_<year>.html)
# Shows: All project icons for a selected division + year
# ─────────────────────────────────────────────────────────────────────────────

def generate_projects_page(div_key, year):
    """
    Generates the page showing all projects for a given division and year.
    Each project card either opens its folder (if path is set) or shows 'Not Linked'.
    """
    div_info  = DIVISIONS[div_key]
    div_name  = div_info["name"]
    year_str  = str(year)
    projects  = div_info["projects"].get(year_str, [])

    project_cards_html = ""

    if not projects:
        # No projects for this year
        project_cards_html = """
            <div class="empty-state">
                <span class="icon">📭</span>
                <p>No projects found for this year.</p>
            </div>
        """
    else:
        # ── One card per project ──
        for project in projects:
            project_name = project["name"]
            folder_path  = project.get("path", "")  # "" means not yet linked

            if folder_path:
                # Folder is linked → clicking opens the folder
                # We use a JS function to open the folder via a local file:// link
                safe_path = folder_path.replace("\\", "/")
                card_html = f"""
                    <div class="project-card" onclick="openFolder('{safe_path}')" title="Click to open project folder">
                        <span class="icon">📁</span>
                        <h5>{project_name}</h5>
                        <div class="year-tag">📅 {year_str}</div>
                        <span class="link-status linked">✔ Folder Linked</span>
                    </div>
                """
            else:
                # Folder not yet linked → show "Not Linked" badge
                card_html = f"""
                    <div class="project-card no-link" title="Folder not yet linked — see projects_data.py">
                        <span class="icon">📂</span>
                        <h5>{project_name}</h5>
                        <div class="year-tag">📅 {year_str}</div>
                        <span class="link-status not-linked">⚠ Not Linked</span>
                    </div>
                """

            project_cards_html += card_html

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ONGC EPEC — {div_name} | {year_str}</title>
    <style>
        {get_common_styles(BACKGROUND_IMAGE)}
    </style>
</head>
<body>
    <div class="page-wrapper">

        {build_header_html(show_about=False)}

        <!-- Breadcrumb navigation -->
        <div class="breadcrumb">
            <a href="index.html">🏠 Home</a>
            <span>›</span>
            <a href="division_{div_key}.html">{div_name}</a>
            <span>›</span>
            {year_str}
        </div>

        <div class="main-content">
            <div class="section-title">
                <h3>{div_name} — {year_str}</h3>
                <div class="underline"></div>
                <p>{len(projects)} project{"s" if len(projects) != 1 else ""} completed in {year_str}</p>
            </div>

            <div class="cards-grid">
                {project_cards_html}
            </div>
        </div>

        <!-- Bottom navigation buttons -->
        <div class="nav-buttons">
            <a href="division_{div_key}.html" class="btn btn-back">← Back to Years</a>
            <a href="index.html" class="btn btn-home">🏠 Home</a>
        </div>

        {build_footer_html()}
    </div>

    <script>
        /**
         * openFolder: Opens a local folder in Windows Explorer (or Mac Finder).
         *
         * HOW IT WORKS:
         * - It creates a temporary <a> tag pointing to the file:// path
         * - On Windows this opens the folder in Explorer
         * - Note: Some browsers block local file links for security.
         *   If it does not work, try opening the dashboard in Firefox,
         *   or use the path shown in the browser's address bar.
         */
        function openFolder(folderPath) {{
            var link = document.createElement('a');
            link.href = 'file:///' + folderPath;
            link.target = '_blank';
            link.click();
        }}
    </script>
</body>
</html>"""

    return html


# ─────────────────────────────────────────────────────────────────────────────
# MAIN: Generate all HTML files
# ─────────────────────────────────────────────────────────────────────────────

def generate_all_files():
    """
    Master function — generates every HTML file needed for the Dashboard.
    Run this to rebuild the dashboard after making any changes.
    """

    # Create output folder if it doesn't exist
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    files_created = []

    # ── 1. Home Page ──
    path = os.path.join(OUTPUT_FOLDER, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(generate_home_page())
    files_created.append("index.html")

    # ── 2. Division Pages (one per division) ──
    for div_key in DIVISIONS:
        filename = f"division_{div_key}.html"
        path = os.path.join(OUTPUT_FOLDER, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(generate_division_page(div_key))
        files_created.append(filename)

    # ── 3. Project Pages (one per division × year that has projects) ──
    for div_key, div_info in DIVISIONS.items():
        for year_str, projects in div_info["projects"].items():
            if projects:  # Only create page if there are projects
                filename = f"projects_{div_key}_{year_str}.html"
                path = os.path.join(OUTPUT_FOLDER, filename)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(generate_projects_page(div_key, int(year_str)))
                files_created.append(filename)

    # ── Summary ──
    print("=" * 60)
    print("  ONGC EPEC Dashboard — Generation Complete!")
    print("=" * 60)
    print(f"\n  Output folder : {os.path.abspath(OUTPUT_FOLDER)}")
    print(f"  Files created : {len(files_created)}")
    print(f"\n  Files generated:")
    for f in files_created:
        print(f"    ✔  {f}")

    print("\n" + "=" * 60)
    print("  HOW TO VIEW THE DASHBOARD:")
    print(f"  Open this file in your browser:")
    print(f"  {os.path.abspath(os.path.join(OUTPUT_FOLDER, 'index.html'))}")
    print("=" * 60 + "\n")

    return os.path.abspath(os.path.join(OUTPUT_FOLDER, "index.html"))


# ─────────────────────────────────────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    index_path = generate_all_files()

    # Automatically open the dashboard in the default browser
    print("  Opening Dashboard in your browser...")
    webbrowser.open(f"file:///{index_path.replace(os.sep, '/')}")
