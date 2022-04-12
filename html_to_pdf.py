import pdfkit
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import extract_zip
import glob

currdir = os.getcwd()
zip_extract_path = (currdir+"/faturalar")

root = Tk()
root.title('HTML-PDF DÖNÜŞTÜRÜCÜ')
root.resizable(False, False)
root.geometry('500x250')

def select_zip_directory():
    tempdir = fd.askdirectory(parent=root, initialdir=currdir, title='.Zip klasörü seç')
    return tempdir

def html_to_pdf():
    #Select all zip file
    zip_directory = glob.glob(select_zip_directory()+"/*.zip")

    for i in zip_directory:
        #Folder name consists of filename
        my_folder_name = i.split("\\")[-1].split(".")[0]
        my_directory = zip_extract_path+"/"+my_folder_name

        #Call the extract_zip class
        zip_extractor = extract_zip.ExtractZip(i,my_directory)
        extract_zip.ExtractZip.extractZip(zip_extractor)

        #Delete zip file
        os.remove(i)

        #Select html file path
        html_path = glob.glob(my_directory+"/*.html")

        #HTML --> PDF Converter
        pdfkit.from_file(html_path, zip_extract_path+"/"+my_folder_name+".pdf")

        #Delete junk files
        deleted_files = glob.glob(my_directory+"/*")
        for j in deleted_files:
            os.remove(j)
        os.rmdir(my_directory)

    showinfo(
        title='PDF Dönüştürme',
        message="Dosyalar Başarıyla PDF Formatına Dönüştürüldü..."
    )


open_button = ttk.Button(
    root,
    text=".Zip dosyalarının olduğu klasörü seç",
    command=html_to_pdf
)

open_button.pack(expand=True)

root.mainloop()





