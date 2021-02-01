import pandas as pd

from ame_reaction_2_file import AMEReactionFile_2


class AMEReactionParser_2(AMEReactionFile_2):
    """ Parse the second AME reaction file

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
        df["A"] = self._read_as_int(line, self.START_R2_A, self.END_R2_A)
        df["Z"] = self._read_as_int(line, self.START_R2_Z, self.END_R2_Z)
        df["N"] = df["A"] - df["Z"]

        df["OneNeutronDripLine"] = self._read_as_float(line, self.START_SN, self.END_SN)
        df["OneNeutronDripLineError"] = self._read_as_float(line, self.START_DSN, self.END_DSN)

        df["OneProtonDripLine"] = self._read_as_float(line, self.START_SP, self.END_SP)
        df["OneProtonDripLineError"] = self._read_as_float(line, self.START_DSP, self.END_DSP)

        df["QFourBeta"] = self._read_as_float(line, self.START_Q4B, self.END_Q4B)
        df["QFourBetaError"] = self._read_as_float(line, self.START_DQ4B, self.END_DQ4B)

        df["QDeuteronAlpha"] = self._read_as_float(line, self.START_QDA, self.END_QDA)
        df["QDeuteronAlphaError"] = self._read_as_float(line, self.START_DQDA, self.END_DQDA)

        df["QProtonAlpha"] = self._read_as_float(line, self.START_QPA, self.END_QPA)
        df["QProtonAlphaError"] = self._read_as_float(line, self.START_DQPA, self.END_DQPA)

        df["QNeutronAlpha"] = self._read_as_float(line, self.START_QNA, self.END_QNA)
        df["QNeutronAlphaErrror"] = self._read_as_float(line, self.START_DQNA, self.END_DQNA)

        return df

    def read_file(self):
        """
        Read the file
        """
        with open(self.filename, "r") as f:
            lines = [line.rstrip() for line in f]

        lines = lines[self.AME_HEADER:]

        return pd.DataFrame.from_dict([self._read_line(line) for line in lines])
