#class of rotor settings sets up the wiring and notches for each rotor
class Rotor:
    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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

    #rotate function rotates the rotor by 1 position
    def rotate(self, n=1):
        for i in range(n):
            self.left = self.left[1:] + self.left[0]
            self.right = self.right[1:] + self.right[0]
