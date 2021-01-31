class Parse():
    """Common functions for parsing data

    We read multiple files so put the functions used when parsing
    all of them into this module that we can inherit from.
    """

    def __init__(self):
        super(Parse, self).__init__()
        self.AME_HEADER = 39

    def _read_as_int(self, line: str, start: int, end: int) -> int:
        """
        Wrapper to return the slice if a string as an int
        """
        data = line[start:end].strip()
        return int(data) if data else None

    def _read_as_float(self, line: str, start: int, end: int) -> float:
        """
        Wrapper to return the slice if a string as an float
        """
        data = line[start:end].strip()
        return float(data) if data and data != "*" else None

    def _read_substring(self, line: str, start: int, end: int) -> str:
        """
        Wrapper to return the slice if a string
        """
        data = line[start:end].strip()
        return data if data else None
