#!/usr/bin/env python3
"""
Dopamine competition entry.
Outputs the competition name to entry.txt in MAKEFUN_OUTPUT_DIR
"""
import os


def get_output_dir() -> str:
    """Get and create the output directory."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def main() -> None:
    output_dir = get_output_dir()
    output_file = os.path.join(output_dir, "entry.txt")
    with open(output_file, "w") as f:
        f.write("Dopamine")
    print(f"Entry written to {output_file}")


if __name__ == "__main__":
    main()
