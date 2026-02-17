"""Unit tests for rover2d package."""

from __future__ import annotations

import unittest

from rover2d.cli import process_command
from rover2d.rover import Direction, Rover


class RoverModelTests(unittest.TestCase):
    def test_turn_left_and_right(self) -> None:
        rover = Rover()
        rover.turn_left()
        self.assertEqual(rover.facing, Direction.WEST)
        rover.turn_right()
        self.assertEqual(rover.facing, Direction.NORTH)

    def test_move_in_facing_direction(self) -> None:
        rover = Rover()
        rover.move()
        self.assertEqual((rover.x, rover.y, rover.facing), (0, 1, Direction.NORTH))
        rover.turn_right()
        rover.move(2)
        self.assertEqual((rover.x, rover.y, rover.facing), (2, 1, Direction.EAST))

    def test_face_updates_direction(self) -> None:
        rover = Rover()
        rover.face("s")
        self.assertEqual(rover.facing, Direction.SOUTH)


class RoverCliTests(unittest.TestCase):
    def test_process_commands_sequence(self) -> None:
        rover = Rover()
        process_command(rover, "MOVE")
        process_command(rover, "RIGHT")
        process_command(rover, "MOVE 3")
        should_continue, output = process_command(rover, "REPORT")
        self.assertTrue(should_continue)
        self.assertEqual(output, "3 1 E")

    def test_invalid_command(self) -> None:
        rover = Rover()
        should_continue, output = process_command(rover, "JUMP")
        self.assertTrue(should_continue)
        self.assertIn("Unknown command", output or "")


if __name__ == "__main__":
    unittest.main()
