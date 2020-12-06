import pandas as pd
import pathlib


class MassData:
    """
    """

    def __init__(self):
        self.script_path = pathlib.Path(__file__)
        self.abs_path = self.script_path.resolve()
        self.root_dir = self.abs_path.parent
        self.data_dir = pathlib.Path("data")
        self.years = ["2003", "2012", "2016"]
        self.table_files = [self.masstable(i) for i in self.years]
        self.data = dict(zip(self.years, self.table_files))
        self.dataframes = [self._ingest_datafile(self.data[i], i) for i in self.data]
        self.full_data = pd.concat(self.dataframes, ignore_index=True)
        self._do_indexing()

    def masstable(self, year: int = 2003) -> pathlib.Path:
        return self.root_dir / self.data_dir / f"masstable{year}.json"

    def _ingest_datafile(self, tablefile, year: int, verbosity: int = 1) -> pd.DataFrame:
        if verbosity > 0:
            print(f"Converting <{tablefile}> into a pandas dataframe")

        df = pd.read_json(tablefile)
        df["TableYear"] = year
        df["NubaseRelativeError"] = abs(
            df["ErrorNubaseMassExcess"] / df["NubaseMassExcess"]
        )
        df["AMERelativeError"] = abs(df["ErrorAMEMassExcess"] / df["AMEMassExcess"])

        # 12C has a 0.0 +/ 0.0 mass excess by definition so calculating relative error -> NaN
        # Set the value to 0.0 as that's what it is
        df.loc[(df.Symbol == "C") & (df.A == 12), "NubaseRelativeError"] = 0.0
        df.loc[(df.Symbol == "C") & (df.A == 12), "AMERelativeError"] = 0.0

        return df

    def _do_indexing(self) -> pd.DataFrame:
        self.full_data.set_index("TableYear", inplace=True)
