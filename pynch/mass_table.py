import pathlib

from pynch.nubase_parse import NubaseParser
from pynch.ame_mass_parse import AMEMassParser
from pynch.ame_reaction_1_parse import AMEReactionParser_1
from pynch.ame_reaction_2_parse import AMEReactionParser_2


class MassTable:
    """fjdklsafjsk

    kdfjsdlakfjdklf
    """

    def __init__(self, year: int):
        self.years = [2003, 2012, 2016]
        self.year = year
        self.data_path = pathlib.Path(__file__) / ".." / ".." / "data"
        self._set_datafiles()
        self._parse_datafiles()
        self.merge_ame_data()

    def _set_datafiles(self):
        """
        fsdfa
        """
        if self.year not in self.years:
            print(f"WARNING: {self.year} not a valid table year, using {self.years[-1]}")
            self.year = self.years[-1]

        data_dir = self.data_path / pathlib.Path(str(self.year))
        data_dir = data_dir.resolve()

        if self.year == 2003:
            self.nubase_file = data_dir / "nubtab03.asc"
            self.ame_mass_file = data_dir / "mass.mas03"
            self.ame_reaction_1_file = data_dir / "rct1.mas03"
            self.ame_reaction_2_file = data_dir / "rct2.mas03"
        elif self.year == 2012:
            self.nubase_file = data_dir / "nubtab12.asc"
            self.ame_mass_file = data_dir / "mass.mas12"
            self.ame_reaction_1_file = data_dir / "rct1.mas12"
            self.ame_reaction_2_file = data_dir / "rct2.mas12"
        elif self.year == 2016:
            self.nubase_file = data_dir / "nubase2016.txt"
            self.ame_mass_file = data_dir / "mass16.txt"
            self.ame_reaction_1_file = data_dir / "rct1-16.txt"
            self.ame_reaction_2_file = data_dir / "rct2-16.txt"

    def _parse_datafiles(self):
        """
        fdafs
        """
        self.nubase_df = NubaseParser(self.nubase_file, self.year).read_file()
        self.ame_mass_df = AMEMassParser(self.ame_mass_file, self.year).read_file()
        self.ame_reaction_1_df = AMEReactionParser_1(self.ame_reaction_1_file, self.year).read_file()
        self.ame_reaction_2_df = AMEReactionParser_2(self.ame_reaction_2_file, self.year).read_file()

    def merge_ame_data(self):
        """
        fdsaf
        """
        df = self.ame_mass_df.merge(self.ame_reaction_1_df, on=['A', 'Z', 'N', 'TableYear'])
        self.ame_df = df.merge(self.ame_reaction_2_df, on=['A', 'Z', 'N', 'TableYear'])
