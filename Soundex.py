def get_soundex_code(c):
    """Returns the Soundex code for a single character."""
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c.upper(), '0')  # Default to '0' for non-mapped characters

def get_first_letter(name):
    """Returns the first letter of the name in uppercase."""
    return name[0].upper() if name else ""

def filter_and_map_soundex(name):
    """Returns a list of Soundex codes for the characters in the name, skipping repeated codes."""
    codes = []
    prev_code = ''
    for char in name:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            codes.append(code)
            prev_code = code
    return codes

def pad_soundex(soundex):
    """Pads the Soundex code with zeros to ensure it is 4 characters long."""
    return soundex.ljust(4, '0')

def generate_soundex(name):
    """Generates the Soundex code for a given name."""
    if not name:
        return ""

    first_letter = get_first_letter(name)
    soundex_body = ''.join(filter_and_map_soundex(name[1:]))[:3]  # Take only the first 3 mapped codes
    soundex = first_letter + soundex_body

    return pad_soundex(soundex)

