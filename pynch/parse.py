"""Base class with common parsing functionality."""
import typing


class Parse:
    """Common functions for parsing data.

    We read multiple files so put the functions used when parsing
    all of them into this module that we can inherit from.
    """

    def __init__(self):
        """Construct the symbol to Z map.

        The _read functions could be taken out of the class, but then they wouldn't be inherited by the file parsers,
        so lets leave them as members for the moment.
        """
        super(Parse, self).__init__()
        self.z_to_symbol = {
            0: "n", 1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O", 9: "F",
            10: "Ne", 11: "Na", 12: "Mg", 13: "Al", 14: "Si", 15: "P", 16: "S", 17: "Cl", 18: "Ar", 19: "K",
            20: "Ca", 21: "Sc", 22: "Ti", 23: "V", 24: "Cr", 25: "Mn", 26: "Fe", 27: "Co", 28: "Ni", 29: "Cu",
            30: "Zn", 31: "Ga", 32: "Ge", 33: "As", 34: "Se", 35: "Br", 36: "Kr", 37: "Rb", 38: "Sr", 39: "Y",
            40: "Zr", 41: "Nb", 42: "Mo", 43: "Tc", 44: "Ru", 45: "Rh", 46: "Pd", 47: "Ag", 48: "Cd", 49: "In",
            50: "Sn", 51: "Sb", 52: "Te", 53: "I", 54: "Xe", 55: "Cs", 56: "Ba", 57: "La", 58: "Ce", 59: "Pr",
            60: "Nd", 61: "Pm", 62: "Sm", 63: "Eu", 64: "Gd", 65: "Tb", 66: "Dy", 67: "Ho", 68: "Er", 69: "Tm",
            70: "Yb", 71: "Lu", 72: "Hf", 73: "Ta", 74: "W", 75: "Re", 76: "Os", 77: "Ir", 78: "Pt", 79: "Au",
            80: "Hg", 81: "Tl", 82: "Pb", 83: "Bi", 84: "Po", 85: "At", 86: "Rn", 87: "Fr", 88: "Ra", 89: "Ac",
            90: "Th", 91: "Pa", 92: "U", 93: "Np", 94: "Pu", 95: "Am", 96: "Cm", 97: "Bk", 98: "Cf", 99: "Es",
            100: "Fm", 101: "Md", 102: "No", 103: "Lr", 104: "Rf", 105: "Db", 106: "Sg", 107: "Bh", 108: "Hs", 109: "Mt",
            110: "Ds", 111: "Rg", 112: "Cn", 113: "Ed", 114: "Fl", 115: "Ef", 116: "Lv", 117: "Ts", 118: "Og"
        }

    def _read_as_int(self, line: str, start: int, end: int, default: int = None) -> typing.Union[int, None]:
        """Slice the string and return as an int, or None if the slice is empty."""
        data = line[start:end].strip()
        return int(data) if data else default

    def _read_as_float(self, line: str, start: int, end: int, default: float = None) -> typing.Union[float, None]:
        """Slice the string and return as a float, or None if the slice is empty or just a '*' character."""
        data = line[start:end].strip()
        return float(data) if data and data != "*" else default

    def _read_substring(self, line: str, start: int, end: int, default: str = None) -> typing.Union[str, None]:
        """Slice the string or return None if the slice is empty."""
        data = line[start:end].strip()
        return data if data else default
