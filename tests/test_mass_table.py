from pynch.mass_table import MassTable


def test_set_datafiles():
    # Default
    default = MassTable(2000)
    data_path = default.data_path / str(default.years[-1])
    nubase = data_path / "nubase2016.txt"
    ame = data_path / "mass16.txt"
    ame_r1 = data_path / "rct1-16.txt"
    ame_r2 = data_path / "rct2-16.txt"

    assert default.nubase_file == nubase.resolve()
    assert default.ame_mass_file == ame.resolve()
    assert default.ame_reaction_1_file == ame_r1.resolve()
    assert default.ame_reaction_2_file == ame_r2.resolve()

    # 2003
    the_year = 2003
    mt = MassTable(the_year)
    data_path = mt.data_path / str(the_year)
    nubase = data_path / "nubtab03.asc"
    ame = data_path / "mass.mas03"
    ame_r1 = data_path / "rct1.mas03"
    ame_r2 = data_path / "rct2.mas03"

    assert mt.nubase_file == nubase.resolve()
    assert mt.ame_mass_file == ame.resolve()
    assert mt.ame_reaction_1_file == ame_r1.resolve()
    assert mt.ame_reaction_2_file == ame_r2.resolve()

    # 2012
    the_year = 2012
    mt = MassTable(the_year)
    data_path = mt.data_path / str(the_year)
    nubase = data_path / "nubtab12.asc"
    ame = data_path / "mass.mas12"
    ame_r1 = data_path / "rct1.mas12"
    ame_r2 = data_path / "rct2.mas12"

    assert mt.nubase_file == nubase.resolve()
    assert mt.ame_mass_file == ame.resolve()
    assert mt.ame_reaction_1_file == ame_r1.resolve()
    assert mt.ame_reaction_2_file == ame_r2.resolve()

    # 2016
    the_year = 2016
    mt = MassTable(the_year)
    data_path = mt.data_path / str(the_year)
    nubase = data_path / "nubase2016.txt"
    ame = data_path / "mass16.txt"
    ame_r1 = data_path / "rct1-16.txt"
    ame_r2 = data_path / "rct2-16.txt"

    assert mt.nubase_file == nubase.resolve()
    assert mt.ame_mass_file == ame.resolve()
    assert mt.ame_reaction_1_file == ame_r1.resolve()
    assert mt.ame_reaction_2_file == ame_r2.resolve()
