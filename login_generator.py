"""
=============================================================================
ONGC EPEC — Login Page Generator
=============================================================================

This script generates the login page (login.html) for the Dashboard.
It reads all users from users.py and embeds their credentials securely
into the HTML page using JavaScript so the browser can validate them.

This file is called automatically by dashboard_generator.py.
You do NOT need to run this file separately.

=============================================================================
"""

from users import USERS


def generate_login_page(company_name, dept_name, dept_short,
                        bg_image="", common_styles_fn=None):
    """
    Generates the login.html page.

    Parameters:
        company_name      : e.g. "ONGC"
        dept_name         : e.g. "Engineering and Projects Excellence Centre"
        dept_short        : e.g. "EPEC"
        bg_image          : background image filename (empty = use gradient)
        common_styles_fn  : the get_common_styles() function from dashboard_generator
    """

    # ── Build the user credentials as a JavaScript object ──
    # Only user_id and password are embedded for login validation.
    # Full name, role, division are also embedded for the welcome display.
    js_users = "[\n"
    for u in USERS:
        uid      = u.get("user_id",   "").strip()
        pwd      = u.get("password",  "").strip()
        name     = u.get("full_name", uid).strip() or uid
        role     = u.get("role",      "").strip()
        division = u.get("division",  "").strip()

        # Skip users who have no user_id set
        if not uid:
            continue

        js_users += f'        {{ id: "{uid}", pw: "{pwd}", name: "{name}", role: "{role}", div: "{division}" }},\n'
    js_users += "    ]"

    # ── Background CSS ──
    if bg_image:
        bg_css = f"""
            background-image: url('{bg_image}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        """
    else:
        bg_css = """
            background: linear-gradient(135deg, #0a1628 0%, #0d2137 40%, #0a2e1f 100%);
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ONGC EPEC — Login</title>
    <style>
        /* ── Reset ── */
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
            min-height: 100vh;
            {bg_css}
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}

        /* Dark overlay */
        body::before {{
            content: '';
            position: fixed;
            inset: 0;
            background: rgba(5, 15, 30, 0.78);
            z-index: 0;
        }}

        /* ── Login Container ── */
        .login-wrapper {{
            position: relative;
            z-index: 1;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 30px 20px;
        }}

        /* ── Top Logo / Branding ── */
        .brand-header {{
            text-align: center;
            margin-bottom: 36px;
        }}

        .ongc-logo-img {{
            width: 80px;
            height: 80px;
            object-fit: contain;
            margin-bottom: 16px;
        }}


        .brand-header h1 {{
            font-size: 26px;
            font-weight: 800;
            color: #f0a500;
            letter-spacing: 4px;
            text-transform: uppercase;
        }}

        .brand-header h2 {{
            font-size: 13px;
            color: #7a9ab8;
            letter-spacing: 2px;
            margin-top: 6px;
            font-weight: 400;
        }}

        .brand-divider {{
            width: 60px;
            height: 2px;
            background: linear-gradient(90deg, #f0a500, #00a86b);
            margin: 14px auto 0;
            border-radius: 2px;
        }}

        /* ── Login Card ── */
        .login-card {{
            background: linear-gradient(145deg, rgba(10,30,60,0.95), rgba(10,46,31,0.92));
            border: 1px solid rgba(240,165,0,0.3);
            border-radius: 18px;
            padding: 42px 44px;
            width: 100%;
            max-width: 440px;
            box-shadow: 0 24px 80px rgba(0,0,0,0.6);
        }}

        .login-card h3 {{
            font-size: 17px;
            color: #b0c8e0;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 28px;
            text-align: center;
            font-weight: 500;
        }}

        /* ── Form Fields ── */
        .field-group {{
            margin-bottom: 20px;
        }}

        .field-group label {{
            display: block;
            font-size: 12px;
            color: #7a9ab8;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 8px;
            font-weight: 600;
        }}

        .field-group input {{
            width: 100%;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 8px;
            padding: 13px 16px;
            font-size: 15px;
            color: #e8e8e8;
            outline: none;
            transition: all 0.25s;
            letter-spacing: 0.5px;
        }}

        .field-group input:focus {{
            border-color: #f0a500;
            background: rgba(240,165,0,0.06);
            box-shadow: 0 0 0 3px rgba(240,165,0,0.12);
        }}

        .field-group input::placeholder {{
            color: rgba(255,255,255,0.2);
        }}

        /* ── Password Toggle ── */
        .password-wrap {{
            position: relative;
        }}

        .password-wrap input {{
            padding-right: 48px;
        }}

        .toggle-pw {{
            position: absolute;
            right: 14px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            color: #7a9ab8;
            font-size: 18px;
            cursor: pointer;
            padding: 0;
            transition: color 0.2s;
        }}

        .toggle-pw:hover {{ color: #f0a500; }}

        /* ── Error Message ── */
        .error-msg {{
            background: rgba(220, 50, 50, 0.12);
            border: 1px solid rgba(220,50,50,0.35);
            border-radius: 8px;
            padding: 11px 16px;
            color: #ff8080;
            font-size: 13px;
            text-align: center;
            margin-bottom: 18px;
            display: none;
            letter-spacing: 0.5px;
        }}

        .error-msg.visible {{ display: block; }}

        /* ── Login Button ── */
        .btn-login {{
            width: 100%;
            padding: 14px;
            background: linear-gradient(90deg, #003c78, #005a40);
            border: 1px solid rgba(240,165,0,0.35);
            border-radius: 10px;
            color: white;
            font-size: 15px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            cursor: pointer;
            transition: all 0.25s;
            margin-top: 8px;
        }}

        .btn-login:hover {{
            background: linear-gradient(90deg, #004e9a, #007a55);
            box-shadow: 0 6px 20px rgba(240,165,0,0.2);
            transform: translateY(-1px);
        }}

        .btn-login:active {{
            transform: translateY(0);
        }}

        /* ── Loading Spinner (shown during login) ── */
        .btn-login.loading {{
            opacity: 0.7;
            pointer-events: none;
        }}

        /* ── Footer ── */
        .login-footer {{
            margin-top: 28px;
            text-align: center;
            font-size: 11px;
            color: rgba(255,255,255,0.2);
            letter-spacing: 1px;
        }}

        /* ── Caps Lock Warning ── */
        .capslock-warn {{
            font-size: 11px;
            color: #f0a500;
            margin-top: 5px;
            display: none;
        }}

        .capslock-warn.visible {{ display: block; }}
    </style>
</head>
<body>

    <div class="login-wrapper">

        <!-- Brand Header -->
        <div class="brand-header">
            <img src="ongc_logo.png" class="ongc-logo-img">
            <h1>{company_name}</h1>
            <h2>{dept_name} &mdash; {dept_short}</h2>
            <div class="brand-divider"></div>
        </div>

        <!-- Login Card -->
        <div class="login-card">
            <h3>🔒 Authorized Access Only</h3>

            <!-- Error message (hidden by default) -->
            <div class="error-msg" id="errorMsg">
                ✕ &nbsp; Invalid User ID or Password. Please try again.
            </div>

            <!-- User ID Field -->
            <div class="field-group">
                <label for="userId">User ID</label>
                <input type="text"
                       id="userId"
                       placeholder="Enter your User ID"
                       autocomplete="username"
                       onkeydown="if(event.key==='Enter') attemptLogin()">
            </div>

            <!-- Password Field -->
            <div class="field-group">
                <label for="password">Password</label>
                <div class="password-wrap">
                    <input type="password"
                           id="password"
                           placeholder="Enter your Password"
                           autocomplete="current-password"
                           onkeydown="handlePasswordKey(event)"
                           onkeyup="checkCapsLock(event)">
                    <!-- Show/Hide password toggle -->
                    <button class="toggle-pw" onclick="togglePassword()" title="Show/Hide Password">👁</button>
                </div>
                <div class="capslock-warn" id="capsWarn">⚠ Caps Lock is ON</div>
            </div>

            <!-- Login Button -->
            <button class="btn-login" id="loginBtn" onclick="attemptLogin()">
                Login →
            </button>
        </div>

        <!-- Footer -->
        <div class="login-footer">
            {company_name} &bull; {dept_short} &bull; Restricted Access
        </div>

    </div>

    <script>
        // ── User Credentials (embedded from users.py) ──
        // Each entry: {{ id, pw, name, role, div }}
        const USERS = {js_users};

        /**
         * attemptLogin:
         * Reads the User ID and Password entered by the user.
         * Compares against the USERS list.
         * If matched → saves session info and redirects to dashboard.
         * If not matched → shows error message.
         */
        function attemptLogin() {{
            var enteredId = document.getElementById('userId').value.trim().toLowerCase();
            var enteredPw = document.getElementById('password').value;

            // Clear previous error
            document.getElementById('errorMsg').classList.remove('visible');

            // Check for empty fields
            if (!enteredId || !enteredPw) {{
                document.getElementById('errorMsg').textContent = '✕  Please enter both User ID and Password.';
                document.getElementById('errorMsg').classList.add('visible');
                return;
            }}

            // Search for matching user
            // user_id comparison is case-INSENSITIVE (both converted to lowercase)
            // password comparison is case-SENSITIVE
            var matchedUser = null;
            for (var i = 0; i < USERS.length; i++) {{
                if (USERS[i].id.toLowerCase() === enteredId && USERS[i].pw === enteredPw) {{
                    matchedUser = USERS[i];
                    break;
                }}
            }}

            if (matchedUser) {{
                // ── Login Successful ──
                // Save user info to sessionStorage so dashboard pages
                // can read it and show the user's name, role etc.
                // sessionStorage is cleared automatically when browser tab is closed.
                sessionStorage.setItem('ongc_logged_in', 'true');
                sessionStorage.setItem('ongc_user_id',   matchedUser.id);
                sessionStorage.setItem('ongc_user_name', matchedUser.name);
                sessionStorage.setItem('ongc_user_role', matchedUser.role);
                sessionStorage.setItem('ongc_user_div',  matchedUser.div);

                // Show brief confirmation then redirect
                document.getElementById('loginBtn').textContent = '✔ Logging in...';
                document.getElementById('loginBtn').classList.add('loading');

                setTimeout(function() {{
                    window.location.href = 'index.html';
                }}, 600);

            }} else {{
                // ── Login Failed ──
                document.getElementById('errorMsg').textContent = '✕  Invalid User ID or Password. Please try again.';
                document.getElementById('errorMsg').classList.add('visible');

                // Shake the card for visual feedback
                var card = document.querySelector('.login-card');
                card.style.animation = 'none';
                card.style.transform = 'translateX(8px)';
                setTimeout(function() {{ card.style.transform = 'translateX(-8px)'; }}, 80);
                setTimeout(function() {{ card.style.transform = 'translateX(4px)'; }}, 160);
                setTimeout(function() {{ card.style.transform = 'translateX(0)'; }}, 240);

                // Clear password field
                document.getElementById('password').value = '';
                document.getElementById('password').focus();
            }}
        }}

        /**
         * togglePassword:
         * Shows or hides the password text.
         */
        function togglePassword() {{
            var pw = document.getElementById('password');
            pw.type = (pw.type === 'password') ? 'text' : 'password';
        }}

        /**
         * handlePasswordKey:
         * Allows pressing Enter in the password field to trigger login.
         */
        function handlePasswordKey(event) {{
            checkCapsLock(event);
            if (event.key === 'Enter') attemptLogin();
        }}

        /**
         * checkCapsLock:
         * Shows a warning if Caps Lock is ON while typing the password.
         */
        function checkCapsLock(event) {{
            var warn = document.getElementById('capsWarn');
            if (event.getModifierState && event.getModifierState('CapsLock')) {{
                warn.classList.add('visible');
            }} else {{
                warn.classList.remove('visible');
            }}
        }}

        // Auto-focus the User ID field on page load
        window.onload = function() {{
            document.getElementById('userId').focus();
        }};
    </script>

</body>
</html>"""

    return html
