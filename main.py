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
#PLUGB = plugboard(["PO", "ML", "IU", "KJ", "NH", "YT", "GB", "VF", "RE", "DC"])

PLUGB = {"A": "A", "B": "B", "C": "C", "D": "D",
        "E": "E", "F": "F", "G": "G", "H": "H", 
        "I": "I", "J": "J", "K": "K", "L": "L", 
        "M": "M", "N": "N", "O": "O", "P": "P", 
        "Q": "Q", "R": "R", "S": "S", "T": "T", 
        "U": "U", "V": "V", "W": "W", "X": "X", 
        "Y": "Y", "Z": "Z"}

def pairs(pair):
    if len(pair) == 2:  # Ensure the pair is exactly 2 characters
        A = pair[0]
        B = pair[1]
        if A in PLUGB and B in PLUGB:  # Verify both characters are valid
            PLUGB[A] = B
            PLUGB[B] = A

print("Enter 10 pairs of letters to swap (e.g. AB):")
for i in range(10):
    while True:
        pair = input(f"Enter pair {i+1}: ").upper()
        if len(pair) == 2 and pair[0].isalpha() and pair[1].isalpha():
            pairs(pair)
            break
        else:
            print("Please enter exactly 2 letters (e.g. AB)")

message = input("Enter your message: ")
message = message.upper()
output = ""

for letter in message:
    if letter.isalpha():
        signal = KEYB.forward(letter)
        print(f"After KEYB.forward(letter): {signal}")
        
        signal = KEYB.forward(PLUGB[letter])
        print(f"After PLUGB[letter]: {signal}")
        
        signal = Rotor3.forward(signal)
        print(f"After Rotor3.forward: {signal}")
        
        signal = Rotor2.forward(signal)
        print(f"After Rotor2.forward: {signal}")
        
        signal = Rotor1.forward(signal)
        print(f"After Rotor1.forward: {signal}")
        
        signal = ref.reflect(signal)
        print(f"After ref.reflect: {signal}")
        
        signal = Rotor1.backward(signal)
        print(f"After Rotor1.backward: {signal}")
        
        signal = Rotor2.backward(signal)
        print(f"After Rotor2.backward: {signal}")
        
        signal = Rotor3.backward(signal)
        print(f"After Rotor3.backward: {signal}")
        
        output_letter = KEYB.backward(signal)
        print(f"After KEYB.backward: {output_letter}")
        
        final_letter = PLUGB[output_letter]
        print(f"After PLUGB[output_letter]: {final_letter}")
        
        output += final_letter
    else:  
        output += letter

print("Input:", message)
print("Output:", output)