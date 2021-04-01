"""Storage for the variable line positions."""
from pynch.parse import Parse


class NubaseFile(Parse):
    """Easy access to where variables are in the NUBASE file.

    The NUBASE data file is formatted by location in the line, values exist
    between 2 specific columns in the line. Store the start and end locations
    in this class to allow simple access and stop the NUBASE parser having
    magic numbers.
    """

    def __init__(self, year: int):
        """Setup the values that locate the variable."""
        super(NubaseFile, self).__init__()
        if year < 2020:
            self.START_A = 0
            self.END_A = 3
            self.START_Z = 4
            self.END_Z = 7
            self.START_STATE = 7
            self.END_STATE = 8
            self.START_ME = 18
            self.END_ME = 29
            self.START_DME = 29
            self.END_DME = 38
            self.START_ISOMER = 39
            self.END_ISOMER = 46
            self.START_DISOMER = 48
            self.END_DISOMER = 56
            self.START_HALFLIFEVALUE = 60
            self.END_HALFLIFEVALUE = 68
            self.START_HALFLIFEUNIT = 69
            self.END_HALFLIFEUNIT = 71
            self.START_HALFLIFEERROR = 72
            self.END_HALFLIFEERROR = 77
            self.START_SPIN = 79
            self.END_SPIN = 93
            # After the 2003 table the discovery
            # year was added alterting the positions
            self.START_YEAR = 105
            self.END_YEAR = 109
            # Let the 03 position be the odd-one-out and thus
            # have the slightly awkward name
            self.START_DECAYSTRING_03 = 106
            self.START_DECAYSTRING = 110
            # The decay string goes to EOL put here commented
            # to show that we haven't just forgotten about it.
            # END_DECAYSTRING = EOL;
        else:
            self.START_A = 0
            self.END_A = 3
            self.START_Z = 4
            self.END_Z = 7
            self.START_STATE = 7
            self.END_STATE = 8
            self.START_ME = 18
            self.END_ME = 30
            self.START_DME = 31
            self.END_DME = 41
            self.START_ISOMER = 42
            self.END_ISOMER = 53
            self.START_DISOMER = 54
            self.END_DISOMER = 64
            self.START_HALFLIFEVALUE = 69
            self.END_HALFLIFEVALUE = 77
            self.START_HALFLIFEUNIT = 78
            self.END_HALFLIFEUNIT = 80
            self.START_HALFLIFEERROR = 81
            self.END_HALFLIFEERROR = 87
            self.START_SPIN = 88
            self.END_SPIN = 101
            self.START_ENSDF = 102
            self.END_ENSDF = 103
            self.START_YEAR = 114
            self.END_YEAR = 118
            # Let the 03 position be the odd-one-out and thus
            # have the slightly awkward name
            self.START_DECAYSTRING = 119
            # The decay string goes to EOL put here commented
            # to show that we haven't just forgotten about it.
            # self.END_DECAYSTRING = EOL;
