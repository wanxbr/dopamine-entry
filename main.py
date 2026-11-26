#!/usr/bin/env python3
"""
Dopamine competition entry.
Outputs the competition name to /output/entry.txt
"""
import os

# Create output directory if it doesn't exist
output_dir = "/output"
os.makedirs(output_dir, exist_ok=True)

# Write entry name to output file
output_file = os.path.join(output_dir, "entry.txt")
with open(output_file, "w") as f:
    f.write("Dopamine")

print(f"Entry written to {output_file}")
