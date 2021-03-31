from pynch.ame_mass_parse import AMEMassParser


def test_read_line():
    parser = AMEMassParser(".", 2003)

    line = "  15   41   26   67 Fe    x  -45692.348    415.570     8449.695    6.203 B-   9368.702  523.438  66 950947.244    446.132"
    d = parser._read_line(line)

    assert d['A'] == 67
    assert d['Z'] == 26
    assert d['N'] == 41
    assert d['AMEMassExcess'] == -45692.348
    assert d['AMEMassExcessError'] == 415.570
    assert d['BindingEnergyPerA'] == 8449.695
    assert d['BindingEnergyPerAError'] == 6.203
    assert d['BetaDecayEnergy'] == 9368.702
    assert d['BetaDecayEnergyError'] == 523.438
    assert d['AtomicMass'] == 950947.244
    assert d['AtomicMassError'] == 446.132

    parser = AMEMassParser(".", 2020)

    line = "  15   41   26   67 Fe    x  -45708.416       3.819      8449.9359     0.0570  B-   9613.3678     7.4900   66 950930.000       4.100"
    d = parser._read_line(line)

    assert d['A'] == 67
    assert d['Z'] == 26
    assert d['N'] == 41
    assert d['AMEMassExcess'] == -45708.416
    assert d['AMEMassExcessError'] == 3.819
    assert d['BindingEnergyPerA'] == 8449.9359
    assert d['BindingEnergyPerAError'] == 0.0570
    assert d['BetaDecayEnergy'] == 9613.3678
    assert d['BetaDecayEnergyError'] == 7.4900
    assert d['AtomicMass'] == 950930.00
    assert d['AtomicMassError'] == 4.100
