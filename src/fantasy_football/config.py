from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"

# Data files
PLAYER_DATA_FILE = DATA_DIR / "player_data.csv"
PERFORMANCE_DATA_FILE = DATA_DIR / "performance_data.csv"
LEAGUE_DATA_FILE = DATA_DIR / "league_data.csv"
TEAM_DATA_FILE = DATA_DIR / "team_data.csv"
TEAM_PLAYER_DATA_FILE = DATA_DIR / "team_player_data.csv"

# Database configuration
DATABASE_PATH = BASE_DIR / "fantasy_data.db"
SCHEMA_FILE = BASE_DIR / "sql" / "schema.sql"
