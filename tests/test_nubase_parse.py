# from pynch.nubase_parse import NubaseParser
# import pynch as py
import pynch.nubase_parse as nbp


def test_read_halflife():
    parser = nbp.NubaseParser(".", 2003)

    line_01 = "232 0950   232Am   43400#     300#                             1.31   m 0.04                 91           B+=?;A=2#;B+SF=0.069 10"

    assert parser._read_halflife(line_01) == 1.31

    line_02 = "052 0290   52Cu    -2630#     260#                                             3+#           00           p ?"
    assert parser._read_halflife(line_02) == None


def test_read_halflife_error():
    parser = nbp.NubaseParser(".", 2003)

    line_01 = "113 0500   113Sn  -88333        4                            115.09   d 0.03   1/2+          00           B+=100"
    assert parser._read_halflife_error(line_01) == 0.03

    line_02 = "025 0150   25P     18870#     200#                           <30     ns        1/2+#         00 93Po.Ai   p ?"
    assert parser._read_halflife_error(line_02) == None
