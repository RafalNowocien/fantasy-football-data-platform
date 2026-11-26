
import sqlite3

from src.fantasy_football.config import DATABASE_PATH, SCHEMA_FILE


def initialize_database():
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        connection.execute("PRAGMA foreign_keys = ON")

        schema = SCHEMA_FILE.read_text(encoding="utf-8")

        connection.executescript(schema)

        connection.commit()

    finally:
        connection.close()
