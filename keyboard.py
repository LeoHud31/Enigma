class Keyboard:
    def forward(self, letter):
        signal = "ABCDEFGHIJLMNOPQRSTUVWXYZ".find(letter)
        return signal
    
    def backward(self, signal):
        letter = "ABCDEFGHIJLMNOPQRSTUVWXYZ"[signal]
        return letter