"""Extract the date from the second reaction file."""
import logging
import pathlib

import pandas as pd

from pynch.ame_reaction_2_file import AMEReactionFileTwo


class AMEReactionParserTwo(AMEReactionFileTwo):
    """Parse the second AME reaction file.

    The format is known but I don't think python can easily parse it.
    """

    def __init__(self, filename: pathlib.Path, year: int):
        """Set the file to read and table year."""
        self.filename = filename
        self.year = year
        super().__init__(self.year)
        logging.info(f"Reading {self.filename} from {self.year}")

    def _read_line(self, line: str) -> dict:
        """Read a line from the file."""
        # Don't use a '#' as an experimental marker in this file
        # but still need to remove it
        if line.find("#") != -1:
            line = line.replace("#", " ")

        data = {
            "TableYear": self.year,
            "A": self._read_as_int(line, self.START_R2_A, self.END_R2_A),
            "Z": self._read_as_int(line, self.START_R2_Z, self.END_R2_Z),
            "OneNeutronSeparationEnergy": self._read_as_float(line, self.START_SN, self.END_SN),
            "OneNeutronSeparationEnergyError": self._read_as_float(line, self.START_DSN, self.END_DSN),
            "OneProtonSeparationEnergy": self._read_as_float(line, self.START_SP, self.END_SP),
            "OneProtonSeparationEnergyError": self._read_as_float(line, self.START_DSP, self.END_DSP),
            "QFourBeta": self._read_as_float(line, self.START_Q4B, self.END_Q4B),
            "QFourBetaError": self._read_as_float(line, self.START_DQ4B, self.END_DQ4B),
            "QDeuteronAlpha": self._read_as_float(line, self.START_QDA, self.END_QDA),
            "QDeuteronAlphaError": self._read_as_float(line, self.START_DQDA, self.END_DQDA),
            "QProtonAlpha": self._read_as_float(line, self.START_QPA, self.END_QPA),
            "QProtonAlphaError": self._read_as_float(line, self.START_DQPA, self.END_DQPA),
            "QNeutronAlpha": self._read_as_float(line, self.START_QNA, self.END_QNA),
            "QNeutronAlphaError": self._read_as_float(line, self.START_DQNA, self.END_DQNA),
        }

        data["N"] = data["A"] - data["Z"]
        data["Symbol"] = self.z_to_symbol[data["Z"]]

        return data

    def read_file(self) -> pd.DataFrame:
        """Read the file."""
        with open(self.filename, "r") as f:
            lines = [line.rstrip() for line in f]

        # Remove the header lines and the footer for the 2020 table
        lines = lines[self.HEADER: self.FOOTER]

        # The 2020 rct2 file has additional lines feeds not present in any other file
        the_lines = [line for line in lines if line[:1] != "1"]

        return pd.DataFrame([self._read_line(line) for line in the_lines])
