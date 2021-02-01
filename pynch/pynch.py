import ame_mass_parse
import ame_reaction_1_parse
import ame_reaction_2_parse
import datetime
import nubase_parse
import pathlib

import mass_table

if __name__ == '__main__':
    # datafile = pathlib.Path(__file__) / ".." / ".." / "data" / "2003" / "nubtab03.asc"
    # datafile = datafile.resolve()
    # data = nubase_parse.NubaseParser(datafile, 2003)
    # print(datetime.datetime.now())
    # df = data.read_file()
    # print(datetime.datetime.now())
    # print(df)
    # print(df[df['Level'] == 1])

    # ame_file = pathlib.Path(__file__) / ".." / ".." / "data" / "2003" / "mass.mas03"
    # ame_file = ame_file.resolve()

    # ame = ame_mass_parse.AMEMassParser(ame_file, 2003)
    # ame_df = ame.read_file()
    # print(ame_df)

    # ame_reaction_1 = pathlib.Path(__file__) / ".." / ".." / "data" / "2003" / "rct1.mas03"
    # ame_reaction_1 = ame_reaction_1.resolve()

    # ame_r1 = ame_reaction_1_parse.AMEReactionParser_1(ame_reaction_1, 2003)
    # ame_r1_df = ame_r1.read_file()
    # print(ame_r1_df)

    # ame_reaction_2 = pathlib.Path(__file__) / ".." / ".." / "data" / "2003" / "rct2.mas03"
    # ame_reaction_2 = ame_reaction_2.resolve()

    # ame_r2 = ame_reaction_2_parse.AMEReactionParser_2(ame_reaction_2, 2003)
    # ame_r2_df = ame_r2.read_file()
    # print(ame_r2_df)

    # all_ame = ame_df.merge(ame_r1_df, on=['A', 'Z', 'N', 'TableYear'])
    # all_ame = all_ame.merge(ame_r2_df, on=['A', 'Z', 'N', 'TableYear'])
    # print(all_ame)

    # full = df.merge(ame_df, on=['A', 'Z', 'N', 'TableYear', 'Level'], how='outer')
    # full = ame_df.merge(ame_r1_df, on=['A', 'Z', 'N', 'TableYear'])
    # full = full.merge(ame_r2_df, on=['A', 'Z', 'N', 'TableYear'])
    # full = full.merge(df, on=['A', 'Z', 'N', 'TableYear', 'Level'], how='outer')

    # print(df)

    table03 = mass_table.MassTable(2016)
    # table12 = mass_table.MassTable(2012)
    # table16 = mass_table.MassTable(2016)

    nubase = table03.nubase_df
    ame = table03.ame_df

    print(nubase.dtypes)
    print(ame.dtypes)
