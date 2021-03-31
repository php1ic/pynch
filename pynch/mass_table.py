"""Functionality to parse all data file into a single object."""
import logging
import pathlib
import typing

import pandas as pd

from pynch.ame_mass_parse import AMEMassParser
from pynch.ame_reaction_1_parse import AMEReactionParserOne
from pynch.ame_reaction_2_parse import AMEReactionParserTwo
from pynch.nubase_parse import NubaseParser


class MassTable:
    """Storage class for all of the mass data.

    Internally there are separate dataframes for the NUBASE and AME data as well as a combined one for all data
    """

    def __init__(self):
        """Do all of the work at construction."""
        # Assume this file is some/path/pynch/pynch/mass_table.py
        self.data_path = pathlib.Path(__file__) / ".." / ".." / "data"
        self.existing_years = [2003, 2012, 2016, 2020]
        self.nubase = pd.concat([self._parse_nubase_data(y) for y in self.existing_years], ignore_index=True)
        self.ame = pd.concat([self._parse_ame_data(y) for y in self.existing_years], ignore_index=True)
        self.full_data = self._combine_all_data()
        self._do_indexing()

    def _get_nubase_datafile(self, year: int) -> str:
        """Use the given year to locate the nubase mass table file and return the absolute path."""
        nubase_mass = self.data_path / pathlib.Path(str(year))
        nubase_mass = nubase_mass.resolve()

        if year == 2003:
            nubase_mass = nubase_mass / "nubtab03.asc"
        elif year == 2012:
            nubase_mass = nubase_mass / "nubtab12.asc"
        elif year == 2016:
            nubase_mass = nubase_mass / "nubase2016.txt"
        elif year == 2020:
            nubase_mass = nubase_mass / "nubase_1.mas20"

        return nubase_mass

    def _get_ame_datafiles(self, year: int) -> typing.Tuple[str, str, str]:
        """Use the given year to locate the 3 AME data file and return the absolute path."""
        data_dir = self.data_path / pathlib.Path(str(year))
        data_dir = data_dir.resolve()

        if year == 2003:
            ame_mass = data_dir / "mass.mas03"
            ame_reaction_1 = data_dir / "rct1.mas03"
            ame_reaction_2 = data_dir / "rct2.mas03"
        elif year == 2012:
            ame_mass = data_dir / "mass.mas12"
            ame_reaction_1 = data_dir / "rct1.mas12"
            ame_reaction_2 = data_dir / "rct2.mas12"
        elif year == 2016:
            ame_mass = data_dir / "mass16.txt"
            ame_reaction_1 = data_dir / "rct1-16.txt"
            ame_reaction_2 = data_dir / "rct2-16.txt"
        elif year == 2020:
            ame_mass = data_dir / "mass.mas20"
            ame_reaction_1 = data_dir / "rct1.mas20"
            ame_reaction_2 = data_dir / "rct2.mas20"

        return ame_mass, ame_reaction_1, ame_reaction_2

    def _validate_year(self, year: int) -> None:
        """Point the appropriate variables at the required data files for the table year."""
        if year not in self.existing_years:
            logging.warning(f"{year} not a valid table year, using {self.existing_years[-1]}")
            year = self.existing_years[-1]

        return year

    def _parse_nubase_data(self, year: int) -> pd.DataFrame:
        """Get the nubase for the given year as a pandas.DataFrame."""
        year = self._validate_year(year)
        return NubaseParser(self._get_nubase_datafile(year), year).read_file()

    def _parse_ame_data(self, year: int) -> pd.DataFrame:
        """Combine all the AME files from the given year into a pandas.DataFrame."""
        year = self._validate_year(year)
        ame_mass, ame_reaction_1, ame_reaction_2 = self._get_ame_datafiles(year)

        ame_mass_df = AMEMassParser(ame_mass, year).read_file()

        # Merge all 3 of the AME files/data frames into one
        common_columns = ['A', 'Z', 'N', 'TableYear', 'Symbol']
        temp_df = ame_mass_df.merge(AMEReactionParserOne(ame_reaction_1, year).read_file(), on=common_columns)
        return temp_df.merge(AMEReactionParserTwo(ame_reaction_2, year).read_file(), on=common_columns)

    def _combine_all_data(self) -> pd.DataFrame:
        """Combine all NUBASE and AME data into a single pandas DataFrame."""
        common_columns = ['A', 'Z', 'N', 'TableYear', 'Symbol']
        df = self.nubase.merge(self.ame, on=common_columns)

        df["NubaseRelativeError"] = abs(
            df["NubaseMassExcessError"] / df["NubaseMassExcess"]
        )
        df["AMERelativeError"] = abs(df["AMEMassExcessError"] / df["AMEMassExcess"])

        # 12C has a 0.0 +/ 0.0 mass excess by definition so calculating relative error -> NaN
        # Set the value to 0.0 as that's what it is
        df.loc[(df.Symbol == "C") & (df.A == 12), "NubaseRelativeError"] = 0.0
        df.loc[(df.Symbol == "C") & (df.A == 12), "AMERelativeError"] = 0.0

        return df

    def _do_indexing(self) -> None:
        """
        Set the index of the dataframe to the table year. This is done in place so nothing is returned.

        param: Nothing

        :return: Nothing
        """
        self.nubase.set_index("TableYear", inplace=True)
        self.ame.set_index("TableYear", inplace=True)
        self.full_data.set_index("TableYear", inplace=True)
