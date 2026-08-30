def connect_database(host: str, port: int):
    """Create a connection to the PostgreSQL database."""
    connection = {
        "host": host,
        "port": port,
        "database": "codecompass",
    }

    return connection


def close_database(connection):
    """Close the database connection."""
    connection.clear()