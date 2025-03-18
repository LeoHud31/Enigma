#class of rotor settings sets up the wiring and notches for each rotor
class Rotor:
    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch

    #forward function takes a signal and returns the corresponding signal
    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal   
    
    #backward function takes a signal and returns the corresponding signal
    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
