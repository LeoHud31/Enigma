from keyboard import Keyboard
from Rotor import Rotor
from reflector import Reflector
from plugboard import plugboard


#actual settings of the enigma machine (wikipedia)
Rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
Rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
Rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
Rotor4 = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
Rotor5 = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")


ref1 = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
ref1 = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
ref1 = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

KEYB = Keyboard()
PLUGB = plugboard(["PO", "ML", "IU", "KJ", "NH", "YT", "GB", "VF", "RE", "DC"])

letter = "A"
signal = KEYB.forward(letter)
signal = PLUGB.forward(signal)
signal = Rotor3.forward(signal)
signal = Rotor2.forward(signal)
signal = Rotor1.forward(signal)
print(signal)