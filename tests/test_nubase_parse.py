# from pynch.nubase_parse import NubaseParser
# import pynch as py
import pynch.nubase_parse as nbp


def test_read_halflife_value():
    parser = nbp.NubaseParser(".", 2003)

    line_01 = "232 0950   232Am   43400#     300#                             1.31   m 0.04                 91           B+=?;A=2#;B+SF=0.069 10"

    assert parser._read_halflife_value(line_01) == 1.31

    line_02 = "052 0290   52Cu    -2630#     260#                                             3+#           00           p ?"
    assert parser._read_halflife_value(line_02) == None


def test_read_halflife_error():
    parser = nbp.NubaseParser(".", 2003)

    line_01 = "113 0500   113Sn  -88333        4                            115.09   d 0.03   1/2+          00           B+=100"
    assert parser._read_halflife_error(line_01) == 0.03

    line_02 = "025 0150   25P     18870#     200#                           <30     ns        1/2+#         00 93Po.Ai   p ?"
    assert parser._read_halflife_error(line_02) == None


def test_readable_line():
    parser = nbp.NubaseParser(".", 2003)

    bad_line01 = "003 0030   3Li     28670#    2000#                      RN   p-unst                          98           p ?"
    bad_line02 = "130 0556   130Csx -86873       17        27      15         R=.2~~~.1          fsmix"
    bad_line03 = "267 1081   267Hsm                      non-exist        EU   200     ms                         95Ho.Atdi A=?;IT ?"

    good_line = "072 0360   72Kr   -53941        8                             17.16   s 0.18   0+            95 03Pi03t   B+=100"

    assert not parser._readable_line(bad_line01)
    assert not parser._readable_line(bad_line02)
    assert not parser._readable_line(bad_line03)

    assert parser._readable_line(good_line)


def test_read_line():
    parser = nbp.NubaseParser(".", 2003)

    iso_line = "183 0791   183Aum -30114       10        73.3     0.4         >1     us        (1/2)+        99           IT=100"
    assert parser._read_line(iso_line) == dict()

    gs_line = "057 0290   57Cu   -47310       16                            196.3   ms 0.7    3/2-          98           B+=100"
    d = parser._read_line(gs_line)

    assert d['A'] == 57
    assert d['Z'] == 29
    assert d['N'] == 28
    assert d['Experimental'] is True
    assert d['NubaseMassExcess'] == -47310.0
    assert d['NubaseMassExcessError'] == 16.0
    assert d['HalfLifeValue'] == 196.3
    assert d['HalfLifeUnit'] == "ms"
    assert d['HalfLifeError'] == 0.7
    assert d['LevelSpin'] == "3/2-"
    assert d['DiscoveryYear'] == 1900
    assert d['Decay'] == "B+"

    theoretical_gs_line = "110 0530   110I   -60320#     310#                           650     ms 20     1+#           00           B+=83 4;A=17 4;B+p=11 3;B+A=1.1 3"
    d = parser._read_line(theoretical_gs_line)

    assert d['A'] == 110
    assert d['Z'] == 53
    assert d['N'] == 57
    assert d['Experimental'] is False
    assert d['NubaseMassExcess'] == -60320
    assert d['NubaseMassExcessError'] == 310
    assert d['HalfLifeValue'] == 650
    assert d['HalfLifeUnit'] == "ms"
    assert d['HalfLifeError'] == 20
    assert d['LevelSpin'] == "1+"
    assert d['DiscoveryYear'] == 1900
    assert d['Decay'] == "B+"
