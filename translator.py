import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator
import pyperclip


def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    source = source_lang.get()
    target = target_lang.get()

    if text == "":
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter some text.")
        return

    try:
        translated = GoogleTranslator(
            source=source.lower(),
            target=target.lower()
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Error: " + str(e))



def copy_text():
    pyperclip.copy(output_text.get("1.0", tk.END))
    status.config(text="Copied Successfully!")


root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("650x550")

tk.Label(root, text="Enter Text", font=("Arial", 14)).pack()

input_text = tk.Text(root, height=8, width=60)
input_text.pack(pady=10)

languages = [
    "english",
    "telugu",
    "hindi",
    "tamil",
    "kannada",
    "french",
    "german",
    "spanish"
]

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Source").grid(row=0, column=0)

source_lang = ttk.Combobox(frame, values=languages)
source_lang.current(0)
source_lang.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Target").grid(row=0, column=2)

target_lang = ttk.Combobox(frame, values=languages)
target_lang.current(1)
target_lang.grid(row=0, column=3)

tk.Button(
    root,
    text="Translate",
    command=translate_text,
    bg="green",
    fg="white",
    width=20
).pack(pady=15)

tk.Label(root, text="Translated Text", font=("Arial", 14)).pack()

output_text = tk.Text(root, height=8, width=60)
output_text.pack(pady=10)

tk.Button(
    root,
    text="Copy",
    command=copy_text,
    bg="blue",
    fg="white",
    width=20
).pack()

status = tk.Label(root, text="", fg="green")
status.pack()

root.mainloop()