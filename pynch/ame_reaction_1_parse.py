import pandas as pd

from ame_reaction_1_file import AMEReactionFile_1


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

        df = {"TableYear": self.year}
        df["A"] = self._read_as_int(line, self.START_R1_A, self.END_R1_A)
        df["Z"] = self._read_as_int(line, self.START_R1_Z, self.END_R1_Z)
        df["N"] = df["A"] - df["Z"]

        df["TwoNeutronDripLine"] = self._read_as_float(line, self.START_S2N, self.END_S2N)
        df["TwoNeutronDripLineError"] = self._read_as_float(line, self.START_DS2N, self.END_DS2N)

        df["TwoProtonDripLine"] = self._read_as_float(line, self.START_S2P, self.END_S2P)
        df["TwoProtonDripLineError"] = self._read_as_float(line, self.START_DS2P, self.END_DS2P)

        df["QAlpha"] = self._read_as_float(line, self.START_QA, self.END_QA)
        df["QAlphaError"] = self._read_as_float(line, self.START_DQA, self.END_DQA)

        df["QTwoBeta"] = self._read_as_float(line, self.START_Q2B, self.END_Q2B)
        df["QTwoBetaError"] = self._read_as_float(line, self.START_DQ2B, self.END_DQ2B)

        df["QEpsilon"] = self._read_as_float(line, self.START_QEP, self.END_QEP)
        df["QEpsilonError"] = self._read_as_float(line, self.START_DQEP, self.END_DQEP)

        df["QBetaNeutron"] = self._read_as_float(line, self.START_QBN, self.END_QBN)
        df["QBetaNeutronError"] = self._read_as_float(line, self.START_DQBN, self.END_DQBN)

        return df

    def read_file(self):
        """
        Read the file
        """
        with open(self.filename, "r") as f:
            lines = [line.rstrip() for line in f]

        lines = lines[self.AME_HEADER:]

        return pd.DataFrame.from_dict([self._read_line(line) for line in lines])
