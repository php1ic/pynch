from pynch.ame_reaction_2_parse import AMEReactionParser_2


def test_read_line():
    parser = AMEReactionParser_2(".", 2003)

    line = " 204 Tl  81    6656.10    0.29   6365.82    1.25 -12470.66   24.01  13710.69    1.15   8181.34    1.16   7701.54    3.34"

    d = parser._read_line(line)

    assert d['A'] == 204
    assert d['Z'] == 81
    assert d['N'] == 123
    assert d['OneNeutronDripLine'] == 6656.10
    assert d['OneNeutronDripLineError'] == 0.29
    assert d['OneProtonDripLine'] == 6365.82
    assert d['OneProtonDripLineError'] == 1.25
    assert d['QFourBeta'] == -12470.66
    assert d['QFourBetaError'] == 24.01
    assert d['QDeuteronAlpha'] == 13710.69
    assert d['QDeuteronAlphaError'] == 1.15
    assert d['QProtonAlpha'] == 8181.34
    assert d['QProtonAlphaError'] == 1.16
    assert d['QNeutronAlpha'] == 7701.54
    assert d['QNeutronAlphaErrror'] == 3.34
