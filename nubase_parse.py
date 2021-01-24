import datetime
import pandas as pd
import re


class NubaseFile:
    """Easy access to where variables are in the NUBASE file

    The NUBASE data file is formatted by location in the line, values exist
    between 2 specific columns in the line. Store the start and end locations
    in this class to allow simple access and stop the NUBASE parser having
    magic numbers.
    """

    def __init__(self):
        self.START_A = 0
        self.END_A = 3
        self.START_Z = 4
        self.END_Z = 7
        self.START_STATE = 7
        self.END_STATE = 8
        self.START_ME = 18
        self.END_ME = 29
        self.START_DME = 29
        self.END_DME = 38
        self.START_ISOMER = 39
        self.END_ISOMER = 46
        self.START_DISOMER = 48
        self.END_DISOMER = 56
        self.START_HALFLIFEVALUE = 60
        self.END_HALFLIFEVALUE = 69
        self.START_HALFLIFEUNIT = 69
        self.END_HALFLIFEUNIT = 71
        self.START_HALFLIFEERROR = 72
        self.END_HALFLIFEERROR = 77
        self.START_SPIN = 79
        self.END_SPIN = 93
        # After the 2003 table the discovery
        # year was added alterting the positions
        self.START_YEAR = 105
        self.END_YEAR = 109
        # Let the 03 position be the odd-one-out and thus
        # have the slightly awkward name
        self.START_DECAYSTRING_03 = 106
        self.START_DECAYSTRING = 110
        # The decay string goes to EOL put here commented
        # to show that we haven't just forgotten about it.
        # END_DECAYSTRING = EOL;


class NubaseParser:
    """Parse the NUBASE data file

    fkldsjfldskfj
    """

    def __init__(self, filename: str, year: int):
        self.filename = filename
        self.year = year
        print(f"Reading {self.filename} from {self.year}")

    def _read_as_int(self, line: str, start: int, end: int) -> int:
        """
        Wrapper to return the slice if a string as an int
        """
        data = line[start:end].strip()
        return int(data) if data else None

    def _read_as_float(self, line: str, start: int, end: int) -> float:
        """
        Wrapper to return the slice if a string as an int
        """
        data = line[start:end].strip()
        return float(data) if data else None

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
        nubase = NubaseFile()

        exp = True if line.find("#") == -1 else False

        df = pd.DataFrame([exp], columns=["Experimental"])
        if not exp:
            line = line.replace("#", " ")

        df['TableYear'] = self.year
        df["A"] = self._read_as_int(line, nubase.START_A, nubase.END_A)
        df["Z"] = self._read_as_int(line, nubase.START_Z, nubase.END_Z)
        df["N"] = df["A"] - df["Z"]
        df["Level"] = self._read_as_int(line, nubase.START_STATE, nubase.END_STATE)
        df["NubaseMassExcess"] = self._read_as_float(
            line, nubase.START_ME, nubase.END_ME
        )
        df["NubaseMassExcess_error"] = self._read_as_float(
            line, nubase.START_DME, nubase.END_DME
        )
        df["LevelEnergy"] = self._read_as_float(
            line, nubase.START_ISOMER, nubase.END_ISOMER
        )
        df["LevelEnergy_error"] = self._read_as_float(
            line, nubase.START_DISOMER, nubase.END_DISOMER
        )
        df["HalfLife_value"] = self._read_halflife(
            line, nubase.START_HALFLIFEVALUE, nubase.END_HALFLIFEVALUE
        )
        df["HalfLife_unit"] = line[
            nubase.START_HALFLIFEUNIT : nubase.END_HALFLIFEUNIT
        ].strip()
        df["HalfLife_error"] = self._read_halflife_error(
            line, nubase.START_HALFLIFEERROR, nubase.END_HALFLIFEERROR
        )
        df["LevelSpin"] = line[nubase.START_SPIN : nubase.END_SPIN].strip()
        df["DiscoveryYear"] = (
            self._read_as_int(line, nubase.START_YEAR, nubase.END_YEAR)
            if self.year != 2003
            else 1900
        )
        df["Decay"] = (
            line[nubase.START_DECAYSTRING_03 :].strip()
            if self.year == 2003
            else line[nubase.START_DECAYSTRING :].strip()
        )

        # print(df)
        return df

    def _readable_line(self, line: str) -> bool:
        """
        Some lines have 'random' strings, ignore them
        """
        return (
            line.find("stbl") != -1
            or line.find("p-unst") != -1
            or line.find("mix") != -1
            or line.find("non-exist") != -1
        )

    def read_file(self):
        """
        Read the file
        """
        with open(self.filename, "r") as f:
            lines = [line.rstrip() for line in f]

        print(f"{datetime.datetime.now()} Read all the lines")

        return pd.concat(
            [self._read_line(line) for line in lines if not self._readable_line(line)], ignore_index=True
        )
