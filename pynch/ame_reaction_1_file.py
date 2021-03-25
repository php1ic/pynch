"""Storage for the variable line positions."""
from pynch.parse import Parse


class AMEReactionFileOne(Parse):
    """Easy access to where the variables are in the first AME reaction file."""

    def __init__(self):
        """Setup the values that locate the variable."""
        super(AMEReactionFileOne, self).__init__()
        self.START_R1_A = 1
        self.END_R1_A = 4
        self.START_R1_Z = 8
        self.END_R1_Z = 11
        self.START_S2N = 14
        self.END_S2N = 22
        self.START_DS2N = 23
        self.END_DS2N = 30
        self.START_S2P = 32
        self.END_S2P = 40
        self.START_DS2P = 41
        self.END_DS2P = 48
        self.START_QA = 50
        self.END_QA = 58
        self.START_DQA = 59
        self.END_DQA = 66
        self.START_Q2B = 67
        self.END_Q2B = 76
        self.START_DQ2B = 77
        self.END_DQ2B = 84
        self.START_QEP = 85
        self.END_QEP = 94
        self.START_DQEP = 95
        self.END_DQEP = 102
        self.START_QBN = 103
        self.END_QBN = 111
        self.START_DQBN = 113
        self.END_DQBN = 125
