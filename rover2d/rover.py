"""Core rover movement model."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Direction(str, Enum):
    """Cardinal rover directions."""

    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"

    @classmethod
    def from_value(cls, value: str) -> "Direction":
        """Parse compact or full-word direction values."""
        normalized = value.strip().upper()
        aliases = {
            "N": cls.NORTH,
            "NORTH": cls.NORTH,
            "E": cls.EAST,
            "EAST": cls.EAST,
            "S": cls.SOUTH,
            "SOUTH": cls.SOUTH,
            "W": cls.WEST,
            "WEST": cls.WEST,
        }
        if normalized not in aliases:
            valid = ", ".join(["N", "E", "S", "W"])
            raise ValueError(f"Invalid direction '{value}'. Use one of: {valid}.")
        return aliases[normalized]

    def turn_left(self) -> "Direction":
        """Return the direction 90 degrees counter-clockwise."""
        order = [self.NORTH, self.WEST, self.SOUTH, self.EAST]
        return order[(order.index(self) + 1) % len(order)]

    def turn_right(self) -> "Direction":
        """Return the direction 90 degrees clockwise."""
        order = [self.NORTH, self.EAST, self.SOUTH, self.WEST]
        return order[(order.index(self) + 1) % len(order)]

    @property
    def vector(self) -> tuple[int, int]:
        """Return movement delta for one forward step."""
        vectors = {
            self.NORTH: (0, 1),
            self.EAST: (1, 0),
            self.SOUTH: (0, -1),
            self.WEST: (-1, 0),
        }
        return vectors[self]


@dataclass
class Rover:
    """A rover that can rotate and move on a 2D plane."""

    x: int = 0
    y: int = 0
    facing: Direction = Direction.NORTH

    def turn_left(self) -> None:
        self.facing = self.facing.turn_left()

    def turn_right(self) -> None:
        self.facing = self.facing.turn_right()

    def face(self, direction: Direction | str) -> None:
        self.facing = Direction.from_value(direction) if isinstance(direction, str) else direction

    def move(self, steps: int = 1) -> None:
        if steps < 0:
            raise ValueError("Steps must be a non-negative integer.")
        dx, dy = self.facing.vector
        self.x += dx * steps
        self.y += dy * steps

    def report(self) -> str:
        return f"{self.x} {self.y} {self.facing.value}"
