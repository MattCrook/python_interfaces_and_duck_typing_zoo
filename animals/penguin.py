from movements import IWalking, ISwimming


class Penguin(IWalking, ISwimming):
    def __init__(self, name):
        ISwimming.__init__(self)
        IWalking.__init__(self)
        self.name = name

    def __str__(self):
        return f"{self.name} the Penguin"

    def run(self):
        print(f"{self.legs} waddles.")
