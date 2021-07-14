"""
@author: Mujibul Islam Dipto
This program provides a GUI to encrypt a given plain text using the Caesar Cipher Encryption. 
The user needs to provide the text and the key for encryption.
The encrypted text is automatically copied on the clipboard.
"""


import tkinter as tk


"""
Encrypt a given plaintext using the Caesar Cipher.
"""

def encrypt(event = None):
    # create canvas to display the encrypted text
    canvas = tk.Canvas(root, width=1200, height=200)
    canvas.place(relx=.5, rely=.6, anchor="c")
    
    text = entry.get()
    key = int(spinbox.get())

    if len(text) != 0:
        out = ""
        for c in text:
            val = ord(c)

            # deal with spaces
            if c == ' ':
                out += c
                continue

            # ASCII value of uppercase starts at 65
            if c.isupper():
                new_val = ((val + key - 65) % 26) + 65
                out += chr(new_val)
            # ASCII value of lowercase starts at 97
            else:
                new_val = ((val + key - 97) % 26) + 97
                out += chr(new_val)
        
        label_enc = tk.Label(canvas, text = out)
        label_enc.config(fg = 'red')
        label_enc.config(font=("Terminal", 44))
        label_enc.place(relx=.5, rely=.5, anchor="c")

        # copy encrypted text to clipboard
        root.clipboard_append(out)
        canvas.delete("all")




# Setup GUI
root = tk.Tk()
root.title("Caesar Cipher Encryption")
root.geometry("1200x1000")



# text input to get the plain text
label_info = tk.Label(root, text = "Enter the text to encrypt and select the key")
label_info.config(fg="yellow")
label_info.config(font=("Terminal", 34))
label_info.place(relx=.5, rely=.23, anchor="c")

entry = tk.Entry(root, width=40)
entry.place(relx=.45, rely=.3, anchor="c")

# Spinbox to get the key
spinbox = tk.Spinbox(root, from_=0, to=25, width=3)
spinbox.place(relx=.6, rely=.3, anchor="c")


button = tk.Button(text='Encrypt!', command = encrypt)
button.place(relx=.5, rely=.37, anchor="c")

# ensure app works with keyboard (return key)
root.bind('<Return>', encrypt)
root.mainloop()
