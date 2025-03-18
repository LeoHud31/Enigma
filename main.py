from keyboard import Keyboard
from Rotor import Rotor
from reflector import Reflector
import tkinter as tk
from tkinter import ttk, messagebox

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

class EnigmaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Machine")
        self.root.geometry("600x400")  # Set window size
        self.pairs_count = 0
        
        try:
            self.setup_gui()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to setup GUI: {str(e)}")

    def setup_gui(self):
        # Plugboard frame
        self.plugboard_frame = ttk.LabelFrame(self.root, text="Plugboard Setup")
        self.plugboard_frame.pack(padx=10, pady=5, fill="x")

        self.pair_entry = ttk.Entry(self.plugboard_frame, width=5)
        self.pair_entry.pack(side="left", padx=5)
        
        self.pair_label = ttk.Label(self.plugboard_frame, text="Enter pair 1/10")
        self.pair_label.pack(side="left", padx=5)
        
        self.pair_button = ttk.Button(self.plugboard_frame, text="Add Pair", command=self.add_pair)
        self.pair_button.pack(side="left", padx=5)

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
                if key < value:  # Only show each pair once
                    if key != value:  # Only show actual swapped pairs
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

    def encode_message(self):
        message = self.message_entry.get().upper()
        output = ""
        
        for letter in message:
            if letter.isalpha():
                signal = KEYB.forward(letter)
                self.output_list.insert(tk.END, f"After KEYB.forward(letter): {signal}")
                
                signal = KEYB.forward(PLUGB[letter])
                self.output_list.insert(tk.END, f"After PLUGB[letter]: {signal}")
                
                signal = Rotor3.forward(signal)
                self.output_list.insert(tk.END, f"After Rotor3.forward: {signal}")
                
                signal = Rotor2.forward(signal)
                self.output_list.insert(tk.END, f"After Rotor2.forward: {signal}")
                
                signal = Rotor1.forward(signal)
                self.output_list.insert(tk.END, f"After Rotor1.forward: {signal}")
                
                signal = ref.reflect(signal)
                self.output_list.insert(tk.END, f"After ref.reflect: {signal}")
                
                signal = Rotor1.backward(signal)
                self.output_list.insert(tk.END, f"After Rotor1.backward: {signal}")
                
                signal = Rotor2.backward(signal)
                self.output_list.insert(tk.END, f"After Rotor2.backward: {signal}")
                
                signal = Rotor3.backward(signal)
                self.output_list.insert(tk.END, f"After Rotor3.backward: {signal}")
                
                output_letter = KEYB.backward(signal)
                self.output_list.insert(tk.END, f"After KEYB.backward: {output_letter}")
                
                final_letter = PLUGB[output_letter]
                self.output_list.insert(tk.END, f"After PLUGB[output_letter]: {final_letter}")
                
                output += final_letter
            else:
                output += letter
        
        self.output_list.insert(tk.END, f"Input: {message}")
        self.output_list.insert(tk.END, f"Output: {output}")
        self.output_list.insert(tk.END, "------------------------")
        self.message_entry.delete(0, tk.END)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = EnigmaGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Failed to start application: {str(e)}")