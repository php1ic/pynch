from pynch.ame_reaction_1_parse import AMEReactionParser_1


def test_read_line():
    parser = AMEReactionParser_1(".", 2003)

    line = " 186 Ir  77   15704.74   32.47   9524.26   17.08   3849.65  103.31  -7458.10   26.70  -2639.77   16.57 -10561.10   44.19"

    d = parser._read_line(line)

    assert d['A'] == 186
    assert d['Z'] == 77
    assert d['N'] == 109
    assert d['TwoNeutronDripLine'] == 15704.74
    assert d['TwoNeutronDripLineError'] == 32.47
    assert d['TwoProtonDripLine'] == 9524.26
    assert d['TwoProtonDripLineError'] == 17.08
    assert d['QAlpha'] == 3849.65
    assert d['QAlphaError'] == 103.31
    assert d['QTwoBeta'] == -7458.10
    assert d['QTwoBetaError'] == 26.70
    assert d['QEpsilon'] == -2639.77
    assert d['QEpsilonError'] == 16.57
    assert d['QBetaNeutron'] == -10561.10
    assert d['QBetaNeutronError'] == 44.19
