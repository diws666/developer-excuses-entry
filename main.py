#!/usr/bin/env python3
"""Writes one single-line production excuse to /output/entry.txt."""

# The entry line: exactly 95 characters.
EXCUSE = "I did not break production. Production was already broken; I merely introduced it to the users."

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(EXCUSE)
