"""Interactive command line interface for rover movement."""

from __future__ import annotations

from rover2d.rover import Direction, Rover

HELP_TEXT = """Available commands:
  LEFT | L                 Turn rover left by 90 degrees
  RIGHT | R                Turn rover right by 90 degrees
  MOVE [n] | M [n]         Move forward by n steps (default: 1)
  FACE <N|E|S|W>           Point rover in an explicit direction
  REPORT                   Show current position and facing
  HELP                     Show this help message
  EXIT | QUIT              Exit the application

Examples:
  MOVE
  RIGHT
  MOVE 3
  FACE W
  REPORT
"""


def process_command(rover: Rover, command: str) -> tuple[bool, str | None]:
    """Process a single command.

    Returns:
      (should_continue, output_message)
    """
    text = command.strip()
    if not text:
        return True, None

    parts = text.split()
    action = parts[0].upper()

    if action in {"LEFT", "L"}:
        rover.turn_left()
        return True, f"Turned left. {rover.report()}"

    if action in {"RIGHT", "R"}:
        rover.turn_right()
        return True, f"Turned right. {rover.report()}"

    if action in {"MOVE", "M"}:
        if len(parts) == 1:
            steps = 1
        elif len(parts) == 2 and parts[1].lstrip("-").isdigit():
            steps = int(parts[1])
        else:
            return True, "Usage: MOVE [steps]"
        try:
            rover.move(steps)
        except ValueError as err:
            return True, str(err)
        return True, f"Moved {steps} step(s). {rover.report()}"

    if action == "FACE":
        if len(parts) != 2:
            return True, "Usage: FACE <N|E|S|W>"
        try:
            rover.face(Direction.from_value(parts[1]))
        except ValueError as err:
            return True, str(err)
        return True, f"Now facing {rover.facing.value}. {rover.report()}"

    if action == "REPORT":
        return True, rover.report()

    if action in {"HELP", "H", "?"}:
        return True, HELP_TEXT

    if action in {"EXIT", "QUIT", "Q"}:
        return False, "Goodbye."

    return True, f"Unknown command '{parts[0]}'. Type HELP for commands."


def main() -> int:
    rover = Rover()
    print("Rover 2D CLI")
    print("Type HELP to see commands. Starting at:", rover.report())

    while True:
        try:
            user_input = input("rover> ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        should_continue, message = process_command(rover, user_input)
        if message:
            print(message)
        if not should_continue:
            break

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
