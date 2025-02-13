import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os


extensoes_imagem = ('.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG', '.gif', '.GIF', '.bmp', '.BMP', '.tiff', '.TIFF', '.svg', '.SVG', '.webp', '.WEBP')
extensao_video = ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.m4v')
extensao_doc = ('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp')
extensao_zip = ('.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz')
extensao_exe = ('.exe', '.bat', '.sh', '.bin', '.cmd', '.com', '.msi', '.jar', '.py', '.pl')
extensao_audio = ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.aiff', '.alac')

def get_path():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    return path

def mover(NomePasta, arquivos):
    try:
        if not os.path.exists(NomePasta):
            os.mkdir(NomePasta)
        os.rename(os.getcwd() + "/" + arquivos, os.getcwd() + "/" + NomePasta + "/" + arquivos)
    except: 
        messagebox.showerror("Erro", "Erro ao mover arquivo")
        
def moverDoc(NomePasta):
    try:
        os.chdir(NomePasta)
        lista_doc = os.listdir(os.getcwd()) 

        for i in lista_doc:
            if os.path.isdir(i):
                continue
            for ext in extensao_doc:
                if i.endswith(ext):
                    if not os.path.exists(ext):
                        os.mkdir(ext)
                    os.rename(os.getcwd() + "/" + i, os.getcwd() + "/" + ext + "/" + i)
                    break
            else:
                if not os.path.exists("Arquivos Outros"):
                    os.mkdir("Arquivos Outros")
                os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Outros/" + i)
    except:
        messagebox.showerror("Erro", "Erro ao mover arquivo")
def organizar_arquivos():
    caminho = get_path()
    os.chdir(caminho)
    lista_arquivos = os.listdir(caminho)
    for i in lista_arquivos:
        if i.endswith(extensao_doc):
            mover("Arquivos Documentos", i)
        
        elif i.endswith(extensoes_imagem):
            mover("Arquivos Imagens", i)
            
        elif i.endswith(extensao_video):
           mover("Arquivos Videos", i)
           
        elif i.endswith(extensao_audio):
           mover("Arquivos Áudios", i)
           
        elif i.endswith(extensao_zip):
            mover("Arquivos Compactados", i)
            
        elif i.endswith(extensao_exe):
            mover("Arquivos Executaveis", i)
        else:
            if os.path.isdir(i):
                continue
            else:
                mover("Arquivos Outros", i)
    moverDoc("Arquivos Documentos")
    messagebox.showinfo("Organização de Arquivos", "Arquivos organizados com sucesso!")