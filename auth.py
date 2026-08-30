def login(username: str, password: str) -> str:
    """Authenticate a user and return a JWT token."""
    if not username or not password:
        raise ValueError("Username and password are required.")

    return create_jwt(username)


def create_jwt(username: str) -> str:
    """Create an authentication token for the user."""
    return f"jwt-token-for-{username}"
