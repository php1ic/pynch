"""Extract the data from the AME mass file."""
import pandas as pd

from pynch.ame_mass_file import AMEMassFile


class AMEMassParser(AMEMassFile):
    """Parse the AME mass file.

    The format is known but I don't think python can easily parse it.
    """

    def __init__(self, filename: str, year: int):
        """Set the file to read and table year."""
        super().__init__()
        self.filename = filename
        self.year = year
        print(f"Reading {self.filename} from {self.year}")

    def _read_line(self, line: str) -> dict:
        """Read a line from the file."""
        if line.find("#") != -1:
            line = line.replace("#", " ")

        data = {"TableYear": self.year}
        data["A"] = self._read_as_int(line, self.START_A, self.END_A)
        data["Z"] = self._read_as_int(line, self.START_Z, self.END_Z)
        data["N"] = data["A"] - data["Z"]
        data["Symbol"] = self.z_to_symbol[data["Z"]]

        data["AMEMassExcess"] = self._read_as_float(line, self.START_ME, self.END_ME)
        data["AMEMassExcessError"] = self._read_as_float(line, self.START_DME, self.END_DME)

        data["BindingEnergyPerA"] = self._read_as_float(line, self.START_BE_PER_A, self.END_BE_PER_A)
        data["BindingEnergyPerAError"] = self._read_as_float(line, self.START_DBE_PER_A, self.END_DBE_PER_A)

        data["BetaDecayEnergy"] = self._read_as_float(line, self.START_BETA_DECAY_ENERGY, self.END_BETA_DECAY_ENERGY)
        data["BetaDecayEnergyError"] = self._read_as_float(line, self.START_DBETA_DECAY_ENERGY, self.END_DBETA_DECAY_ENERGY)

        data["AtomicMass"] = self._read_as_float(line, self.START_MICRO_U, self.END_MICRO_U)
        data["AtomicMassError"] = self._read_as_float(line, self.START_MICRO_DU, self.END_MICRO_DU)

        return data

    def read_file(self) -> pd.DataFrame:
        """Read the file."""
        with open(self.filename, "r") as f:
            lines = [line.rstrip() for line in f]

        # Remove the header lines
        lines = lines[self.AME_HEADER:]

        return pd.DataFrame.from_dict([self._read_line(line) for line in lines])
