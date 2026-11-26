
import csv
import sqlite3
from pathlib import Path

from src.fantasy_football.config import (
    DATABASE_PATH,
    PLAYER_DATA_FILE,
    PERFORMANCE_DATA_FILE,
    LEAGUE_DATA_FILE,
    TEAM_DATA_FILE,
    TEAM_PLAYER_DATA_FILE,
)

def import_csv(
    connection: sqlite3.Connection,
    csv_path: Path,
    table_name: str,
):
    with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames

        placeholders = ", ".join("?" for _ in columns)
        column_names = ", ".join(columns)

        query = (
            f"INSERT INTO {table_name} ({column_names}) "
            f"VALUES ({placeholders})"
        )

        rows = (tuple(row[column] for column in columns) for row in reader)

        connection.executemany(query, rows)


def ingest_data():
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        connection.execute("PRAGMA foreign_keys = ON")

        import_csv(connection, LEAGUE_DATA_FILE, "league")
        import_csv(connection, PLAYER_DATA_FILE, "player")
        import_csv(connection, TEAM_DATA_FILE, "team")
        import_csv(connection, TEAM_PLAYER_DATA_FILE, "team_player")
        import_csv(connection, PERFORMANCE_DATA_FILE, "performance")

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
