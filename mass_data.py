import pandas as pd
import pathlib


class MassData:
    """
    Storage class for all of the mass data
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

    def _is_valid_year(self, year: int) -> bool:
        """
        Make sure the given <year> is one in which a mass table exists

        param: The year to check

        :return: True if the year is valid
        :return: False if the year is no valid
        """
        return year in self.years

    def masstable(self, year: int = 2003) -> pathlib.Path:
        """
        Construct the absolute path to the data file for <year>

        param: The year of the data file

        :return: The absoulte path to the data file if the year is valid
        :return: Empty path if the year requested does not have data
        """
        return (
            self.root_dir / self.data_dir / f"masstable_{year}.json"
            if self._is_valid_year(year)
            else pathlib.Path("")
        )

    def _ingest_datafile(
        self, tablefile, year: int, verbosity: int = 1
    ) -> pd.DataFrame:
        """
        Read the <tablefile> into a pandas dataframe and add columns using
        calculations on existing data and <year>

        param: The file to read
        param: The year of the table file

        :return: A pandas dataframe with the files data
        """
        if verbosity > 0:
            print(f"Converting <{tablefile}> into a pandas dataframe")

        if not self._is_valid_year(year):
            if verbosity > 0:
                print(f"No data for {year} returning empty dataframe")
            return pd.DataFrame()

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
        """
        Set the index of the dataframe to the table year

        param: Nothing

        :return: Nothing
        """
        self.full_data.set_index("TableYear", inplace=True)
