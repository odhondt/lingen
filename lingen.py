import random
from fpdf import FPDF

def generate_drum_sequence(patterns, num_measures, over_the_bar=False):
    """
    Generates a random sequence of patterns, cuts it to the required number of notes,
    and formats it into measures of 4/4 with groups of 4 16th notes and '|' every 16 notes.

    Args:
        patterns (list): List of drum sticking patterns (e.g., ["RLLK", "RLK"]).
        num_measures (int): Number of 4/4 measures to generate.
        over_the_bar (bool): If True, the patterns will continue across measures. If False,
                             patterns will be cut exactly to fit each measure.

    Returns:
        str: A string representing the sequence of drum patterns, grouped in 4s and measures of 16.
    """
    total_notes = num_measures * 16  # Total number of 16th notes to fill
    sequence = []

    # Generate a long sequence of patterns
    while len("".join(sequence)) < total_notes:
        pattern = random.choice(patterns)
        sequence.append(pattern)
    
    # Join the sequence and trim it to the required length
    full_sequence = "".join(sequence)[:total_notes]

    # Split into groups of 4 notes
    grouped_sequence = [full_sequence[i:i+4] for i in range(0, len(full_sequence), 4)]
    
    # Join groups with spaces and add '|' every 4 groups (i.e., every 16 notes)
    formatted_sequence = " | ".join([" ".join(grouped_sequence[i:i+4]) for i in range(0, len(grouped_sequence), 4)])
    
    return formatted_sequence

def generate_drum_pdf(sequence, filename="drum_score.pdf"):
    """
    Creates a PDF with the given drum sequence in the same format as the string.

    Args:
        sequence (str): The sequence of drum patterns as a string (output from `generate_drum_sequence`).
        filename (str): The name of the PDF file to save (default is "drum_score.pdf").

    Returns:
        None
    """
    pdf = FPDF()
    pdf.add_page()

    # Set font for drum sequence
    pdf.set_font('Arial', '', 12)

    # Write the full sequence in one line without separating measures by lines
    pdf.multi_cell(0, 10, sequence)

    pdf.output(filename)




