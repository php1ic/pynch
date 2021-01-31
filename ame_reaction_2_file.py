from parse import Parse


class AMEReactionFile_2(Parse):
    """Easy access to where the variables are in the second AME reaction file

    The second AME reaction file
    """

    def __init__(self):
        super(AMEReactionFile_2, self).__init__()
        self.START_R2_A = 1
        self.END_R2_A = 4
        self.START_R2_Z = 8
        self.END_R2_Z = 11
        self.START_SN = 14
        self.END_SN = 22
        self.START_DSN = 23
        self.END_DSN = 30
        self.START_SP = 32
        self.END_SP = 39
        self.START_DSP = 41
        self.END_DSP = 48
        self.START_Q4B = 49
        self.END_Q4B = 58
        self.START_DQ4B = 59
        self.END_DQ4B = 66
        self.START_QDA = 67
        self.END_QDA = 75
        self.START_DQDA = 77
        self.END_DQDA = 84
        self.START_QPA = 85
        self.END_QPA = 94
        self.START_DQPA = 95
        self.END_DQPA = 102
        self.START_QNA = 103
        self.END_QNA = 111
        self.START_DQNA = 113
        self.END_DQNA = 125
