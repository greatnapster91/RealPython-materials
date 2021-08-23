"""This module provides the RP to-do model-controller."""

from pathlib import Path
from typing import Any, Dict, NamedTuple

from .database import DatabaseHandler


class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int


class Todoer:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path)
