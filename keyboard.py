#contains the keyboard class which converts letters to signals
class Keyboard:
    #fuunction for when the message is passing forward through the rotors
    def forward(self, letter):
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal
    
    #function for when the message is passing backward through the rotors
    def backward(self, signal):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter