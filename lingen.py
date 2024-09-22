import random
from pylatex import Document, Section, Command, NewPage
from pylatex.utils import NoEscape
import os

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

def generate_latex_pdf(sequence, filename="drum_score.pdf", font="lmodern", letter_spacing=0.2):
    """
    Generates a PDF for the drum sequence using pylatex with custom font and spacing.

    Args:
        sequence (str): The sequence of drum patterns as a string (output from `generate_drum_sequence`).
        filename (str): The name of the PDF file to save (default is "drum_score.pdf").
        font (str): LaTeX font to use (default is "lmodern").
        letter_spacing (float): Additional space between letters in em units (default is 0.2).

    Returns:
        None
    """
    # Create a LaTeX document
    doc = Document()
    
    # Add custom font and packages for formatting
    doc.preamble.append(Command('usepackage', 'lmodern'))  # Use Latin Modern font
    doc.preamble.append(Command('usepackage', 'microtype'))  # Improve typesetting
    doc.preamble.append(Command('usepackage', 'setspace'))  # For spacing adjustments

    # Set the custom letter spacing (microtype's `\textls` command)
    doc.preamble.append(NoEscape(f"\\newcommand{{\\customspacing}}[1]{{\\textls[{int(letter_spacing * 100)}]{{#1}}}}"))
    doc.append(NoEscape('\\begin{center}'))
    doc.append(NoEscape('\\large'))
    
    # Add the sequence with custom spacing
    for char in sequence:
        if char == " ":
            # Add a regular space
            doc.append(" ")
        elif char == "|":
            # Add measure separator with space
            doc.append(" | ")
        else:
            # Add each letter with custom spacing
            doc.append(NoEscape(f"\\customspacing{{{char}}}"))

    doc.append(NoEscape('\\end{center}'))

    # Generate the PDF
    doc.generate_pdf(filename.split(".pdf")[0], clean_tex=False)

# Example usage
patterns = ["RLLK", "RLK", "KLR", "RRLL"]
sequence = generate_drum_sequence(patterns, 8, over_the_bar=True)  # Generate 8 measures
generate_latex_pdf(sequence, "drum_score.pdf", font="lmodern", letter_spacing=0.3)