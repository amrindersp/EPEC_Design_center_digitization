===============================================================================
  ONGC EPEC — PROJECT DASHBOARD
  Complete Setup & Usage Guide
===============================================================================

FILES IN THIS FOLDER:
  dashboard_generator.py   → Main script — run this to build/rebuild the dashboard
  projects_data.py         → All project data is stored here (edit this for projects)
  import_from_excel.py     → Run this to import projects from an Excel file
  dashboard_output/        → Generated HTML files (created after first run)
  README.txt               → This file

===============================================================================
  STEP 1: REQUIREMENTS
===============================================================================

  Make sure Python is installed on your computer.
  Then install the required library by running in Command Prompt:

      pip install pandas openpyxl

===============================================================================
  STEP 2: RUN THE DASHBOARD (First Time)
===============================================================================

  1. Open Command Prompt (Windows: press Win+R, type "cmd", press Enter)
  2. Navigate to this folder:
         cd C:\Path\To\This\Folder
  3. Run the generator:
         python dashboard_generator.py
  4. The dashboard will open automatically in your browser!
     If it doesn't open, go to the "dashboard_output" folder
     and double-click "index.html"

===============================================================================
  STEP 3: ADD PROJECTS FROM EXCEL
===============================================================================

  a) Place your Excel file (.xlsx) in this same folder.
  b) Open "import_from_excel.py" in Notepad or any text editor.
  c) Edit these settings at the top of the file:

       EXCEL_FILENAME       = "your_excel_file.xlsx"
       DIVISION_KEY         = "offshore_works"       ← or "offshore_design" / "onshore"
       COLUMN_PROJECT_NAME  = "Project Name"         ← exact column heading in Excel
       COLUMN_YEAR          = "Year"                 ← exact column heading in Excel

  d) Save and run:
         python import_from_excel.py

  e) Then rebuild the dashboard:
         python dashboard_generator.py

===============================================================================
  STEP 4: LINK PROJECT FOLDERS
===============================================================================

  After importing projects, each project card will show "⚠ Not Linked".
  To link a folder:

  1. Open "projects_data.py" in Notepad or any text editor.
  2. Find the project by name. It will look like this:
         {"name": "Heera Redevelopment", "path": ""},

  3. Replace the empty "" with the folder path:
         {"name": "Heera Redevelopment", "path": "C:/Projects/OffshoreWorks/2015/Heera"},

     IMPORTANT RULES FOR PATHS:
     ✔ Use forward slashes  /  (not backslashes  \ )
     ✔ Windows: "C:/Users/YourName/Projects/FolderName"
     ✔ Network drives: "//ServerName/ShareName/FolderName"
     ✗ Do NOT use backslashes: "C:\Projects\Folder"   ← WRONG

  4. Save projects_data.py
  5. Run: python dashboard_generator.py

  When you click the linked card in the browser, the folder will open
  in Windows Explorer.

  NOTE: Folder opening via browser requires Firefox or a compatible browser.
  If it does not work in Chrome, try Firefox.

===============================================================================
  STEP 5: ADD BACKGROUND IMAGE
===============================================================================

  1. Place your image file (JPG or PNG) in the same folder as this script.
  2. Open "dashboard_generator.py" in a text editor.
  3. Find this line near the top:
         BACKGROUND_IMAGE = ""
  4. Change it to your image filename:
         BACKGROUND_IMAGE = "background.jpg"
  5. Run: python dashboard_generator.py

===============================================================================
  ADDING MORE DIVISIONS (e.g., for future departments)
===============================================================================

  Open "projects_data.py" and copy the block for any existing division.
  Paste it at the end (before the final closing "}" bracket).
  Change the key name, "name", "icon", and "description".
  Then run dashboard_generator.py.

===============================================================================
  TROUBLESHOOTING
===============================================================================

  "Module not found: pandas"   → Run: pip install pandas openpyxl
  "File not found" error       → Make sure you are in the correct folder in CMD
  Folder does not open         → Try using Firefox browser; Chrome blocks local file links
  Dashboard looks wrong        → Delete "dashboard_output" folder and re-run the generator

===============================================================================
  CONTACT / FEEDBACK
===============================================================================

  For modifications or new features, share the updated requirement
  along with this script with your developer.

===============================================================================
