import difflib

def compare_texts(text1, text2):
    """
    Compares two texts and returns differences with line and word numbers.
    """
    diff = difflib.ndiff(text1.splitlines(), text2.splitlines())  # Compare line by line
    differences = []

    for i, line in enumerate(diff):
        if line.startswith("+ ") or line.startswith("- "):  # Detect changed lines
            words = line[2:].split()  # Get words from the line
            word_diffs = [(j + 1, word) for j, word in enumerate(words)]  # Track word numbers
            differences.append((i + 1, line[0], word_diffs))  # Store (line number, type, words)
    
    return differences
