import random

def generate_drum_sequence(patterns, num_measures):
    """
    Generates a random sequence of 4/4 measures using given sticking patterns.
    
    Args:
        patterns (list): List of drum sticking patterns (e.g., ["RLLK", "RLK"]).
        num_measures (int): Number of 4/4 measures to generate.
    
    Returns:
        str: A string representing the sequence of drum patterns in measures.
    """
    sequence = []
    
    for _ in range(num_measures):
        measure = []
        remaining_notes = 16  # 4/4 measure in 16th notes
        
        while remaining_notes > 0:
            pattern = random.choice(patterns)
            # Cut the pattern to fit within the remaining space in the measure
            pattern_to_add = pattern[:remaining_notes]
            measure.append(pattern_to_add)
            remaining_notes -= len(pattern_to_add)
        
        sequence.append(" ".join(measure))
    
    return " | ".join(sequence)
