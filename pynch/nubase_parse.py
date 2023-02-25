"""Extract the data from the nubse file."""
import logging
import pathlib
import re
import typing

import pandas as pd

from pynch.nubase_file import NubaseFile


class NubaseParser(NubaseFile):
    """Parse the NUBASE data file.

    A collection of functions to parse the weird format of the NUBASE file.
    """

    def __init__(self, filename: pathlib.Path, year: int):
        """Set the file to read and the table year."""
        self.filename = filename
        self.year = year
        super().__init__(self.year)
        logging.info(f"Reading {self.filename} from {self.year}")

    def _read_halflife_value(self, line: str) -> typing.Union[float, None]:
        """Slice the string to get the numerical value or None if it's empty."""
        data = line[self.START_HALFLIFEVALUE: self.END_HALFLIFEVALUE].strip()
        number = re.sub(r"[<>?~]", "", data)
        return float(number) if number else None

    def _read_halflife_error(self, line: str) -> typing.Union[float, None]:
        """Slice the string to get the numerical value or None if it's empty."""
        data = line[self.START_HALFLIFEERROR: self.END_HALFLIFEERROR].strip()
        number = re.sub(r"[<>?~a-z]", "", data)
        return float(number) if number else None

    def _read_all_halflife_data(self, line: str) -> tuple:
        """Extract all the data related to the halflife."""
        data = line[self.START_HALFLIFEVALUE: self.END_HALFLIFEVALUE].strip()
        number = re.sub(r"[<>?~]", "", data) if data != "stbl" else "-1.0"

        if number == "-1.0":
            return 99.99, "Zy", 0.0

        return (
            float(number) if number else None,
            self._read_substring(line, self.START_HALFLIFEUNIT, self.END_HALFLIFEUNIT),
            self._read_halflife_error(line)
        )

    def _read_spin(self, line: str) -> typing.Union[str, None]:
        """Extract the spin of the isotope and it's level."""
        # 2020 brought in '*' for directly measured. Just remove it for the moment
        # TODO parse the spin parity with the new characters
        spin = self._read_substring(line, self.START_SPIN, self.END_SPIN)
        if spin and spin.find('*') != -1:
            spin = spin.replace('*', '')

        return spin

    def _read_decay_string(self, line: str) -> str:
        """Extract the decay mode and do some book keeping for consistency."""
        decay_string = (
            self._read_substring(line, self.START_DECAYSTRING_03, len(line))
            if self.year == 2003
            else self._read_substring(line, self.START_DECAYSTRING, len(line))
        )

        if decay_string is None:
            decay_string = "UNKNOWN"
        # Get the first value in the ';' separated list
        # Get the initial part of the first value
        filtered = re.split('=| |~|<|>', decay_string.split(';')[0])[0]

        # Tidy up 'random' strings into standard ones
        if filtered == "e+":
            filtered = "B+"
        elif filtered == "IS":
            filtered = "stable"

        return filtered

    def _read_line(self, line: str) -> dict:
        """Read a line of the file."""
        # Ignore isomers for the moment
        state = self._read_as_int(line, self.START_STATE, self.END_STATE)  
        if state is None or state > 0:
            return dict()

        exp = True if line.find("#") == -1 else False
        if not exp:
            line = line.replace("#", " ")

        data = {
            "Experimental" : exp,
            "TableYear": self.year,
            "A" : self._read_as_int(line, self.START_A, self.END_A),
            "Z" : self._read_as_int(line, self.START_Z, self.END_Z),
            "NubaseMassExcess" : self._read_as_float(line, self.START_ME, self.END_ME),
            "NubaseMassExcessError" : self._read_as_float(line, self.START_DME, self.END_DME),
            # "LevelEnergy" : self._read_as_float(,
            #     line, self.START_ISOMER, self.END_ISOMER
            # )
            # "LevelEnergyError" : self._read_as_float(,
            #     line, self.START_DISOMER, self.END_DISOMER
            # )
            "LevelSpin" : self._read_spin(line),
            "DiscoveryYear" : (
                self._read_as_int(line, self.START_YEAR, self.END_YEAR, default=1900)
                if self.year != 2003
                else 1900
            ),
            "Decay" : self._read_decay_string(line),
        }

        data["HalfLifeValue"], data["HalfLifeUnit"], data["HalfLifeError"] = self._read_all_halflife_data(line)
        data["N"] = data["A"] - data["Z"]
        data["Symbol"] = self.z_to_symbol[data["Z"]]

        return data

    def _readable_line(self, line: str) -> bool:
        """Some lines have 'random' strings, ignore them."""
        return (line.find("p-unst") == -1 and line.find("mix") == -1 and line.find("non-exist") == -1)

    def read_file(self) -> pd.DataFrame:
        """Read the file."""
        with open(self.filename, "r") as f:
            lines = [line.rstrip() for line in f]

        lines = lines[self.HEADER:self.FOOTER]

        the_lines = [
            self._read_line(line) for line in lines if self._readable_line(line)
        ]

        return pd.DataFrame([d for d in the_lines if d])
