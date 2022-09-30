"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    # Convert everything to strings
    for i in range(0, len(items)):
        items[i] = str(items[i])


    # Count the frequencies
    frequencies = {}

    for item in items:
        if item not in frequencies.keys():
            frequencies[item] = items.count(item)

    return frequencies
