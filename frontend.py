def render_dashboard(username: str) -> str:
    """Render the main dashboard for a user."""
    return f"<h1>Welcome, {username}</h1>"


def render_login_form() -> str:
    """Render the login form."""
    return """
    <form>
        <input name="username">
        <input name="password" type="password">
        <button>Login</button>
    </form>
    """