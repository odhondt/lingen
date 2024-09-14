import random


def generate_drum_sequence(patterns, num_measures, ternary=False):
    """
    Generates a random sequence of patterns, cuts it to the required number of notes,
    and formats it into measures of 4/4 with groups of 4 16th notes and '|' every 16 notes.

    Args:
        patterns (list): List of drum sticking patterns (e.g., ["RLLK", "RLK"]).
        num_measures (int): Number of 4/4 measures to generate.
        ternary (bool): If set to True, generate sextuplets instead of 16th notes.

    Returns:
        str: A string representing the sequence of drum patterns, grouped in 4s and measures of 16.
    """

    if not ternary:
        npm = 16
        gr = 4
    else:
        npm = 24
        gr = 6

    total_notes = num_measures * npm  # Total number of 16th notes to fill
    sequence = []

    # Generate a long sequence of patterns
    while len("".join(sequence)) < total_notes:
        pattern = random.choice(patterns)
        sequence.append(pattern)

    # Join the sequence and trim it to the required length
    full_sequence = "".join(sequence)[:total_notes]

    # Split into groups of 4 notes
    grouped_sequence = [full_sequence[i:i+gr]
                        for i in range(0, len(full_sequence), gr)]

    # Join groups with spaces and add '|' every 4 groups (i.e., every 16 notes)
    formatted_sequence = " | ".join(
        [" ".join(grouped_sequence[i:i+gr]) for i in range(0, len(grouped_sequence), gr)])

    return formatted_sequence
