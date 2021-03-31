from pynch.ame_reaction_2_parse import AMEReactionParserTwo


def test_read_line():
    parser = AMEReactionParserTwo(".", 2003)

    line = " 204 Tl  81    6656.10    0.29   6365.82    1.25 -12470.66   24.01  13710.69    1.15   8181.34    1.16   7701.54    3.34"

    d = parser._read_line(line)

    assert d['A'] == 204
    assert d['Z'] == 81
    assert d['N'] == 123
    assert d['OneNeutronSeparationEnergy'] == 6656.10
    assert d['OneNeutronSeparationEnergyError'] == 0.29
    assert d['OneProtonSeparationEnergy'] == 6365.82
    assert d['OneProtonSeparationEnergyError'] == 1.25
    assert d['QFourBeta'] == -12470.66
    assert d['QFourBetaError'] == 24.01
    assert d['QDeuteronAlpha'] == 13710.69
    assert d['QDeuteronAlphaError'] == 1.15
    assert d['QProtonAlpha'] == 8181.34
    assert d['QProtonAlphaError'] == 1.16
    assert d['QNeutronAlpha'] == 7701.54
    assert d['QNeutronAlphaErrror'] == 3.34

    parser = AMEReactionParserTwo(".", 2020)

    line = " 204 Tl  81    6656.0787    0.2907   6365.8379    1.2542 -12470.8182   22.6974  13710.0469    1.0612   8180.5147    1.0721   7701.0380    3.3084"

    d = parser._read_line(line)

    assert d['A'] == 204
    assert d['Z'] == 81
    assert d['N'] == 123
    assert d['OneNeutronSeparationEnergy'] == 6656.0787
    assert d['OneNeutronSeparationEnergyError'] == 0.2907
    assert d['OneProtonSeparationEnergy'] == 6365.8379
    assert d['OneProtonSeparationEnergyError'] == 1.2542
    assert d['QFourBeta'] == -12470.8182
    assert d['QFourBetaError'] == 22.6974
    assert d['QDeuteronAlpha'] == 13710.0469
    assert d['QDeuteronAlphaError'] == 1.0612
    assert d['QProtonAlpha'] == 8180.5147
    assert d['QProtonAlphaError'] == 1.0721
    assert d['QNeutronAlpha'] == 7701.0380
    assert d['QNeutronAlphaErrror'] == 3.3084
