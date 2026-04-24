"""
=============================================================================
ONGC EPEC — Excel Project Importer
=============================================================================

HOW TO USE:
1. Place your Excel file (.xlsx) in the SAME folder as this script
2. Open this file and set EXCEL_FILENAME and DIVISION_KEY below
3. Set the correct column names from your Excel file
4. Run: python import_from_excel.py
5. Then run: python dashboard_generator.py to rebuild the dashboard

EXCEL FILE FORMAT EXPECTED:
   Your Excel file should have at minimum these two columns:
   - One column with the PROJECT NAME
   - One column with the YEAR of completion (as a 4-digit number, e.g. 2018)

   You can also have an optional column for the FOLDER PATH.

=============================================================================
"""

import pandas as pd
import os
import sys

# ─────────────────────────────────────────────────────────────────────────────
# ▼▼▼  SETTINGS — EDIT THESE BEFORE RUNNING  ▼▼▼
# ─────────────────────────────────────────────────────────────────────────────

# Name of your Excel file (must be in the same folder as this script)
EXCEL_FILENAME = "Onshore_Projects.xlsx"

# Which division to import into?
# Options: "offshore_design" | "offshore_works" | "onshore"
DIVISION_KEY = "onshore"

# Column name in your Excel file that contains the PROJECT NAME
# (Check your Excel file — it must match exactly, including capitals)
COLUMN_PROJECT_NAME = "Project Name"

# Column name in your Excel file that contains the COMPLETION YEAR
COLUMN_YEAR = "Year"

# (Optional) Column name for folder path — leave as "" if your Excel has no path column
COLUMN_PATH = ""

# Which sheet in Excel to read? (0 = first sheet, or write sheet name like "Sheet1")
EXCEL_SHEET = 0

# ▲▲▲  END OF SETTINGS  ▲▲▲
# ─────────────────────────────────────────────────────────────────────────────


def read_excel_projects():
    """
    Reads the Excel file and returns a dict like:
    {
        "2015": [{"name": "Project A", "path": ""}, ...],
        "2018": [{"name": "Project B", "path": ""}, ...],
        ...
    }
    """
    # Check if the file exists
    if not os.path.exists(EXCEL_FILENAME):
        print(f"\n  ERROR: File not found: '{EXCEL_FILENAME}'")
        print(f"  Please place the Excel file in this folder:")
        print(f"  {os.path.abspath('.')}\n")
        sys.exit(1)

    # Read the Excel file
    print(f"\n  Reading: {EXCEL_FILENAME} ...")
    df = pd.read_excel(EXCEL_FILENAME, sheet_name=EXCEL_SHEET)

    # Show what columns were found (helpful for debugging)
    print(f"  Columns found in Excel: {list(df.columns)}")
    print(f"  Total rows found: {len(df)}")

    # Check that required columns exist
    if COLUMN_PROJECT_NAME not in df.columns:
        print(f"\n  ERROR: Column '{COLUMN_PROJECT_NAME}' not found in Excel.")
        print(f"  Available columns: {list(df.columns)}")
        print(f"  Please update COLUMN_PROJECT_NAME in this script.\n")
        sys.exit(1)

    if COLUMN_YEAR not in df.columns:
        print(f"\n  ERROR: Column '{COLUMN_YEAR}' not found in Excel.")
        print(f"  Available columns: {list(df.columns)}")
        print(f"  Please update COLUMN_YEAR in this script.\n")
        sys.exit(1)

    # Build the projects dictionary grouped by year
    projects_by_year = {}

    skipped = 0
    for _, row in df.iterrows():
        project_name = str(row[COLUMN_PROJECT_NAME]).strip()
        year_raw     = row[COLUMN_YEAR]

        # Skip blank rows
        if not project_name or project_name.lower() in ("nan", "none", ""):
            skipped += 1
            continue

        # Convert year to string
        try:
            year_str = str(int(float(str(year_raw).strip())))
        except (ValueError, TypeError):
            print(f"  WARNING: Skipping row with invalid year '{year_raw}' for project '{project_name}'")
            skipped += 1
            continue

        # Get folder path if the column exists
        folder_path = ""
        if COLUMN_PATH and COLUMN_PATH in df.columns:
            raw_path = str(row[COLUMN_PATH]).strip()
            if raw_path.lower() not in ("nan", "none", ""):
                # Normalize path to use forward slashes
                folder_path = raw_path.replace("\\", "/")

        # Add to dictionary
        if year_str not in projects_by_year:
            projects_by_year[year_str] = []

        projects_by_year[year_str].append({
            "name": project_name,
            "path": folder_path
        })

    if skipped:
        print(f"  Skipped {skipped} blank/invalid rows.")

    return projects_by_year


def update_projects_data(new_projects_by_year):
    """
    Reads projects_data.py, updates the specified division's projects
    with the imported data, and writes the file back.
    """
    # Import current data
    import projects_data
    divisions = projects_data.DIVISIONS

    if DIVISION_KEY not in divisions:
        print(f"\n  ERROR: Division key '{DIVISION_KEY}' not found in projects_data.py")
        print(f"  Available divisions: {list(divisions.keys())}\n")
        sys.exit(1)

    # Update projects for the target division
    # We REPLACE the projects for each year that appears in the Excel data
    # Years not in Excel are left unchanged
    total_added = 0
    for year_str, projects in new_projects_by_year.items():
        divisions[DIVISION_KEY]["projects"][year_str] = projects
        total_added += len(projects)
        print(f"  Year {year_str}: {len(projects)} project(s) imported")

    # Write the updated data back to projects_data.py
    write_projects_data_file(divisions)

    print(f"\n  ✔ Total projects imported: {total_added}")
    print(f"  ✔ Division updated: {DIVISION_KEY}")
    print(f"  ✔ projects_data.py has been updated.\n")


def write_projects_data_file(divisions):
    """
    Writes the DIVISIONS dictionary back to projects_data.py
    in a clean, readable format.
    """
    lines = []
    lines.append('"""')
    lines.append('=============================================================================')
    lines.append('ONGC EPEC — PROJECT DATA FILE')
    lines.append('=============================================================================')
    lines.append('')
    lines.append('This is the ONLY file you need to edit to manage projects.')
    lines.append('')
    lines.append('HOW TO ADD A NEW PROJECT:')
    lines.append('   1. Find the correct division (e.g., "offshore_works")')
    lines.append('   2. Find the correct year (e.g., "2018")')
    lines.append('   3. Add a new line:  {"name": "Your Project Name", "path": ""},')
    lines.append('   4. Save this file and run dashboard_generator.py to rebuild.')
    lines.append('')
    lines.append('HOW TO LINK A PROJECT FOLDER:')
    lines.append('   Replace the empty path "" with the actual folder path.')
    lines.append('   Windows: "C:/Projects/OffshoreWorks/2018/ProjectAlpha"')
    lines.append('   Use forward slashes "/" even on Windows.')
    lines.append('"""')
    lines.append('')
    lines.append('')
    lines.append('DIVISIONS = {')
    lines.append('')

    for div_key, div_info in divisions.items():
        lines.append(f'    # {"─" * 65}')
        lines.append(f'    # DIVISION: {div_info["name"].upper()}')
        lines.append(f'    # {"─" * 65}')
        lines.append(f'    "{div_key}": {{')
        lines.append(f'        "name":        "{div_info["name"]}",')
        lines.append(f'        "icon":        "{div_info.get("icon", "🏗️")}",')
        lines.append(f'        "description": "{div_info.get("description", "")}",')
        lines.append(f'        "projects": {{')
        lines.append('')

        for year in range(2010, 2027):
            year_str = str(year)
            projects = div_info["projects"].get(year_str, [])
            lines.append(f'            "{year_str}": [')

            if projects:
                for p in projects:
                    name = p["name"].replace('"', '\\"')
                    path = p.get("path", "").replace('"', '\\"')
                    lines.append(f'                {{"name": "{name}", "path": "{path}"}},')
            else:
                lines.append(f'                # No projects for {year_str}')
                lines.append(f'                # {{"name": "Project Name", "path": ""}},')

            lines.append(f'            ],')
            lines.append('')

        lines.append(f'        }}')
        lines.append(f'    }},  # ← End of {div_info["name"]}')
        lines.append('')

    lines.append('}  # ← End of DIVISIONS')
    lines.append('')

    # Write file
    content = "\n".join(lines)
    with open("projects_data.py", "w", encoding="utf-8") as f:
        f.write(content)


# ─────────────────────────────────────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  ONGC EPEC — Excel Project Importer")
    print("=" * 60)
    print(f"\n  Division  : {DIVISION_KEY}")
    print(f"  Excel file: {EXCEL_FILENAME}")

    projects_by_year = read_excel_projects()
    update_projects_data(projects_by_year)

    print("=" * 60)
    print("  NEXT STEP: Run dashboard_generator.py to rebuild the dashboard.")
    print("=" * 60 + "\n")
