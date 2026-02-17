# rover2d

Command line rover simulation on a 2D plane.

## Features

- Tracks rover coordinates on an `(x, y)` grid.
- Tracks facing direction (`N`, `E`, `S`, `W`).
- Supports turning left/right and moving forward in current direction.
- Interactive CLI prompt for issuing commands.

## Install

```bash
pip install -e .
```

## Run

```bash
rover2d
```

Or:

```bash
python -m rover2d
```

## Commands

- `LEFT` or `L` - turn 90 degrees left
- `RIGHT` or `R` - turn 90 degrees right
- `MOVE [n]` or `M [n]` - move forward `n` steps (default `1`)
- `FACE <N|E|S|W>` - point the rover in a specific direction
- `REPORT` - print `x y direction`
- `HELP` - show command help
- `EXIT` or `QUIT` - leave the app

## Example Session

```text
Rover 2D CLI
Type HELP to see commands. Starting at: 0 0 N
rover> MOVE
Moved 1 step(s). 0 1 N
rover> RIGHT
Turned right. 0 1 E
rover> MOVE 2
Moved 2 step(s). 2 1 E
rover> REPORT
2 1 E
```
