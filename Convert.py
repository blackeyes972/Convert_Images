import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import time
from datetime import datetime
import os
from PIL import Image, ImageTk

# crea la finestra principale
root = tk.Tk()
root.title("Convert your images")
root.geometry("600x400")
root.resizable(False, False)      
root.iconbitmap("assets/icon.ico")
root.config(cursor="hand2")


#prendo l'ora corrente    
now = datetime.now()
current_time = now.strftime("%I:%M:%S ")


# carica l'immagine da visualizzare
image_path = "assets/logo.png"
logo_image = Image.open(image_path)
logo_image = logo_image.resize((150, 150))  # ridimensiona l'immagine
logo_photo = ImageTk.PhotoImage(logo_image)

# crea un label per l'immagine
logo_label = ttk.Label(root, image=logo_photo)
logo_label.pack()

# crea un label per il titolo
title_label = tk.Label(root, text="Convert your images",  font=("Arial", 24))
title_label.pack()



PATH = 'Convert_images'
SUBFOLDER = 'converted_images'

def create_image_folder():
    # crea la cartella per le immagini se non esiste già
    if not os.path.exists(os.path.join(SUBFOLDER)):
        os.makedirs(os.path.join(SUBFOLDER))

def jpg_to_png():
    # crea la cartella per le immagini se non esiste già
    create_image_folder()

    # seleziona il file da convertre
    file = filedialog.askopenfilename(initialdir="/", title="Select the JPG file", defaultextension=".jpg", filetypes=(("JPG files", "*.jpg"), ("all files", "*.*")))
    if not file:
        # l'utente ha cliccato "Cancel"
        return

    # converte il file
    with Image.open(file) as img:
        # salva l'immagine in formato PNG
        filename = os.path.splitext(os.path.basename(file))[0] + ".png"
        output_path = os.path.join(SUBFOLDER, filename)
        img.save(output_path)
        converted_image_label.configure(text=output_path)
        messagebox.showinfo(title="Conversion completed", message="{} -> {}".format(file, output_path))
        converted_image_label.configure(text='')


def png_to_jpg():
   # crea la cartella per le immagini se non esiste già
    create_image_folder()

    # seleziona il file da convertre
    file = filedialog.askopenfilename(initialdir="/", title="Select the PNG file", defaultextension=".jpg", filetypes=(("PNG files", "*.png"), ("all files", "*.*")))
    if not file:
        # l'utente ha cliccato "Cancel"
        return

    # converte il file
    with Image.open(file) as img:
        # salva l'immagine in formato PNG
        filename = os.path.splitext(os.path.basename(file))[0] + ".jpg"
        output_path = os.path.join(SUBFOLDER, filename)
         # convert the mode to RGB if it has an alpha channel
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        img.save(output_path)
        converted_image_label.configure(text=output_path)
        messagebox.showinfo(title="Conversion completed", message="{} -> {}".format(file, output_path))
        converted_image_label.configure(text='')





def image_to_ico():
    # crea la cartella per le immagini se non esiste già
    create_image_folder()

    # seleziona il file da convertre
    file = filedialog.askopenfilename(initialdir="/", title="Select the ICO file", defaultextension=".jpg", filetypes=(("PNG files", "*.png"),("JPG files", "*.jpg"), ("all files", "*.*")))
    if not file:
        # l'utente ha cliccato "Cancel"
        return

    # apri l'immagine in formato JPG o PNG
    with Image.open(file) as img:
        # ridimensiona l'immagine proporzionalmente mantenendo l'aspect ratio
        width, height = img.size
        if width > height:
            new_width = 256
            new_height = int((new_width / width) * height)
        else:
            new_height = 256
            new_width = int((new_height / height) * width)
        img = img.resize((new_width, new_height), resample=Image.LANCZOS) # da luglio 2023 Resampling

        # crea un'icona vuota con la dimensione desiderata
        icon = Image.new('RGBA', (256, 256), (255, 255, 255, 0))
        # copia l'immagine ridimensionata nell'icona
        icon.paste(img, ((256 - new_width) // 2, (256 - new_height) // 2))

        # salva l'immagine in formato ICO
        filename = os.path.splitext(os.path.basename(file))[0] + ".ico"
        output_path = os.path.join(SUBFOLDER, filename)
        icon.save(output_path, format="ICO")
        converted_image_label.configure(text=output_path)
        messagebox.showinfo(title="Conversion completed", message="{} -> {}".format(file, output_path))
        converted_image_label.configure(text='')



def convert_jpgs_to_pngs():
    # crea la cartella per le immagini convertte se non esiste già
    folder = filedialog.askdirectory(initialdir="/", title="Enter the path to the folder containing the JPG images to convert: ")
    output_folder = os.path.join(folder, "converted_images")
    os.makedirs(output_folder, exist_ok=True)

    # itera su tutti i file nella cartella e converte i file JPG in PNG
    for filename in os.listdir(folder):
        if filename.endswith(".jpg"):
            file_path = os.path.join(folder, filename)
            with Image.open(file_path) as img:
                output_filename = os.path.splitext(filename)[0] + ".png"
                output_path = os.path.join(output_folder, output_filename)
                img.save(output_path)
                converted_image_label.configure(text=output_path)


    messagebox.showinfo(title="Conversion completed", message="{} -> {}".format(filename, output_path))
    converted_image_label.configure(text='')
    convert_jpgs_to_pngs(folder)

def convert_pngs_to_jpgs():
    # crea la cartella per le immagini convertte se non esiste già
    folder = filedialog.askdirectory(initialdir="/", title="Enter the path to the folder containing the JPG images to convert: ")
    output_folder = os.path.join(folder, "converted_images")
    os.makedirs(output_folder, exist_ok=True)

    # itera su tutti i file nella cartella e converte i file JPG in PNG
    for filename in os.listdir(folder):
        if filename.endswith(".png"):
            file_path = os.path.join(folder, filename)
            with Image.open(file_path) as img:
                output_filename = os.path.splitext(filename)[0] + ".jpg"
                output_path = os.path.join(output_folder, output_filename)
                 # convert the mode to RGB if it has an alpha channel
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                img.save(output_path)
                converted_image_label.configure(text=output_path)

    messagebox.showinfo(title="Conversion completed", message="{} -> {}".format(filename, output_path))
    converted_image_label.configure(text='')
    convert_pngs_to_jpgs(folder)



def convert_images_to_ico():
    # crea la cartella per le immagini se non esiste già
    create_image_folder()

    # seleziona la cartella contenente le immagini da convertre
    folder_path = filedialog.askdirectory(initialdir="/", title="Select folder containing images")
    if not folder_path:
        # l'utente ha clicato "Cancel"
        return

    for filename in os.listdir(folder_path):
        # salta i file che non sono immagini PNG o JPG
        if not filename.lower().endswith(('.png', '.jpg')):
            continue

        # crea il percorso completo del file
        file_path = os.path.join(folder_path, filename)

        # apri l'immagine in formato JPG o PNG
        with Image.open(file_path) as img:
            # ridimensiona l'immagine proporzionalmente mantenendo l'aspect ratio
            width, height = img.size
            if width > height:
                new_width = 256
                new_height = int((new_width / width) * height)
            else:
                new_height = 256
                new_width = int((new_height / height) * width)
            img = img.resize((new_width, new_height), resample=Image.LANCZOS) # da luglio 2023 Resampling

            # crea un'icona vuota con la dimensione desiderata
            icon = Image.new('RGBA', (256, 256), (255, 255, 255, 0))
            # copia l'immagine ridimensionata nell'icona
            icon.paste(img, ((256 - new_width) // 2, (256 - new_height) // 2))

            # salva l'immagine in formato ICO
            output_filename = os.path.splitext(filename)[0] + ".ico"
            output_path = os.path.join(SUBFOLDER, output_filename)
            icon.save(output_path, format="ICO")
            converted_image_label.configure(text=output_path)
            messagebox.showinfo(title="Conversion completed", message="{} -> {}".format(filename, output_path))
            converted_image_label.configure(text='')

# menu a tendina con le opzioni
options_frame = Frame(root)
options_frame.pack(side=TOP, fill=X)

option_var = StringVar(value="Select an option...")
options = ["Convert JPG to PNG", "Convert PNG to JPG", "Convert to ICO", "Convert multiple JPG images to PNG","Convert multiple PNG images to JPG",
           "Convert multiple images to ICO"]
option_menu = OptionMenu(options_frame, option_var, *options)
option_menu.pack(side=TOP, padx=10, pady=10)

def convert_image():
    selected_option = option_var.get()
    if selected_option == "Convert JPG to PNG":
        jpg_to_png()
    elif selected_option == "Convert PNG to JPG":
        png_to_jpg()
    elif selected_option == "Convert to ICO":
        image_to_ico()
    elif selected_option == "Convert multiple JPG images to PNG":
        convert_jpgs_to_pngs()
    elif selected_option == "Convert multiple PNG images to JPG":
        convert_pngs_to_jpgs()
    elif selected_option == "Convert multiple images to ICO":
        convert_images_to_ico()

def create_menu(root):
    # Crea la menubar 
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0) 
    convert_menu = tk.Menu(menubar, tearoff=0)
    convertplus_menu = tk.Menu(menubar, tearoff=0)
    
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Exit", command=root.quit)
    
    menubar.add_cascade(label="Convert single images", menu=convert_menu)
    convert_menu.add_command(label="Convert JPG to PNG", command=jpg_to_png)
    convert_menu.add_command(label="Convert PNG to JPG", command=png_to_jpg)
    convert_menu.add_command(label="Convert to ICO", command=image_to_ico)
    
    menubar.add_cascade(label="Convert multiple images", menu=convertplus_menu)
    convertplus_menu.add_command(label="Convert multiple JPG images to PNG", command=convert_jpgs_to_pngs)
    convertplus_menu.add_command(label="Convert multiple PNG images to JPG", command=convert_pngs_to_jpgs)
    convertplus_menu.add_command(label="Convert multiple images to ICO", command=convert_images_to_ico)

    root.config(menu=menubar)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label = "About...", command=About_me)
    menubar.add_cascade(label="?", menu=helpmenu)
    #Creo barra di stato
    status_bar = Label(root, text="", bg="#434343", fg="white", bd=1,relief=SUNKEN, anchor=E)
    status_bar.pack(fill=X, side=BOTTOM, ipady=2)
    #orologio status bar
    def clock():
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        second = time.strftime("%S ")
        day = time.strftime("%A %d %B")

        status_bar.config(text=day + " - " + hour + ":" + minute + ":" + second)
        status_bar.after(1000, clock)
        # la funzione clock() viene chiamata alla fine della funzione create_menu() per avviare l'orologio sulla barra di stato.
    clock()

def About_me():
    messagebox.showinfo(title="Info", message="Convert images to various formats.")

converted_image_label = Label(root, text="")
converted_image_label.pack(padx=10, pady=10)

# crea i bottoni per avviare le funzioni di conversione
convert_button = Button(root, text="Convert", command=convert_image)
convert_button.pack(side=TOP, padx=10, pady=10)

# avvia la finestra principale
create_menu(root)
root.mainloop()