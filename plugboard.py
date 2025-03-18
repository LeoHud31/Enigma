#plugboard class
#plugboard class is used to create a plugboard object that can be used to encode and decode messages
class plugboard:
    
    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A)
            pos_B = self.right.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B+1:]

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
    