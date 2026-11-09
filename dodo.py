"""Initial project tasks; empirical replication tasks will be added during development."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from settings import config, create_directories

DOIT_CONFIG = {
    "backend": "sqlite3",
    "dep_file": ".doit-db.sqlite",
    "default_tasks": ["config", "tests"],
}


def task_config():
    """Create local data and output directories without downloading data."""
    return {"actions": [create_directories], "clean": []}


def task_tests():
    """Run the inherited helper tests without credentials or external data."""
    return {
        "actions": [[sys.executable, "-m", "pytest", "-q", "src/test_misc_tools.py"]],
        "verbosity": 2,
        "clean": [],
    }


def task_site():
    """Build project documentation with ChartBook; no empirical results are registered yet."""
    return {
        "actions": ["chartbook docs build"],
        "file_dep": ["README.md", "chartbook.toml", *map(str, Path("docs_src").rglob("*.md"))],
        "targets": ["docs/index.html"],
        "clean": [],
    }
