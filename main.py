import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from utils.path_utils import resource_path


sing_codes = {
    "A": "7  1", "B": "7  2", "C": "7  3", "D": "7  4", "E": "8  1", "F": "8  2", "G": "8  3", "H": "8  4", "I": "9  1",
    "J": "9  2", "K": "9  3", "L": "9  4", "M": "4  1", "N": "4  2", "O": "4  3", "P": "4  4", "Q": "5  1", "R": "5  2",
    "S": "5  3", "T": "5  4", "U": "6  1", "V": "6  2", "W": "6  3", "X": "6  4", "Y": "1  1", "Z": "1  2", "Ź": "1  3",
    "Ż": "1  4", "Ą": "2  1", "Ć": "2  2", "Ę": "2  3", "Ł": "2  4", "Ó": "3  1", "Ś": "3  2", "Ń": "3  3", "@": "3  4",
    "-": "0  1", "/": "0  2", "\"": "0  3", "%": "0  4", " ": "00 1", "&": "00 2", "!": "00 3", "*": "00 4",
    "_": ",  1", "(": ",  2", ")": ",  3", ".": ",  4", ",  ": ",  0", "1": "1  0", "2": "2  0", "3": "3  0",
    "4": "4  0", "5": "5  0", "6": "6  0", "7": "7  0", "8": "8  0", "9": "9  0", "0": "0  0"
}


def calculate_widget_width(widget: (tkinter.Entry, ScrolledText)):
    return widget.winfo_width()


def gen_bingo_str():
    _input = str_input.get().upper()
    converted_input = []
    element_per_line = calculate_widget_width(converted_str_text) // 80 - 1
    for index, sign in enumerate(_input):
        if index > 0 and index % element_per_line == 0:
            converted_input.append("\n")
        if sign in sing_codes:
            converted_input.append(sing_codes[sign])
        else:
            # Handle unsupported characters
            converted_input.append(f"?? {sign}")
    converted_str_text.config(state=NORMAL)
    converted_str_text.delete(1.0, END)  # Clear previous text
    if converted_input:
        new_text = " | " + " | ".join(converted_input) + " | "
        converted_str_text.insert(END, new_text)  # Insert new text
        converted_str_text.config(state=DISABLED)


# Main window setup
window = Tk()
window.title("PosNetBingo")
window.iconbitmap(resource_path("icon.ico"))
window.minsize(width=500, height=450)
window.config(bg="#f0f0f0", padx=20, pady=20)

# Title
title = Label(window, text="PosNetBingo", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333333")
title.grid(column=0, row=0, columnspan=2, pady=(10, 20))

# Labels
str_input_lbl = Label(window, text="Wprowadź tekst", font=("Helvetica", 12), bg="#f0f0f0", fg="#333333")
str_input_lbl.grid(column=0, row=1, pady=10, padx=5, sticky=E)

# Entries
str_input = Entry(window, font=("Helvetica", 12), width=30)
str_input.grid(column=1, row=1, pady=10, padx=5, sticky=W)

# Converted string scrolled text
converted_str_text = ScrolledText(window, font=("Consolas", 15), bg="#ffffff", fg="#000000", height=10, wrap=WORD)
converted_str_text.grid(column=0, row=2, columnspan=2, pady=10, sticky=EW)

# Generate button
generate_btn = Button(window, command=gen_bingo_str, text="Generuj kod Bingo", font=("Helvetica", 12, "bold"),
                      bg="#4CAF50", fg="white")
generate_btn.grid(column=0, row=3, columnspan=2, pady=10, padx=5, sticky=EW)

# Adjust column weights to make the layout responsive
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()
