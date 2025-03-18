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


ref = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")


KEYB = Keyboard()
PLUGB = plugboard(["PO", "ML", "IU", "KJ", "NH", "YT", "GB", "VF", "RE", "DC"])



letter = input("Enter a letter: ")
letter = letter.upper()
signal = KEYB.forward(letter)
signal = PLUGB.forward(signal)
signal = Rotor3.forward(signal)
signal = Rotor2.forward(signal)
signal = Rotor1.forward(signal)
signal = ref.reflect(signal)
signal = Rotor1.backward(signal)
signal = Rotor2.backward(signal)
signal = Rotor3.backward(signal)
signal = PLUGB.backward(signal)
signal = KEYB.backward(signal)

print(letter)
print(signal)