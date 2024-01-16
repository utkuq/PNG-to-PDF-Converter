import customtkinter as ctk
from tkinter import filedialog as fd
from PIL import Image
import os
from tkinter import messagebox

root = ctk.CTk()
root.title('PDF Merger')
root.geometry("300x100")
root.eval('tk::PlaceWindow . center')


def convert_pngs_to_pdf(png_dir):
    try:
        # Sort file paths by file name
        file_paths = sorted(png_dir)

        # Open each PNG file and append to list of images
        images = []
        for file_path in file_paths:
            image = Image.open(file_path).convert("RGB")
            images.append(image)

        # Convert list of images to PDF and save
        current_path = os.getcwd()
        pdf_path = os.path.join(current_path, "output.pdf")
        images[0].save(pdf_path, save_all=True, append_images=images[1:])
        messagebox.showinfo("Info", "Merging Completed")
    except Exception as e:
        messagebox.showerror("Error", e)


arr = []


def fileSelect():
    global arr
    filetypes = (("PNG Files", "*.png"), ("All Files", "*.*"))
    filenames = fd.askopenfilenames(
        title="Open Files", initialdir="/", filetypes=filetypes)
    arr = [i for i in filenames]
    convert_pngs_to_pdf(arr)


btn1 = ctk.CTkButton(
    master=root, text="Select Files & Merge", command=fileSelect)
btn1.pack(padx=10, pady=40)

root.mainloop()
