"""Storage for the variable line positions."""
from pynch.parse import Parse


class AMEReactionFileTwo(Parse):
    """Easy access to where the variables are in the second AME reaction file."""

    def __init__(self, year: int):
        """Setup the values that locate the variables."""
        super(AMEReactionFileTwo, self).__init__()
        if year < 2020:
            self.START_R2_A = 1
            self.END_R2_A = 4
            self.START_R2_Z = 8
            self.END_R2_Z = 11
            self.START_SN = 14
            self.END_SN = 22
            self.START_DSN = 23
            self.END_DSN = 30
            self.START_SP = 32
            self.END_SP = 40
            self.START_DSP = 41
            self.END_DSP = 48
            self.START_Q4B = 49
            self.END_Q4B = 58
            self.START_DQ4B = 59
            self.END_DQ4B = 66
            self.START_QDA = 67
            self.END_QDA = 76
            self.START_DQDA = 77
            self.END_DQDA = 84
            self.START_QPA = 85
            self.END_QPA = 94
            self.START_DQPA = 95
            self.END_DQPA = 102
            self.START_QNA = 103
            self.END_QNA = 112
            self.START_DQNA = 113
            self.END_DQNA = 125
        else:
            self.START_R2_A = 1
            self.END_R2_A = 4
            self.START_R2_Z = 8
            self.END_R2_Z = 11
            self.START_SN = 14
            self.END_SN = 24
            self.START_DSN = 25
            self.END_DSN = 34
            self.START_SP = 36
            self.END_SP = 46
            self.START_DSP = 47
            self.END_DSP = 56
            self.START_Q4B = 57
            self.END_Q4B = 68
            self.START_DQ4B = 69
            self.END_DQ4B = 78
            self.START_QDA = 79
            self.END_QDA = 90
            self.START_DQDA = 91
            self.END_DQDA = 100
            self.START_QPA = 101
            self.END_QPA = 112
            self.START_DQPA = 113
            self.END_DQPA = 122
            self.START_QNA = 123
            self.END_QNA = 134
            self.START_DQNA = 135
            self.END_DQNA = 144
