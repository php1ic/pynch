import datetime
import pandas as pd

from ame_mass_file import AMEMassFile


class AMEMassParser(AMEMassFile):
    """ Parse the first AME reaction file

    fjkdslfjskal
    """

    def __init__(self, filename: str, year: int):
        super().__init__()
        self.filename = filename
        self.year = year
        print(f"Reading {self.filename} from {self.year}")

    def _read_line(self, line: str):
        """
        Read a line from the file
        """
        # exp = True if line.find("#") == -1 else False

        # df = {"Experimental": exp}
        if line.find("#") != -1:
            line = line.replace("#", " ")

        df = {"TableYear": self.year}
        df["Level"] = 0
        df["A"] = self._read_as_int(line, self.START_A, self.END_A)
        df["Z"] = self._read_as_int(line, self.START_Z, self.END_Z)
        df["N"] = df["A"] - df["Z"]

        df["AMEMassExcess"] = self._read_as_float(line, self.START_ME, self.END_ME)
        df["AMEMassExcessError"] = self._read_as_float(line, self.START_DME, self.END_DME)

        df["BindingEnergyPerA"] = self._read_as_float(line, self.START_BE_PER_A, self.END_BE_PER_A)
        df["BindingEnergyPerAError"] = self._read_as_float(line, self.START_DBE_PER_A, self.END_DBE_PER_A)

        df["BetaDecayEnergy"] = self._read_as_float(line, self.START_BETA_DECAY_ENERGY, self.END_BETA_DECAY_ENERGY)
        df["BetaDecayEnergyError"] = self._read_as_float(line, self.START_DBETA_DECAY_ENERGY, self.END_DBETA_DECAY_ENERGY)

        df["AtomicMass"] = self._read_as_float(line, self.START_MICRO_U, self.END_MICRO_U)
        df["AtomicMassError"] = self._read_as_float(line, self.START_MICRO_DU, self.END_MICRO_DU)

        return df

    def read_file(self):
        """
        Read the file
        """
        with open(self.filename, "r") as f:
            lines = [line.rstrip() for line in f]

        lines = lines[self.AME_HEADER:]
        print(f"{datetime.datetime.now()} Read all the lines")

        return pd.DataFrame.from_dict([self._read_line(line) for line in lines])
