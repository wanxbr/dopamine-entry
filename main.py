#!/usr/bin/env python3
"""
Dopamine competition entry.
Outputs the competition name to entry.txt in MAKEFUN_OUTPUT_DIR
"""
import os

# Use MAKEFUN_OUTPUT_DIR environment variable for output
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
os.makedirs(output_dir, exist_ok=True)

# Write entry name to output file
output_file = os.path.join(output_dir, "entry.txt")
with open(output_file, "w") as f:
    f.write("Dopamine")

print(f"Entry written to {output_file}")
