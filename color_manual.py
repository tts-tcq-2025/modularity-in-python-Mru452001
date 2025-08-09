from color_utils import get_color_from_pair_number
from color_constants import MAJOR_COLORS, MINOR_COLORS

def print_reference_manual():
    """Prints the color coding reference manual."""
    print("Pair No.   Major   Minor")
    print("------------------------")
    pair_number = 1
    for major in MAJOR_COLORS:
        for minor in MINOR_COLORS:
            print(f"{pair_number:<9} {major:<6} {minor}")
            pair_number += 1
