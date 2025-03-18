#class of reflector settings sets up the wiring and notch
class Reflector:
    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring

    #reflect function takes a signal and returns the corresponding signal
    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal


