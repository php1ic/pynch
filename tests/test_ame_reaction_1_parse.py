from pynch.ame_reaction_1_parse import AMEReactionParserOne


def test_read_line():
    parser = AMEReactionParserOne(".", 2003)

    line = " 186 Ir  77   15704.74   32.47   9524.26   17.08   3849.65  103.31  -7458.10   26.70  -2639.77   16.57 -10561.10   44.19"

    d = parser._read_line(line)

    assert d['A'] == 186
    assert d['Z'] == 77
    assert d['N'] == 109
    assert d['TwoNeutronSeparationEnergy'] == 15704.74
    assert d['TwoNeutronSeparationEnergyError'] == 32.47
    assert d['TwoProtonSeparationEnergy'] == 9524.26
    assert d['TwoProtonSeparationEnergyError'] == 17.08
    assert d['QAlpha'] == 3849.65
    assert d['QAlphaError'] == 103.31
    assert d['QTwoBeta'] == -7458.10
    assert d['QTwoBetaError'] == 26.70
    assert d['QEpsilon'] == -2639.77
    assert d['QEpsilonError'] == 16.57
    assert d['QBetaNeutron'] == -10561.10
    assert d['QBetaNeutronError'] == 44.19

    parser = AMEReactionParserOne(".", 2020)

    line = " 186 Ir  77   15704.1312   32.4655   9530.4731   17.0698   3848.8777  103.3133  -7457.4943   26.6968  -2642.2739   16.5459 -10555.5245   30.6658"

    d = parser._read_line(line)

    assert d['A'] == 186
    assert d['Z'] == 77
    assert d['N'] == 109
    assert d['TwoNeutronSeparationEnergy'] == 15704.1312
    assert d['TwoNeutronSeparationEnergyError'] == 32.4655
    assert d['TwoProtonSeparationEnergy'] == 9530.4731
    assert d['TwoProtonSeparationEnergyError'] == 17.0698
    assert d['QAlpha'] == 3848.8777
    assert d['QAlphaError'] == 103.3133
    assert d['QTwoBeta'] == -7457.4943
    assert d['QTwoBetaError'] == 26.6968
    assert d['QEpsilon'] == -2642.2739
    assert d['QEpsilonError'] == 16.5459
    assert d['QBetaNeutron'] == -10555.5245
    assert d['QBetaNeutronError'] == 30.6658
