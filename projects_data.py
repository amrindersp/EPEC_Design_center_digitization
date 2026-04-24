"""
=============================================================================
ONGC EPEC — PROJECT DATA FILE
=============================================================================

This is the ONLY file you need to edit to manage projects.

HOW TO ADD A NEW PROJECT:
   1. Find the correct division (e.g., "offshore_works")
   2. Find the correct year (e.g., "2018")
   3. Add a new line:  {"name": "Your Project Name", "path": ""},
   4. Save this file and run dashboard_generator.py to rebuild.

HOW TO LINK A PROJECT FOLDER:
   Replace the empty path "" with the actual folder path.
   Windows: "C:/Projects/OffshoreWorks/2018/ProjectAlpha"
   Use forward slashes "/" even on Windows.
"""


DIVISIONS = {

    # ─────────────────────────────────────────────────────────────────
    # DIVISION: OFFSHORE DESIGN
    # ─────────────────────────────────────────────────────────────────
    "offshore_design": {
        "name":        "Offshore Design",
        "icon":        "📐",
        "description": "Engineering design projects for offshore platforms, structures, and facilities.",
        "projects": {

            "2010": [
                # No projects for 2010
                # {"name": "Project Name", "path": ""},
            ],

            "2011": [
                # No projects for 2011
                # {"name": "Project Name", "path": ""},
            ],

            "2012": [
                # No projects for 2012
                # {"name": "Project Name", "path": ""},
            ],

            "2013": [
                # No projects for 2013
                # {"name": "Project Name", "path": ""},
            ],

            "2014": [
                # No projects for 2014
                # {"name": "Project Name", "path": ""},
            ],

            "2015": [
                # No projects for 2015
                # {"name": "Project Name", "path": ""},
            ],

            "2016": [
                # No projects for 2016
                # {"name": "Project Name", "path": ""},
            ],

            "2017": [
                # No projects for 2017
                # {"name": "Project Name", "path": ""},
            ],

            "2018": [
                # No projects for 2018
                # {"name": "Project Name", "path": ""},
            ],

            "2019": [
                # No projects for 2019
                # {"name": "Project Name", "path": ""},
            ],

            "2020": [
                # No projects for 2020
                # {"name": "Project Name", "path": ""},
            ],

            "2021": [
                # No projects for 2021
                # {"name": "Project Name", "path": ""},
            ],

            "2022": [
                # No projects for 2022
                # {"name": "Project Name", "path": ""},
            ],

            "2023": [
                # No projects for 2023
                # {"name": "Project Name", "path": ""},
            ],

            "2024": [
                # No projects for 2024
                # {"name": "Project Name", "path": ""},
            ],

            "2025": [
                # No projects for 2025
                # {"name": "Project Name", "path": ""},
            ],

            "2026": [
                # No projects for 2026
                # {"name": "Project Name", "path": ""},
            ],

        }
    },  # ← End of Offshore Design

    # ─────────────────────────────────────────────────────────────────
    # DIVISION: OFFSHORE PROJECTS
    # ─────────────────────────────────────────────────────────────────
    "offshore_works": {
        "name":        "Offshore Projects",
        "icon":        "🌊",
        "description": "Construction, installation and commissioning of offshore oil & gas infrastructure.",
        "projects": {

            "2010": [
                {"name": "BB-BL-RP II", "path": ""},
                {"name": "HEERA REDEVELOPMENT PROJECT (HRP)", "path": ""},
                {"name": "NQ COMPLEX RE-CONSTRUCTION PROJECT (NQRC)", "path": ""},
            ],

            "2011": [
                {"name": "REVAMPING OF 26 WELL PLATFORMS PROJECT (26 WPP)", "path": ""},
                {"name": "B193 5 WELLHEAD PLATFORMS (B-193 5WPP)", "path": ""},
                {"name": "MH NORTH REDEVELOPMENT PHASE-II 4WELL PLATFORM PROJECT (MHNRD PH II 4   WPP)", "path": ""},
                {"name": "RS 12 WELL PLATFORM PROJECT", "path": ""},
            ],

            "2012": [
                {"name": "B‐SERIES, N‐15 & N‐16 PIPELINE PROJECT", "path": ""},
                {"name": "MHN PGC PROJECT", "path": ""},
                {"name": "MHN PIPELINE PROJECT", "path": ""},
                {"name": "MHN PROCESS PLATFORM AND LQ PROJECT", "path": ""},
                {"name": "MNW-NF BRIDGE PROJECT", "path": ""},
                {"name": "NEELAM HEERA RECONSTRUCTION PROJECT (NHRC)", "path": ""},
                {"name": "WIN REVAMP PROJECT", "path": ""},
            ],

            "2013": [
                {"name": "CLUSTER-7 WELL PLATFORMS PROJECT", "path": ""},
                {"name": "WO-16 CLUSTER & SB-14 WELL PLATFORM PROJECT", "path": ""},
            ],

            "2014": [
                {"name": "PIPELINE REPLACEMENT PROJECT 2 (PRP-2)", "path": ""},
                {"name": "OFFSHORE GRID INTERCONNECTIVITY - POWER TO ESP PROJECT (OGIP)", "path": ""},
                {"name": "B127 CLUSTER WELL PLATFORM PROJECT", "path": ""},
            ],

            "2015": [
                {"name": "HRP-II 3 WELL PLATFORM PROJECT", "path": ""},
                {"name": "PIPELINE REPLACEMENT PROJECT 3 (PRP-3)", "path": ""},
            ],

            "2016": [
                {"name": "RE-ROUTING SECTION OF 42 INCH SBHT PIPELINE PROJECT UMBHRAT, HAZIRA", "path": ""},
                {"name": "ADDITIONAL DEVELOPMENT OF VASAI EAST PROJECT (ADVEP)", "path": ""},
            ],

            "2017": [
                {"name": "C26 CLUSTER & B173A-B WELL PLATFORM PROJECT", "path": ""},
                {"name": "BASSEIN DEVELOPMENT PROJECT", "path": ""},
            ],

            "2018": [
                {"name": "B127 CLUSTER PIPELINE RTR PROJECT", "path": ""},
                {"name": "PRP-4", "path": ""},
                {"name": "MHNRD Ph III", "path": ""},
            ],

            "2019": [
                {"name": "DAMAN DEVELOPMENT PROJECT (DDP)", "path": ""},
                {"name": "NEELAM REDEVELOPMENT AND B173AC PROJECT (NRDP)", "path": ""},
                {"name": "BASSEIN DEVELOPMENT 3 WELL PLATFORM PROJECT (BD3WPP)", "path": ""},
                {"name": "NBP Field Ph IV", "path": ""},
            ],

            "2020": [
                {"name": "Mumbai High South redevelopment Phase-III", "path": ""},
                {"name": "PRP-5", "path": ""},
                {"name": "Neelam  Redevelopment Plan for Exploitation of Bassein & Mukta pay-Neelam field", "path": ""},
            ],

            "2021": [
                {"name": "R SERIES 5 WHP & PIPELINE PROJECT (RS5WPPP)", "path": ""},
                {"name": "NEW WATER INJECTION SOUTH - R PLATFORM PROJECT (NWIS-R)", "path": ""},
                {"name": "Development of Cluster-8 Marginal Field Project", "path": ""},
            ],

            "2022": [
                {"name": "PRP-6", "path": ""},
                {"name": "Mumbai High South redevelopment Phase-IV", "path": ""},
            ],

            "2023": [
                {"name": "HEERA REDEVELOPMENT PROJECT (HRP) Phase III", "path": ""},
            ],

            "2024": [
                {"name": "Clamp On projects (13 Platforms)", "path": ""},
                {"name": "2 Clamp on Project (2CP)", "path": ""},
                {"name": "BB-BL-RP-IV", "path": ""},
            ],

            "2025": [
                {"name": "PRP-7", "path": ""},
                {"name": "MHNRD Ph IV", "path": ""},
            ],

            "2026": [
                {"name": "PRPP", "path": ""},
                {"name": "T&I 98/2", "path": ""},
            ],

        }
    },  # ← End of Offshore Projects

    # ─────────────────────────────────────────────────────────────────
    # DIVISION: ONSHORE PROJECTS
    # ─────────────────────────────────────────────────────────────────
    "onshore": {
        "name":        "Onshore Projects",
        "icon":        "🏭",
        "description": "Onshore drilling, production, pipeline, and plant engineering projects.",
        "projects": {

            "2010": [
                # No projects for 2010
                # {"name": "Project Name", "path": ""},
            ],

            "2011": [
                # No projects for 2011
                # {"name": "Project Name", "path": ""},
            ],

            "2012": [
                # No projects for 2012
                # {"name": "Project Name", "path": ""},
            ],

            "2013": [
                # No projects for 2013
                # {"name": "Project Name", "path": ""},
            ],

            "2014": [
                {"name": "Surface facilities at Cauvery Asset", "path": ""},
            ],

            "2015": [
                # No projects for 2015
                # {"name": "Project Name", "path": ""},
            ],

            "2016": [
                {"name": "6 ETPs Ahmedabad and Ankleshwar", "path": ""},
                {"name": "UGFPS Ankleshwar", "path": ""},
                {"name": "6 ETPs Ahmedabad and Ankleshwar 1", "path": ""},
            ],

            "2017": [
                {"name": "3 ETPs Rajahmundry", "path": ""},
            ],

            "2018": [
                {"name": "PRP Ahmedabad", "path": ""},
                {"name": "Gas Compressors Ahmedabad", "path": ""},
                {"name": "Nawagam - Koyali Pipeline", "path": ""},
                {"name": "Gamij Redevelopment", "path": ""},
                {"name": "1 ETP at GGS Nada", "path": ""},
                {"name": "6 PLRP  Assam", "path": ""},
                {"name": "3 ETPs Mehsana", "path": ""},
            ],

            "2019": [
                {"name": "Assam Renewal Project", "path": ""},
                {"name": "1 ETP and 3 ETP cum WIPs Assam", "path": ""},
                {"name": "MB Lal at  Mehsana", "path": ""},
            ],

            "2020": [
                {"name": "MB Lal at  Ahmedabad", "path": ""},
                {"name": "Up-gradation of Fire Fighting Facilities at Four(4) CTFs of Mehsana Asset (UGFFS-MHN)", "path": ""},
            ],

            "2021": [
                {"name": "Pipeline Network Project, Geleki, Assam Asset", "path": ""},
                {"name": "Madanam CPF & PLP Project", "path": ""},
                {"name": "Four Installation Revamping Project, Mehsana", "path": ""},
                {"name": "Construction of Produced Water Treatment Plant of 4000 M3/day capacity at North Santhal in Mehsana Asset", "path": ""},
                {"name": "Creation of Gojalia GCS, Tripura Asset", "path": ""},
            ],

            "2022": [
                {"name": "MB Lal at  CPF Gandhar and CTF Ankleshwar", "path": ""},
                {"name": "MB Lal at  Geleki", "path": ""},
                {"name": "Construction of Crude Oil Storage Tanks & Firefighting facilities at Cauvery Asset", "path": ""},
                {"name": "Nandasan Surface Facilities Project, Mehsana Asset", "path": ""},
                {"name": "Gamnewala GCS and Pipeline", "path": ""},
            ],

            "2023": [
                {"name": "Booster Gas Compressor Project, Ramol, Ahmedabad", "path": ""},
                {"name": "Hot Flare System Ahmedabad", "path": ""},
                {"name": "UGFS-AAC", "path": ""},
                {"name": "GCP Ankleshwar", "path": ""},
                {"name": "GRP- Ankleshwar", "path": ""},
                {"name": "CBM Bokaro Project", "path": ""},
                {"name": "Anklav Surface Facilities Cambay", "path": ""},
                {"name": "Flare Stacks Installation & Other Installation works at Cauvery Asset (Flare_cav)", "path": ""},
            ],

            "2024": [
                {"name": "Balance work of Up-gradation of Fire Fighting System at Ankleshwar, Ahmedabad, Assam & Cauvery Assets (UGFS-AAAC)", "path": ""},
                {"name": "RFS Assam Group A", "path": ""},
                {"name": "GDU-DPD Cauvery", "path": ""},
                {"name": "Produced Water Treatment Plant Project at Sobhasan & Bechraji fields of Mehsana Asset (2PWTP Mehsana)", "path": ""},
                {"name": "GDU-DPD Rajahmundry", "path": ""},
            ],

            "2025": [
                {"name": "RFS Assam Group B", "path": ""},
                {"name": "GCP Lakwa", "path": ""},
                {"name": "North Kadi Produced water Treatment Plant, Mehsana", "path": ""},
                {"name": "Replacement of Air Compressor At Mehsana( RAC Santhal)", "path": ""},
                {"name": "Revamping of Fire Protection systems at installations of Mehsana Asset(RFPS Mehsana)", "path": ""},
                {"name": "North Kadi Polymer Flooding Project", "path": ""},
                {"name": "Revamping of Slug Catcher, Uran", "path": ""},
            ],

            "2026": [
                {"name": "Laying of Pipelines in Nawagam & Kalol", "path": ""},
                {"name": "ETP Jahlora and South Kadi", "path": ""},
                {"name": "Replacement of pipelines of RDS and Satellite fields of Assam Asset(PNP RDS)", "path": ""},
                {"name": "PNP Laiplinggaon", "path": ""},
                {"name": "Borholla GGS Life Extension Project", "path": ""},
                {"name": "Creation of HP Gas Compression Facilities at Geleki, Assam Asset.", "path": ""},
                {"name": "Development of Jharia CBM Block- Facility", "path": ""},
                {"name": "Rerouting of 10” ND Trunk pipeline in Akholjuni area at Cambay Asset", "path": ""},
                {"name": "Restoration of Gas Terminal Ph-I(Part A)", "path": ""},
                {"name": "Restoration of Gas Terminal Part B", "path": ""},
                {"name": "Borholla GGS Life Extension Project", "path": ""},
                {"name": "Old Pipeline Replacement Project, Mehsana Asset", "path": ""},
                {"name": "Air and Gas PRP - Mehsana Asset", "path": ""},
                {"name": "Construction of 66-11 KV GIS Substation at Sobhasan GGS II", "path": ""},
                {"name": "Construction of 66-11 KV GIS Substation at Linch GGS", "path": ""},
                {"name": "Redevelopment of Sobhasan Complex", "path": ""},
                {"name": "Re-Development of Linch Field", "path": ""},
                {"name": "Creation of Gas Compression and Dehydration facilities Jotana GGS MHN Asset", "path": ""},
                {"name": "Gas Dehydration Facilities Tripura Asset", "path": ""},
                {"name": "CSU Off Gas Compressor, Uran", "path": ""},
                {"name": "ISBL PRP, URAN", "path": ""},
                {"name": "Replacement of Flare Pipe Network, Uran", "path": ""},
            ],

        }
    },  # ← End of Onshore Projects

}  # ← End of DIVISIONS
