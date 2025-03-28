#import statements from the other files
from keyboard import Keyboard
from Rotor import Rotor
from reflector import Reflector
import tkinter as tk
from tkinter import ttk, messagebox

#actual settings of the enigma machine (wikipedia) based on Enigma I introduced in 1930
Rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "q")
Rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "e")
Rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "v")
Rotor4 = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "j")
Rotor5 = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "z")


ref = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")


KEYB = Keyboard()

#dictionary of the plugboard settings
PLUGB = {"A": "A", "B": "B", "C": "C", "D": "D",
        "E": "E", "F": "F", "G": "G", "H": "H", 
        "I": "I", "J": "J", "K": "K", "L": "L", 
        "M": "M", "N": "N", "O": "O", "P": "P", 
        "Q": "Q", "R": "R", "S": "S", "T": "T", 
        "U": "U", "V": "V", "W": "W", "X": "X", 
        "Y": "Y", "Z": "Z"}

#function to add pairs to the plugboard
def pairs(pair):
    if len(pair) == 2:  
        A = pair[0]
        B = pair[1]
        if A in PLUGB and B in PLUGB:  
            PLUGB[A] = B
            PLUGB[B] = A


#class for the GUI
class EnigmaGUI:
    #gui for the enigma machine
    #constructor for the GUI
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Machine")
        self.root.geometry("600x700")  # Set window size
        self.pairs_count = 0
        
        try:
            self.setup_gui()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to setup GUI: {str(e)}")

    def set_rotors(self):
        # Set the rotor positions
        rotor1_Option = self.rotor_entry_1
        rotor2_Option = self.rotor_entry_2
        rotor3_Option = self.rotor_entry_3

        #nested if statements to set the rotors based on the user input
        if rotor1_Option == "1":
            rotor1_Option = Rotor1
        elif rotor1_Option == "2":
            rotor1_Option = Rotor2
        elif rotor1_Option == "3":
            rotor1_Option = Rotor3
        elif rotor1_Option == "4":
            rotor1_Option = Rotor4
        elif rotor1_Option == "5":
            rotor1_Option = Rotor5

        if rotor2_Option == "1":
            rotor2_Option = Rotor1
        elif rotor2_Option == "2":
            rotor2_Option = Rotor2
        elif rotor2_Option == "3":
            rotor2_Option = Rotor3
        elif rotor2_Option == "4":
            rotor2_Option = Rotor4
        elif rotor2_Option == "5":
            rotor2_Option = Rotor5
        
        if rotor3_Option == "1":
            rotor3_Option = Rotor1
        elif rotor3_Option == "2":
            rotor3_Option = Rotor2
        elif rotor3_Option == "3":
            rotor3_Option = Rotor3
        elif rotor3_Option == "4":
            rotor3_Option = Rotor4
        elif rotor3_Option == "5":
            rotor3_Option = Rotor5
        

    def setup_gui(self):
        #set up the GUI
        # Plugboard frame
        self.plugboard_frame = ttk.LabelFrame(self.root, text="Plugboard Setup")
        self.plugboard_frame.pack(padx=10, pady=5, fill="x")

        self.pair_entry = ttk.Entry(self.plugboard_frame, width=5)
        self.pair_entry.pack(side="left", padx=5)
        
        self.pair_label = ttk.Label(self.plugboard_frame, text="Enter pair 1/10")
        self.pair_label.pack(side="left", padx=5)
        
        self.pair_button = ttk.Button(self.plugboard_frame, text="Add Pair", command=self.add_pair)
        self.pair_button.pack(side="left", padx=5)

        #rotor setup frame

        self.rotor_frame = ttk.Label(self.root)
        self.rotor_frame.pack(padx=10, pady=5, fill="x")

        self.rotor_entry_1 = ttk.Entry(self.rotor_frame, width=1)
        self.rotor_entry_1.pack(side="left", padx=5)

        self.rotor_entry_2 = ttk.Entry(self.rotor_frame, width=1)
        self.rotor_entry_2.pack(side="left", padx=5)

        self.rotor_entry_3 = ttk.Entry(self.rotor_frame, width=1)
        self.rotor_entry_3.pack(side="left", padx=5)

        self.rotor_button = ttk.Button(self.rotor_frame, text="Set Rotors", command=self.set_rotors)
        self.rotor_button.pack(side="left", padx=5)

        # Message frame
        self.message_frame = ttk.LabelFrame(self.root, text="Message")
        self.message_frame.pack(padx=10, pady=5, fill="x")

        self.message_entry = ttk.Entry(self.message_frame)
        self.message_entry.pack(side="left", padx=5, fill="x", expand=True)
        
        self.encode_button = ttk.Button(self.message_frame, text="Encode", command=self.encode_message)
        self.encode_button.pack(side="left", padx=5)

        # Output frame
        self.output_frame = ttk.LabelFrame(self.root, text="Results")
        self.output_frame.pack(padx=10, pady=5, fill="both", expand=True)

        self.output_list = tk.Listbox(self.output_frame, height=10)
        self.output_list.pack(padx=5, pady=5, fill="both", expand=True)

    #function to add pairs to the plugboard
    def add_pair(self):
        pair = self.pair_entry.get().upper()
        if len(pair) == 2 and pair[0].isalpha() and pair[1].isalpha():
            pairs(pair)
            self.pairs_count += 1
            # Display the newly added pair
            self.output_list.insert(tk.END, f"Added pair: {pair[0]} <-> {pair[1]}")
            
            # Display current plugboard state
            active_pairs = []
            for key, value in PLUGB.items():
                if key < value:  
                    if key != value: 
                        active_pairs.append(f"{key}-{value}")
            self.output_list.insert(tk.END, f"Current plugboard pairs: {', '.join(active_pairs)}")
            self.output_list.insert(tk.END, "------------------------")
            
            if self.pairs_count < 10:
                self.pair_label.config(text=f"Enter pair {self.pairs_count + 1}/10")
                self.pair_entry.delete(0, tk.END)
            else:
                self.plugboard_frame.pack_forget()
        else:
            messagebox.showerror("Error", "Please enter exactly 2 letters (e.g. AB)")

    #function to encode the message
    def encode_message(self):
        message = self.message_entry.get().upper()
        output = ""
        
        #storing the inital position of the rotors
        initial_position = {"Rotor1": Rotor1.left, 
                            "Rotor2": Rotor2.left,
                            "Rotor3": Rotor3.left}

        #looping through the message and encoding each letter with the rotors
        for letter in message:
            if letter.isalpha():
                if Rotor2.left == Rotor2.notch and Rotor3.left == Rotor3.notch:
                    Rotor1.rotate()
                    Rotor2.rotate()
                    Rotor3.rotate()
                elif Rotor3.left[0] == Rotor3.notch:
                    Rotor2.rotate()
                    Rotor3.rotate()
                else:
                    Rotor3.rotate()
                
                #sending the letter through the rotors

                signal = KEYB.forward(letter)       
                signal = KEYB.forward(PLUGB[letter])          
                signal = Rotor3.forward(signal)            
                signal = Rotor2.forward(signal)
                signal = Rotor1.forward(signal)        
                signal = ref.reflect(signal)
                signal = Rotor1.backward(signal) 
                signal = Rotor2.backward(signal)
                signal = Rotor3.backward(signal)
                output_letter = KEYB.backward(signal)
                final_letter = PLUGB[output_letter]
                Rotor1.left = initial_position["Rotor1"]
                Rotor2.left = initial_position["Rotor2"]
                Rotor3.left = initial_position["Rotor3"]
                output += final_letter
            else:
                output += letter
    
        # Display the input message and the encoded output
        self.output_list.insert(tk.END, f"Input: {message}")
        self.output_list.insert(tk.END, f"Output: {output}")
        self.output_list.insert(tk.END, "------------------------")
        self.message_entry.delete(0, tk.END)


#main function to drive events
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = EnigmaGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Failed to start application: {str(e)}")