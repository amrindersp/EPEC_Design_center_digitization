"""
=============================================================================
ONGC EPEC — USER CREDENTIALS FILE
=============================================================================

This file stores all authorized User IDs and Passwords for the Dashboard.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HOW TO ADD A NEW USER:
   Copy one of the existing blocks below and fill in the details.

   Example — Add a new user at the bottom of the USERS list:
       {
           "user_id"    : "jsmith",
           "password"   : "Pass@2024",
           "full_name"  : "John Smith",
           "role"       : "Engineer",
           "division"   : "Offshore Works",
       },

HOW TO REMOVE A USER:
   Delete their entire block (from the opening { to the closing },)

HOW TO CHANGE A PASSWORD:
   Find the user's block and update the "password" field.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FIELD DESCRIPTIONS:
   user_id   → The login username (no spaces, case-insensitive)
   password  → The login password (case-sensitive)
   full_name → Display name shown after login (e.g., "Welcome, John Smith")
   role      → Job role shown on dashboard (e.g., "Senior Engineer")
   division  → Division the user belongs to (shown as info only)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECURITY NOTE:
   This is a local HTML-based dashboard used within a controlled
   office environment. Passwords are stored as plain text here.
   Do not share this file outside your organization.

=============================================================================
"""

# =============================================================================
# USERS LIST
# =============================================================================
# Each user is one block { } in the list below.
# Add as many users as needed following the same pattern.
# =============================================================================

USERS = [

    # ── User 1 ──────────────────────────────────────────────────────────────
    {
        "user_id"    : "admin",          # ← Login username
        "password"   : "Admin@123",      # ← Login password (fill in your own)
        "full_name"  : "Administrator",  # ← Name shown after login
        "role"       : "Dashboard Admin",
        "division"   : "EPEC",
    },

    # ── User 2 ──────────────────────────────────────────────────────────────
    {
        "user_id"    : "user01",         # ← Fill in User ID
        "password"   : "",               # ← Fill in Password
        "full_name"  : "",               # ← Fill in Full Name
        "role"       : "",               # ← Fill in Role
        "division"   : "Offshore Design",
    },

    # ── User 3 ──────────────────────────────────────────────────────────────
    {
        "user_id"    : "user02",
        "password"   : "",
        "full_name"  : "",
        "role"       : "",
        "division"   : "Offshore Works",
    },

    # ── User 4 ──────────────────────────────────────────────────────────────
    {
        "user_id"    : "user03",
        "password"   : "",
        "full_name"  : "",
        "role"       : "",
        "division"   : "Onshore Projects",
    },

    # ── ADD MORE USERS BELOW THIS LINE ──────────────────────────────────────
    # Copy and paste the block below, then fill in the details:
    #
    # {
    #     "user_id"    : "newuser",
    #     "password"   : "YourPassword",
    #     "full_name"  : "Full Name Here",
    #     "role"       : "Job Role Here",
    #     "division"   : "Division Name Here",
    # },

]
