import datetime
import pandas as pd
import re

from nubase_file import NubaseFile


class NubaseParser(NubaseFile):
    """Parse the NUBASE data file

    A collection of functions to parse the weird format of the NUBASE file.
    """

    def __init__(self, filename: str, year: int):
        super().__init__()
        self.filename = filename
        self.year = year
        print(f"Reading {self.filename} from {self.year}")

    def _read_halflife(self, line: str, start: int, end: int) -> float:
        """"""
        data = line[start:end].strip()
        number = re.sub(r"[<>?~]", "", data)
        return float(number) if number else None

    def _read_halflife_error(self, line: str, start: int, end: int) -> float:
        """"""
        data = line[start:end].strip()
        number = re.sub(r"[<>?~a-z]", "", data)
        return float(number) if number else None

    def _read_line(self, line: str):
        """
        Read a line of the file
        """
        exp = True if line.find("#") == -1 else False

        df = {"Experimental": exp}
        if not exp:
            line = line.replace("#", " ")

        df["TableYear"] = self.year
        df["A"] = self._read_as_int(line, self.START_A, self.END_A)
        df["Z"] = self._read_as_int(line, self.START_Z, self.END_Z)
        df["N"] = df["A"] - df["Z"]
        df["Level"] = self._read_as_int(line, self.START_STATE, self.END_STATE)
        df["NubaseMassExcess"] = self._read_as_float(
            line, self.START_ME, self.END_ME
        )
        df["NubaseMassExcess_error"] = self._read_as_float(
            line, self.START_DME, self.END_DME
        )
        df["LevelEnergy"] = self._read_as_float(
            line, self.START_ISOMER, self.END_ISOMER
        )
        df["LevelEnergy_error"] = self._read_as_float(
            line, self.START_DISOMER, self.END_DISOMER
        )
        df["HalfLife_value"] = self._read_halflife(
            line, self.START_HALFLIFEVALUE, self.END_HALFLIFEVALUE
        )
        df["HalfLife_unit"] = self._read_substring(line, self.START_HALFLIFEUNIT, self.END_HALFLIFEUNIT)
        df["HalfLife_error"] = self._read_halflife_error(
            line, self.START_HALFLIFEERROR, self.END_HALFLIFEERROR
        )
        df["LevelSpin"] = self._read_substring(line, self.START_SPIN, self.END_SPIN)
        df["DiscoveryYear"] = (
            self._read_as_int(line, self.START_YEAR, self.END_YEAR)
            if self.year != 2003
            else 1900
        )
        df["Decay"] = (
            self._read_substring(line, self.START_DECAYSTRING_03, len(line))
            if self.year == 2003
            else self._read_substring(line, self.START_DECAYSTRING, len(line))
        )

        return df

    def _readable_line(self, line: str) -> bool:
        """
        Some lines have 'random' strings, ignore them
        """
        return (
            line.find("stbl") == -1
            and line.find("p-unst") == -1
            and line.find("mix") == -1
            and line.find("non-exist") == -1
        )

    def read_file(self):
        """
        Read the file
        """
        with open(self.filename, "r") as f:
            lines = [line.rstrip() for line in f]

        print(f"{datetime.datetime.now()} Read all the lines")

        return pd.DataFrame.from_dict(
            [self._read_line(line) for line in lines if self._readable_line(line)]
        )
