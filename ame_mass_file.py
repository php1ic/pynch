from parse import Parse


class AMEMassFile(Parse):
    """Easy access to where the variables are in the AME mass file

    The AME mass file
    """

    def __init__(self):
        super(AMEMassFile, self).__init__()
        self.START_A = 16
        self.END_A = 19
        self.START_Z = 11
        self.END_Z = 14
        self.START_ME = 29
        self.END_ME = 41
        self.START_DME = 42
        self.END_DME = 53
        self.START_BE_PER_A = 54
        self.END_BE_PER_A = 64
        self.START_DBE_PER_A = 65
        self.END_DBE_PER_A = 72
        self.START_BETA_DECAY_ENERGY = 76
        self.END_BETA_DECAY_ENERGY = 86
        self.START_DBETA_DECAY_ENERGY = 87
        self.END_DBETA_DECAY_ENERGY = 95
        self.START_MICRO_U = 100
        self.END_MICRO_U = 112
        self.START_MICRO_DU = 113
        self.END_MICRO_DU = 125
