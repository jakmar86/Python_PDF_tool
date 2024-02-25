import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

def select_pdf():
    global file_paths
    file_paths = list(filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")]))
    if not file_paths:
        return
    listbox.delete(0, tk.END)
    for file_path in file_paths:
        listbox.insert(tk.END, os.path.basename(file_path))  # show only filename

def move_up():
    selected = listbox.curselection()
    if not selected:
        return
    for pos in selected:
        if pos == 0:
            continue
        text = listbox.get(pos)
        listbox.delete(pos)
        listbox.insert(pos - 1, text)
        listbox.select_set(pos - 1)

def move_down():
    selected = listbox.curselection()
    if not selected:
        return
    for pos in reversed(selected):
        if pos == listbox.size() - 1:
            continue
        text = listbox.get(pos)
        listbox.delete(pos)
        listbox.insert(pos + 1, text)
        listbox.select_set(pos + 1)

def split_pdf():
    if not file_paths:
        return

    for file_path in file_paths:
        pdf = PdfReader(file_path)
        for page in range(len(pdf.pages)):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf.pages[page])

            output_filename = f'{file_path}_page_{page}.pdf'

            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)

            text.insert(tk.END, f'Created: {output_filename}\n')

        text.insert(tk.END, 'Done\n')

def clear_window():
    text.delete(1.0, tk.END)
    listbox.delete(0, tk.END)

def merge_pdfs():
    global file_paths
    pdf_merger = PdfMerger()
    for path in file_paths:
        pdf_merger.append(path)
        text.insert(tk.END, f'Selected: {os.path.basename(path)}\n')

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf")
    pdf_merger.write(output_path)
    pdf_merger.close()

    text.insert(tk.END, 'Done\n')


root = tk.Tk()
root.geometry('800x600')

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Split PDF", command=lambda: open_new_window(split_pdf))
file_menu.add_command(label="Merge PDFs", command=lambda: open_new_window(merge_pdfs))

def open_new_window(action):
    global file_paths, label, text, listbox
    new_window = tk.Toplevel(root)
    new_window.geometry('800x600')

    select_button = tk.Button(new_window, text="Select PDF file", command=select_pdf)
    select_button.pack()

    listbox = tk.Listbox(new_window, width=100)  # make listbox wider
    listbox.pack()

    scrollbar = tk.Scrollbar(new_window)  # create a scrollbar
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox.config(yscrollcommand=scrollbar.set)  # attach listbox to scrollbar
    scrollbar.config(command=listbox.yview)

    up_button = tk.Button(new_window, text="Move Up", command=move_up)
    up_button.pack()

    down_button = tk.Button(new_window, text="Move Down", command=move_down)
    down_button.pack()

    action_button = tk.Button(new_window, text=action.__name__, command=action)
    action_button.pack()

    clear_button = tk.Button(new_window, text="Clear", command=clear_window)
    clear_button.pack()

    label = tk.Label(new_window, text="")
    label.pack()

    text = tk.Text(new_window)
    text.pack(fill=tk.BOTH, expand=True)  # make text widget expand to fill window

    new_window.transient(root)
    new_window.grab_set()

root.mainloop()
