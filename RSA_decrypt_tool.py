import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from sympy import mod_inverse

class RSADecryptorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Decryptor")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Info.TLabel', font=('Arial', 9))
        
        # Main frame with padding
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="RSA Decryption Tool", 
                               style='Header.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Prime p input
        ttk.Label(main_frame, text="Prime p:", font=('Arial', 10)).grid(
            row=1, column=0, sticky=tk.W, pady=5)
        self.p_entry = ttk.Entry(main_frame, width=50, font=('Courier', 9))
        self.p_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Prime q input
        ttk.Label(main_frame, text="Prime q:", font=('Arial', 10)).grid(
            row=2, column=0, sticky=tk.W, pady=5)
        self.q_entry = ttk.Entry(main_frame, width=50, font=('Courier', 9))
        self.q_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Ciphertext input
        ttk.Label(main_frame, text="Ciphertext:", font=('Arial', 10)).grid(
            row=3, column=0, sticky=tk.W, pady=5)
        self.c_entry = ttk.Entry(main_frame, width=50, font=('Courier', 9))
        self.c_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Public exponent (optional, default 65537)
        ttk.Label(main_frame, text="Public exponent (e):", font=('Arial', 10)).grid(
            row=4, column=0, sticky=tk.W, pady=5)
        self.e_entry = ttk.Entry(main_frame, width=50, font=('Courier', 9))
        self.e_entry.insert(0, "65537")
        self.e_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Decrypt button
        decrypt_btn = ttk.Button(main_frame, text="Decrypt", 
                                command=self.decrypt, style='Accent.TButton')
        decrypt_btn.grid(row=5, column=0, columnspan=2, pady=20)
        
        # Results section
        ttk.Label(main_frame, text="Results:", style='Header.TLabel').grid(
            row=6, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        
        # Results text area
        self.result_text = scrolledtext.ScrolledText(main_frame, 
                                                     width=70, 
                                                     height=15, 
                                                     font=('Courier', 9),
                                                     wrap=tk.WORD)
        self.result_text.grid(row=7, column=0, columnspan=2, 
                             sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Configure row weight for text area
        main_frame.rowconfigure(7, weight=1)
        
        # Clear button
        clear_btn = ttk.Button(main_frame, text="Clear All", command=self.clear_all)
        clear_btn.grid(row=8, column=0, columnspan=2, pady=10)
        
        # Status bar
        self.status_label = ttk.Label(main_frame, text="Ready", 
                                     style='Info.TLabel', relief=tk.SUNKEN)
        self.status_label.grid(row=9, column=0, columnspan=2, 
                              sticky=(tk.W, tk.E), pady=(10, 0))
    
    def decrypt(self):
        try:
            # Clear previous results
            self.result_text.delete(1.0, tk.END)
            self.status_label.config(text="Processing...")
            self.root.update()
            
            # Get input values
            p_str = self.p_entry.get().strip()
            q_str = self.q_entry.get().strip()
            c_str = self.c_entry.get().strip()
            e_str = self.e_entry.get().strip()
            
            # Validate inputs
            if not all([p_str, q_str, c_str, e_str]):
                messagebox.showerror("Error", "All fields are required!")
                self.status_label.config(text="Error: Missing fields")
                return
            
            # Convert to integers
            p = int(p_str)
            q = int(q_str)
            c = int(c_str)
            e = int(e_str)
            
            # Calculate n
            n = p * q
            
            # Calculate Euler's totient
            phi = (p - 1) * (q - 1)
            
            # Calculate private key
            d = mod_inverse(e, phi)
            
            # Decrypt
            m = pow(c, d, n)
            
            # Convert to hex and decode
            hex_m = hex(m)[2:]  # Remove '0x'
            
            # Try to decode as UTF-8
            try:
                plain_text = bytes.fromhex(hex_m).decode('utf-8')
            except (UnicodeDecodeError, ValueError):
                try:
                    plain_text = bytes.fromhex(hex_m).decode('utf-8', errors='ignore')
                except:
                    plain_text = f"Could not decode as UTF-8. Raw hex: {hex_m}"
            
            # Display results
            results = f"""RSA Decryption Results
{'='*60}

Public Key (n): {n}
Public Exponent (e): {e}

Prime p: {p}
Prime q: {q}

Euler's Totient (φ): {phi}
Private Key (d): {d}

Ciphertext (c): {c}
Decrypted Message (m): {m}

Hex Representation: {hex_m}

{'='*60}
DECRYPTED TEXT:
{plain_text}
{'='*60}
"""
            
            self.result_text.insert(1.0, results)
            self.status_label.config(text="Decryption successful!")
            
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {str(ve)}\nPlease enter valid integers.")
            self.status_label.config(text="Error: Invalid input")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_label.config(text=f"Error: {str(e)}")
    
    def clear_all(self):
        """Clear all input fields and results"""
        self.p_entry.delete(0, tk.END)
        self.q_entry.delete(0, tk.END)
        self.c_entry.delete(0, tk.END)
        self.e_entry.delete(0, tk.END)
        self.e_entry.insert(0, "65537")
        self.result_text.delete(1.0, tk.END)
        self.status_label.config(text="Ready")

def main():
    root = tk.Tk()
    app = RSADecryptorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()