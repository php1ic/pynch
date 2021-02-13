import pandas as pd

from pynch.ame_reaction_1_file import AMEReactionFile_1


class AMEReactionParser_1(AMEReactionFile_1):
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
        # Don't use a '#' as an experimental marker in this file
        # but still need to remove it
        if line.find("#") != -1:
            line = line.replace("#", " ")

        data = {"TableYear": self.year}
        data["A"] = self._read_as_int(line, self.START_R1_A, self.END_R1_A)
        data["Z"] = self._read_as_int(line, self.START_R1_Z, self.END_R1_Z)
        data["N"] = data["A"] - data["Z"]

        data["TwoNeutronDripLine"] = self._read_as_float(line, self.START_S2N, self.END_S2N)
        data["TwoNeutronDripLineError"] = self._read_as_float(line, self.START_DS2N, self.END_DS2N)

        data["TwoProtonDripLine"] = self._read_as_float(line, self.START_S2P, self.END_S2P)
        data["TwoProtonDripLineError"] = self._read_as_float(line, self.START_DS2P, self.END_DS2P)

        data["QAlpha"] = self._read_as_float(line, self.START_QA, self.END_QA)
        data["QAlphaError"] = self._read_as_float(line, self.START_DQA, self.END_DQA)

        data["QTwoBeta"] = self._read_as_float(line, self.START_Q2B, self.END_Q2B)
        data["QTwoBetaError"] = self._read_as_float(line, self.START_DQ2B, self.END_DQ2B)

        data["QEpsilon"] = self._read_as_float(line, self.START_QEP, self.END_QEP)
        data["QEpsilonError"] = self._read_as_float(line, self.START_DQEP, self.END_DQEP)

        data["QBetaNeutron"] = self._read_as_float(line, self.START_QBN, self.END_QBN)
        data["QBetaNeutronError"] = self._read_as_float(line, self.START_DQBN, self.END_DQBN)

        return data

    def read_file(self):
        """
        Read the file
        """
        with open(self.filename, "r") as f:
            lines = [line.rstrip() for line in f]

        lines = lines[self.AME_HEADER:]

        return pd.DataFrame.from_dict([self._read_line(line) for line in lines])
