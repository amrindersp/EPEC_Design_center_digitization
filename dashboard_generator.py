"""
=============================================================================
ONGC - Engineering and Projects Excellence Centre (EPEC)
Project Dashboard Generator  ——  v2.0  (with Login & User Session)
=============================================================================

HOW TO USE THIS SCRIPT:
1. Run this script: python dashboard_generator.py
2. It generates all HTML files inside "dashboard_output/" folder
3. Open "dashboard_output/login.html" in your browser  ← START HERE
4. Login with a User ID and Password from users.py
5. You will be taken to the main Dashboard

HOW TO MANAGE USERS (ADD / REMOVE / CHANGE PASSWORDS):
   Open "users.py" — all user credentials are stored there.
   After making changes, run this script again to rebuild.

HOW TO ADD / REMOVE PROJECTS:
   Open "projects_data.py" — all project data is stored there.
   After making changes, run this script again to rebuild.

HOW TO LINK PROJECT FOLDERS:
   In "projects_data.py", replace the empty path "" with the actual
   folder path on your computer.
   Windows example : "C:/Projects/OffshoreWorks/2015/ProjectName"
   Always use forward slashes "/" even on Windows.

HOW TO ADD A BACKGROUND IMAGE:
   Place your image file in the same folder as this script.
   Then change the line below:
       BACKGROUND_IMAGE = ""
   To:
       BACKGROUND_IMAGE = "your_image.jpg"
   Then run this script again.

=============================================================================
"""

import os
import webbrowser


# =============================================================================
# SETTINGS
# Change these values to customize the Dashboard.
# =============================================================================

COMPANY_NAME     = "ONGC"
DEPARTMENT_NAME  = "Engineering and Projects Excellence Centre"
DEPARTMENT_SHORT = "EPEC"
OUTPUT_FOLDER    = "dashboard_output"

# To add a background image, replace "" with your image filename.
# Example: BACKGROUND_IMAGE = "background.jpg"
BACKGROUND_IMAGE = ""

ABOUT_TEXT = (
    "This Dashboard has been made to enable structured access, systematic compilation, "
    "effective data management, and long-term preservation of legacy engineering and project "
    "information pertaining to all Onshore and Offshore projects executed over the past few years."
)

# Year range for projects
YEAR_START = 2010
YEAR_END   = 2026


# =============================================================================
# IMPORTS
# =============================================================================

from projects_data   import DIVISIONS
from login_generator import generate_login_page


# =============================================================================
# FUNCTION: get_session_guard_js()
# -----------------------------------------------------------------------------
# Returns a JavaScript block that is inserted at the top of EVERY dashboard
# page (Home, Division, Projects).
#
# HOW IT WORKS:
#   - When a user logs in via login.html, a flag is saved in sessionStorage.
#   - Every dashboard page checks for this flag as soon as it loads.
#   - If the flag is missing (not logged in, or tab was closed and reopened),
#     the page immediately redirects to login.html.
#   - sessionStorage is automatically cleared when the browser tab is closed,
#     so the user must log in again in a new tab.
#   - The logoutUser() function is also defined here so it is available on
#     every page (called by the Logout button in the header).
# =============================================================================

def get_session_guard_js():
    return """
    <script>
        // ── Session Guard ──
        // Runs immediately when the page loads (before anything is shown).
        // If the user is not logged in, they are sent back to login.html.
        (function() {
            if (!sessionStorage.getItem('ongc_logged_in')) {
                window.location.replace('login.html');
            }
        })();

        // ── Logout Function ──
        // Called when the user clicks the Logout button in the header.
        // Clears all session data and redirects to login.html.
        function logoutUser() {
            if (confirm('Are you sure you want to logout?')) {
                sessionStorage.clear();
                window.location.replace('login.html');
            }
        }
    </script>
    """


# =============================================================================
# FUNCTION: get_common_styles()
# -----------------------------------------------------------------------------
# Returns all CSS styles used across every dashboard page.
# If a background image filename is provided, it is set as the page background.
# Otherwise a dark professional gradient is used as the default background.
# =============================================================================

def get_common_styles(bg_image=""):

    # Background CSS: image if provided, otherwise gradient
    if bg_image:
        bg_css = f"""
        background-image: url('../{bg_image}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        """
    else:
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

        .ongc-logo-img {{
            width: 64px;
            height: 64px;
            object-fit: contain;
            flex-shrink: 0;
        }}
        
        /* Semi-transparent dark overlay on top of background for readability */
        body::before {{
            content: '';
            position: fixed;
            inset: 0;
            background: rgba(5, 15, 30, 0.72);
            z-index: 0;
        }}

        /* All page content sits above the overlay */
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
            padding: 14px 30px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }}

        .header-left {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}

        /* Circular ONGC logo badge in the header */
        .ongc-logo {{
            width: 58px;
            height: 58px;
            background: linear-gradient(135deg, #f0a500, #e06000);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 19px;
            font-weight: 900;
            color: white;
            letter-spacing: -1px;
            box-shadow: 0 0 18px rgba(240,165,0,0.5);
            flex-shrink: 0;
        }}

        .header-title h1 {{
            font-size: 20px;
            font-weight: 800;
            letter-spacing: 3px;
            color: #f0a500;
            text-transform: uppercase;
        }}

        .header-title h2 {{
            font-size: 12px;
            font-weight: 400;
            color: #b0c8e0;
            letter-spacing: 1.5px;
            margin-top: 2px;
        }}

        /* ── Header Right Section ── */
        /* Contains: User Info Pill + About button + Logout button + EPEC badge */
        .header-right {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        /* Pill that shows logged-in user's name and role */
        .user-info-pill {{
            background: rgba(255,255,255,0.07);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 20px;
            padding: 6px 16px;
            font-size: 12px;
            color: #b0c8e0;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .user-info-pill .user-name {{
            color: #f0a500;
            font-weight: 600;
        }}

        .user-info-pill .user-role {{
            color: #7a9ab8;
            font-size: 11px;
        }}

        /* EPEC badge on the right end of header */
        .header-badge {{
            background: rgba(240,165,0,0.15);
            border: 1px solid rgba(240,165,0,0.4);
            border-radius: 20px;
            padding: 6px 16px;
            font-size: 12px;
            color: #f0a500;
            letter-spacing: 2px;
            font-weight: 600;
        }}

        /* Logout button in the header */
        .btn-logout {{
            background: rgba(180,40,40,0.20);
            border: 1px solid rgba(220,80,80,0.35);
            border-radius: 8px;
            padding: 7px 16px;
            color: #ff9090;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            letter-spacing: 1px;
        }}

        .btn-logout:hover {{
            background: rgba(220,50,50,0.35);
            color: white;
        }}

        /* ── Breadcrumb Navigation Bar ── */
        /* Shown on Division and Projects pages to show current location */
        .breadcrumb {{
            background: rgba(0,0,0,0.3);
            padding: 9px 30px;
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

        /* Arrow separator between breadcrumb items */
        .breadcrumb span {{
            color: #b0c8e0;
            margin: 0 8px;
        }}

        /* ── Main Content Area ── */
        .main-content {{
            flex: 1;
            padding: 44px 30px;
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
        }}

        /* Section title used on Division and Projects pages */
        .section-title {{
            text-align: center;
            margin-bottom: 44px;
        }}

        .section-title h3 {{
            font-size: 26px;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}

        /* Coloured underline beneath section titles */
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

        /* ── Cards Grid Layout ── */
        /* Used on all three page types to arrange cards */
        .cards-grid {{
            display: flex;
            flex-wrap: wrap;
            gap: 26px;
            justify-content: center;
        }}

        /* ── Division Card (Home Page) ── */
        .division-card {{
            background: linear-gradient(145deg, rgba(0,40,80,0.85), rgba(0,25,50,0.90));
            border: 1px solid rgba(240,165,0,0.25);
            border-radius: 16px;
            padding: 36px 28px;
            width: 290px;
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
            font-size: 50px;
            margin-bottom: 16px;
            display: block;
        }}

        .division-card h4 {{
            font-size: 17px;
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

        /* Project count badge on Division cards */
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

        /* ── Year Card (Division Page) ── */
        .year-card {{
            background: linear-gradient(145deg, rgba(0,40,80,0.80), rgba(0,25,50,0.85));
            border: 1px solid rgba(100,160,220,0.25);
            border-radius: 12px;
            padding: 20px 26px;
            width: 135px;
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
            font-size: 24px;
            font-weight: 800;
            color: #f0a500;
        }}

        .year-card .project-count {{
            font-size: 12px;
            color: #7a9ab8;
            margin-top: 6px;
        }}

        /* Years with no projects are greyed out and non-clickable */
        .year-card.no-projects {{
            opacity: 0.40;
            cursor: default;
            pointer-events: none;
        }}

        /* ── Project Card (Projects Page) ── */
        .project-card {{
            background: linear-gradient(145deg, rgba(0,50,30,0.75), rgba(0,30,60,0.80));
            border: 1px solid rgba(0,168,107,0.25);
            border-radius: 14px;
            padding: 26px 22px;
            width: 255px;
            text-align: center;
            transition: all 0.3s ease;
            text-decoration: none;
            color: inherit;
            display: block;
            box-shadow: 0 6px 24px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
        }}

        /* Coloured top stripe on each project card */
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
            font-size: 36px;
            margin-bottom: 12px;
            display: block;
        }}

        .project-card h5 {{
            font-size: 14px;
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

        /* Project cards without a linked folder are slightly faded */
        .project-card.no-link {{ opacity: 0.7; }}
        .project-card.no-link:hover {{ cursor: not-allowed; }}

        /* Linked / Not Linked status badge on project cards */
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

        /* ── Bottom Navigation Button Bar ── */
        /* Shown at the bottom of Division and Projects pages */
        .nav-buttons {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 18px 30px;
            background: rgba(0,0,0,0.3);
            border-top: 1px solid rgba(255,255,255,0.08);
            margin-top: auto;
        }}

        .btn {{
            padding: 10px 26px;
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

        /* Back button (left side) */
        .btn-back {{
            background: rgba(255,255,255,0.08);
            color: #b0c8e0;
            border: 1px solid rgba(255,255,255,0.15);
        }}

        .btn-back:hover {{ background: rgba(255,255,255,0.15); color: white; }}

        /* Home button (right side) */
        .btn-home {{
            background: linear-gradient(90deg, #003c78, #005a40);
            color: white;
            border: 1px solid rgba(240,165,0,0.3);
        }}

        .btn-home:hover {{
            background: linear-gradient(90deg, #004e9a, #007a55);
            box-shadow: 0 4px 15px rgba(240,165,0,0.2);
        }}

        /* ── About Modal Popup ── */
        .modal-overlay {{
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.75);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }}

        /* Modal is shown by adding the 'active' class */
        .modal-overlay.active {{ display: flex; }}

        .modal-box {{
            background: linear-gradient(145deg, #0a1e3a, #0a2e1f);
            border: 1px solid rgba(240,165,0,0.4);
            border-radius: 16px;
            padding: 38px;
            max-width: 580px;
            width: 90%;
            position: relative;
            box-shadow: 0 24px 80px rgba(0,0,0,0.6);
        }}

        .modal-box h3 {{
            font-size: 19px;
            color: #f0a500;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 18px;
            padding-bottom: 14px;
            border-bottom: 1px solid rgba(240,165,0,0.2);
        }}

        .modal-box p {{ font-size: 14px; color: #b0c8e0; line-height: 1.8; }}

        /* Close (X) button in the top-right corner of the modal */
        .modal-close {{
            position: absolute;
            top: 14px; right: 18px;
            background: none;
            border: none;
            color: #7a9ab8;
            font-size: 22px;
            cursor: pointer;
            transition: color 0.2s;
        }}

        .modal-close:hover {{ color: #f0a500; }}

        /* ── Page Footer ── */
        .footer {{
            text-align: center;
            padding: 12px;
            font-size: 11px;
            color: rgba(255,255,255,0.20);
            border-top: 1px solid rgba(255,255,255,0.05);
            letter-spacing: 1px;
        }}

        /* ── Empty State Message ── */
        /* Shown when a year has no projects */
        .empty-state {{ text-align: center; padding: 60px 20px; color: #7a9ab8; }}
        .empty-state .icon {{ font-size: 48px; display: block; margin-bottom: 16px; }}
        .empty-state p {{ font-size: 15px; }}

        /* ── Home Page: Welcome Banner ── */
        .welcome-banner {{ text-align: center; padding: 44px 20px 26px; }}

        .welcome-banner h2 {{
            font-size: 34px;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: 4px;
            text-transform: uppercase;
        }}

        /* "Dashboard" word in the title is highlighted in orange */
        .welcome-banner h2 span {{ color: #f0a500; }}

        /* Personalised welcome message shown below the main title */
        .welcome-user {{
            font-size: 15px;
            color: #b0c8e0;
            margin-top: 10px;
        }}

        .welcome-user strong {{ color: #f0a500; }}

        /* Horizontal divider line on the home page */
        .section-separator {{
            width: 100%;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(240,165,0,0.3), transparent);
            margin: 36px 0;
        }}

        /* "SELECT DIVISION" label above the division cards */
        .projects-section-label {{
            text-align: center;
            font-size: 13px;
            letter-spacing: 4px;
            color: #7a9ab8;
            text-transform: uppercase;
            margin-bottom: 28px;
        }}
    """


# =============================================================================
# FUNCTION: build_header_html()
# -----------------------------------------------------------------------------
# Returns the HTML for the top header bar shown on every dashboard page.
#
# The header contains:
#   LEFT  : ONGC logo circle + Company name + Department name
#   RIGHT : User info pill (name + role from session) +
#           About button (optional) +
#           Logout button +
#           EPEC badge
#
# The user info pill is populated by a small inline JavaScript block that
# reads the user's name and role from sessionStorage (saved at login).
#
# Parameters:
#   show_about : True  = show the About button (used on Home page only)
#                False = hide the About button (used on other pages)
# =============================================================================

def build_header_html(show_about=True):

    # About button — only shown on the Home page
    about_btn = ""
    if show_about:
        about_btn = """
            <button class="btn btn-home"
                    onclick="document.getElementById('aboutModal').classList.add('active')"
                    style="background: linear-gradient(90deg, #a07000, #006040);
                           font-size:12px; padding: 7px 16px;">
                ℹ️ About
            </button>
        """

    return f"""
        <div class="header">

            <!-- Left side: Logo + Title -->
            <div class="header-left">
                <img src="ongc_logo.png" class="ongc-logo-img">
                <div class="header-title">
                    <h1>{COMPANY_NAME}</h1>
                    <h2>{DEPARTMENT_NAME} &mdash; {DEPARTMENT_SHORT}</h2>
                </div>
            </div>

            <!-- Right side: User pill + About + Logout + Badge -->
            <div class="header-right">

                <!-- User Info Pill: hidden by default, shown by JS if user is logged in -->
                <div class="user-info-pill" id="userInfoPill" style="display:none;">
                    👤
                    <span class="user-name" id="headerUserName"></span>
                    &nbsp;|&nbsp;
                    <span class="user-role" id="headerUserRole"></span>
                </div>

                {about_btn}

                <!-- Logout Button: calls logoutUser() defined in the session guard -->
                <button class="btn-logout" onclick="logoutUser()">⏻ Logout</button>

                <div class="header-badge">{DEPARTMENT_SHORT}</div>

            </div>
        </div>

        <!-- Populate user info pill from sessionStorage -->
        <script>
            (function() {{
                var name = sessionStorage.getItem('ongc_user_name');
                var role = sessionStorage.getItem('ongc_user_role');
                if (name) {{
                    document.getElementById('headerUserName').textContent = name;
                    document.getElementById('headerUserRole').textContent = role || '';
                    document.getElementById('userInfoPill').style.display = 'flex';
                }}
            }})();
        </script>
    """


# =============================================================================
# FUNCTION: build_about_modal_html()
# -----------------------------------------------------------------------------
# Returns the HTML for the About popup modal.
# The modal is hidden by default and shown when the About button is clicked.
# It is closed by clicking the X button or clicking outside the box.
# =============================================================================

def build_about_modal_html():
    return f"""
        <div class="modal-overlay" id="aboutModal">
            <div class="modal-box">
                <button class="modal-close"
                        onclick="document.getElementById('aboutModal').classList.remove('active')">
                    ✕
                </button>
                <h3>About This Dashboard</h3>
                <p>{ABOUT_TEXT}</p>
            </div>
        </div>
    """


# =============================================================================
# FUNCTION: build_footer_html()
# Returns the HTML for the page footer shown at the bottom of every page.
# =============================================================================

def build_footer_html():
    return f"""
        <div class="footer">
            {COMPANY_NAME} &bull; {DEPARTMENT_NAME} ({DEPARTMENT_SHORT}) &bull; Project Information Dashboard
        </div>
    """


# =============================================================================
# PAGE GENERATOR 1: generate_home_page()
# -----------------------------------------------------------------------------
# Generates "index.html" — the main dashboard page shown after login.
#
# This page shows:
#   - Personalised welcome message (user's name from session)
#   - One Division Card for each division defined in projects_data.py
#   - About modal popup
#
# TO ADD A NEW DIVISION: Add it in projects_data.py — it will automatically
# appear here as a new card without any changes to this function.
# =============================================================================

def generate_home_page():

    # Count total projects across all years for each division
    # This number is shown as a badge on each division card
    def count_projects(division_key):
        total = 0
        for year_data in DIVISIONS[division_key]["projects"].values():
            total += len(year_data)
        return total

    # Build one division card per division
    division_cards_html = ""
    for div_key, div_info in DIVISIONS.items():
        count = count_projects(div_key)
        icon  = div_info.get("icon", "🏗️")
        name  = div_info["name"]
        desc  = div_info.get("description", "")
        page  = f"division_{div_key}.html"

        # Each card is a clickable link to that division's year-selection page
        division_cards_html += f"""
            <a href="{page}" class="division-card">
                <span class="icon">{icon}</span>
                <h4>{name}</h4>
                <p>{desc}</p>
                <span class="project-count">{count} Projects</span>
            </a>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ONGC EPEC — Dashboard</title>
    <style>{get_common_styles(BACKGROUND_IMAGE)}</style>
</head>
<body>

    <!-- SESSION GUARD: Redirects to login.html if user is not logged in -->
    {get_session_guard_js()}

    <div class="page-wrapper">

        {build_header_html(show_about=True)}
        {build_about_modal_html()}

        <div class="main-content">

            <!-- Welcome Banner -->
            <div class="welcome-banner">
                <h2>Project <span>Dashboard</span></h2>
                <!-- This paragraph is updated by JS below with the logged-in user's name -->
                <p class="welcome-user" id="welcomeMsg">
                    Select a Division to browse projects by year
                </p>
            </div>

            <div class="section-separator"></div>

            <div class="projects-section-label">📁 Select Division</div>

            <!-- Division Cards Grid -->
            <div class="cards-grid">
                {division_cards_html}
            </div>

        </div>

        {build_footer_html()}

    </div>

    <script>
        // ── Personalised Welcome Message ──
        // Reads the logged-in user's name and division from sessionStorage
        // and updates the welcome message on the page.
        var userName = sessionStorage.getItem('ongc_user_name');
        var userDiv  = sessionStorage.getItem('ongc_user_div');
        if (userName) {{
            document.getElementById('welcomeMsg').innerHTML =
                'Welcome, <strong>' + userName + '</strong>' +
                (userDiv ? ' &mdash; ' + userDiv : '') +
                ' &nbsp;|&nbsp; Select a Division to browse projects';
        }}

        // Close the About modal when clicking outside the modal box
        document.getElementById('aboutModal').addEventListener('click', function(e) {{
            if (e.target === this) this.classList.remove('active');
        }});
    </script>

</body>
</html>"""

    return html


# =============================================================================
# PAGE GENERATOR 2: generate_division_page()
# -----------------------------------------------------------------------------
# Generates "division_<div_key>.html" — the year-selection page for a division.
#
# This page shows one Year Card for each year from YEAR_START to YEAR_END.
#   - Years WITH projects  → coloured card, clickable link to projects page
#   - Years WITHOUT projects → greyed-out card, not clickable
#
# Parameters:
#   div_key : the division key string (e.g. "offshore_works")
# =============================================================================

def generate_division_page(div_key):

    div_info = DIVISIONS[div_key]
    div_name = div_info["name"]
    projects = div_info["projects"]

    # Build one year card per year in the range
    year_cards_html = ""
    for year in range(YEAR_START, YEAR_END + 1):
        year_str = str(year)
        count    = len(projects.get(year_str, []))

        if count > 0:
            # Year has projects → make it a clickable link
            page = f"projects_{div_key}_{year_str}.html"
            year_cards_html += f"""
                <a href="{page}" class="year-card">
                    <div class="year-number">{year}</div>
                    <div class="project-count">{count} project{"s" if count != 1 else ""}</div>
                </a>
            """
        else:
            # Year has no projects → greyed out, not a link
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
    <style>{get_common_styles(BACKGROUND_IMAGE)}</style>
</head>
<body>

    <!-- SESSION GUARD: Redirects to login.html if user is not logged in -->
    {get_session_guard_js()}

    <div class="page-wrapper">

        {build_header_html(show_about=False)}

        <!-- Breadcrumb: Home > Division Name -->
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

            <!-- Year Cards Grid -->
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


# =============================================================================
# PAGE GENERATOR 3: generate_projects_page()
# -----------------------------------------------------------------------------
# Generates "projects_<div_key>_<year>.html" — the project cards page.
#
# This page shows one Project Card for every project in a given division + year.
#
# Each card has two possible states:
#   ✔ Folder Linked   : path is set in projects_data.py → clicking opens the folder
#   ⚠ Not Linked      : path is empty → card is shown but cannot be clicked
#
# HOW FOLDER OPENING WORKS:
#   A JavaScript function builds a file:// URL from the folder path and opens it.
#   This works in Firefox. In Chrome, local file links may be blocked for security.
#   If folders don't open in Chrome, switch to Firefox.
#
# Parameters:
#   div_key : division key string (e.g. "offshore_works")
#   year    : integer year (e.g. 2018)
# =============================================================================

def generate_projects_page(div_key, year):

    div_info = DIVISIONS[div_key]
    div_name = div_info["name"]
    year_str = str(year)
    projects = div_info["projects"].get(year_str, [])

    # Build project cards
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
        # One card per project in the list
        for project in projects:
            project_name = project["name"]
            folder_path  = project.get("path", "")   # "" means not yet linked

            if folder_path:
                # ── Folder is linked ──
                # Clicking the card calls openFolder() to open the folder
                safe_path = folder_path.replace("\\", "/")
                project_cards_html += f"""
                    <div class="project-card"
                         onclick="openFolder('{safe_path}')"
                         title="Click to open project folder">
                        <span class="icon">📁</span>
                        <h5>{project_name}</h5>
                        <div class="year-tag">📅 {year_str}</div>
                        <span class="link-status linked">✔ Folder Linked</span>
                    </div>
                """
            else:
                # ── Folder not yet linked ──
                # Card is shown but not clickable; tooltip explains what to do
                project_cards_html += f"""
                    <div class="project-card no-link"
                         title="Folder not yet linked — open projects_data.py to add the path">
                        <span class="icon">📂</span>
                        <h5>{project_name}</h5>
                        <div class="year-tag">📅 {year_str}</div>
                        <span class="link-status not-linked">⚠ Not Linked</span>
                    </div>
                """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ONGC EPEC — {div_name} | {year_str}</title>
    <style>{get_common_styles(BACKGROUND_IMAGE)}</style>
</head>
<body>

    <!-- SESSION GUARD: Redirects to login.html if user is not logged in -->
    {get_session_guard_js()}

    <div class="page-wrapper">

        {build_header_html(show_about=False)}

        <!-- Breadcrumb: Home > Division > Year -->
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

            <!-- Project Cards Grid -->
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
         * openFolder()
         * ------------
         * Opens a local folder on the computer in Windows Explorer (or Mac Finder).
         *
         * HOW IT WORKS:
         *   Creates a temporary invisible link with a file:// URL pointing to the
         *   folder path, then simulates a click on it to open the folder.
         *
         * IMPORTANT NOTES:
         *   - Works best in Firefox.
         *   - Chrome blocks local file:// links for security. If folders do not
         *     open in Chrome, switch to Firefox.
         *   - Network drive paths also work:
         *     e.g. "//ServerName/ShareName/FolderName"
         *
         * Parameters:
         *   folderPath : the folder path string from projects_data.py
         *                (forward slashes, e.g. "C:/Projects/2018/ProjectName")
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


# =============================================================================
# MAIN FUNCTION: generate_all_files()
# -----------------------------------------------------------------------------
# This is the master function that generates EVERY HTML file for the dashboard.
#
# FILES GENERATED (in order):
#   1. login.html                          ← Entry point — open this first
#   2. index.html                          ← Home/Dashboard page
#   3. division_<div_key>.html             ← One per division (Year selection)
#   4. projects_<div_key>_<year>.html      ← One per division × year with projects
#
# All files are saved into the OUTPUT_FOLDER ("dashboard_output/").
# Run this function again anytime you make changes to projects_data.py or users.py.
# =============================================================================

def generate_all_files():

    # Create the output folder if it does not already exist
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    files_created = []

    # ── Step 1: Login Page ────────────────────────────────────────────────────
    # This is the entry point of the dashboard.
    # Users must log in here before they can see any other page.
    path = os.path.join(OUTPUT_FOLDER, "login.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(generate_login_page(
            company_name = COMPANY_NAME,
            dept_name    = DEPARTMENT_NAME,
            dept_short   = DEPARTMENT_SHORT,
            bg_image     = BACKGROUND_IMAGE,
        ))
    files_created.append("login.html  ← OPEN THIS FIRST IN YOUR BROWSER")

    # ── Step 2: Home Page ─────────────────────────────────────────────────────
    # Shown after successful login. Displays all division cards.
    path = os.path.join(OUTPUT_FOLDER, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(generate_home_page())
    files_created.append("index.html")

    # ── Step 3: Division Pages ────────────────────────────────────────────────
    # One page per division. Shows year cards for that division.
    # TO ADD A NEW DIVISION: add it in projects_data.py — it is picked up automatically.
    for div_key in DIVISIONS:
        filename = f"division_{div_key}.html"
        path = os.path.join(OUTPUT_FOLDER, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(generate_division_page(div_key))
        files_created.append(filename)

    # ── Step 4: Project Pages ─────────────────────────────────────────────────
    # One page per division × year (only for years that have at least 1 project).
    # TO ADD MORE PROJECTS: add them in projects_data.py — pages are auto-generated.
    for div_key, div_info in DIVISIONS.items():
        for year_str, projs in div_info["projects"].items():
            if projs:   # Only generate a page if the year has at least one project
                filename = f"projects_{div_key}_{year_str}.html"
                path = os.path.join(OUTPUT_FOLDER, filename)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(generate_projects_page(div_key, int(year_str)))
                files_created.append(filename)

    # ── Print Summary ─────────────────────────────────────────────────────────
    print("=" * 62)
    print("  ONGC EPEC Dashboard — Generation Complete!")
    print("=" * 62)
    print(f"\n  Output folder : {os.path.abspath(OUTPUT_FOLDER)}")
    print(f"  Files created : {len(files_created)}")
    print(f"\n  Files generated:")
    for f in files_created:
        print(f"    ✔  {f}")
    print("\n" + "=" * 62)
    print("  HOW TO START THE DASHBOARD:")
    print(f"  Open this file in your browser (Firefox recommended):")
    print(f"  {os.path.abspath(os.path.join(OUTPUT_FOLDER, 'login.html'))}")
    print("=" * 62 + "\n")

    return os.path.abspath(os.path.join(OUTPUT_FOLDER, "login.html"))


# =============================================================================
# ENTRY POINT
# =============================================================================
# Run this script directly to generate all dashboard files and open the
# login page automatically in the default browser.
# =============================================================================

if __name__ == "__main__":
    login_path = generate_all_files()
    print("  Opening Login Page in your browser...")
    webbrowser.open(f"file:///{login_path.replace(os.sep, '/')}")
