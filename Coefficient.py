# Coefficient of Form
class Coefficient:
    def __init__(self, L, B, T, V):
        self.L = L
        self.B = B
        self.T = T
        self.V = V

    # Block Coefficient
    def Cb(self):
        self.V / self.L * self.B * self.T

    # Midship Section Coefficient
    def Cm(self, Am):
        Am / self.B * self.T

    # Waterplane Coefficient
    def Cw(self, Aw):
        Aw / self.L * self.B

    # Prismatic Coefficient
    def Cp(self, Am):
        self.V / self.L * Am

    # Vertical Prismatic Coefficient
    def Cvp(self, Vw, Aw):
        Vw / Aw * self.T
