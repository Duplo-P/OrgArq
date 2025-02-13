import os 

#os.mkdir("Nova_pasta")vcriar pasta
diretorio_atual = os.getcwd() #Mostrar caminho atual
print(diretorio_atual)
print("---------")
os.chdir("Nova_pasta") # Muda o diretório de trabalho atual.
print(os.getcwd()) 
print("------Novo caminho---")
caminho = os.getcwd()
print("--------- Listar todos os arquivo da pasta----")
lista_arquivo = os.listdir(caminho)
for i in lista_arquivo:
    if i.endswith('.pdf'):
        if not os.path.exists("Arquivos Pdf"):
            os.mkdir("Arquivos Pdf")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Pdf/" + i)
    elif i.endswith('.txt'):
        if not os.path.exists("Arquivos Txt"):
            os.mkdir("Arquivos Txt")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Txt/" + i)
    elif i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.JPG') or i.endswith('.JPEG') or i.endswith('.png') or i.endswith('.PNG') or i.endswith('.gif') or i.endswith('.GIF') or i.endswith('.bmp') or i.endswith('.BMP') or i.endswith('.tiff') or i.endswith('.TIFF') or i.endswith('.svg') or i.endswith('.SVG') or i.endswith('.webp') or i.endswith('.WEBP'):
        if not os.path.exists("Arquivos Jpg"):
            os.mkdir("Arquivos Jpg")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Jpg/" + i)    
    elif i.endswith('.png'):
        if not os.path.exists("Arquivos Png"):
            os.mkdir("Arquivos Png")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Png/" + i)
    elif i.endswith('.xlsx'):
        if not os.path.exists("Arquivos Excel"):
            os.mkdir("Arquivos Excel")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Excel/" + i)  
    elif i.endswith('.docx'):
        if not os.path.exists("Arquivos Word"):
            os.mkdir("Arquivos Word")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Word/" + i)
    elif i.endswith('.pptx'):
        if not os.path.exists("Arquivos Power Point"):
            os.mkdir("Arquivos Power Point")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Power Point/" + i)    
    elif i.endswith('.zip'):
        if not os.path.exists("Arquivos Zip"):
            os.mkdir("Arquivos Zip")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Zip/" + i)
    elif i.endswith('.rar'):
        if not os.path.exists("Arquivos Rar"):
            os.mkdir("Arquivos Rar")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Rar/" + i)
    elif i.endswith('.mp3'):
        if not os.path.exists("Arquivos Mp3"):
            os.mkdir("Arquivos Mp3")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Mp3/" + i)
    elif i.endswith('.mp4'):
        if not os.path.exists("Arquivos Mp4"):
            os.mkdir("Arquivos Mp4")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Mp4/" + i)    
    elif i.endswith('.avi'):
        if not os.path.exists("Arquivos Avi"):
            os.mkdir("Arquivos Avi")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Avi/" + i)    
    elif i.endswith('.exe'):
        if not os.path.exists("Arquivos Exe"):
            os.mkdir("Arquivos Exe")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Exe/" + i)
    elif i.endswith('.iso'):
        if not os.path.exists("Arquivos Iso"):
            os.mkdir("Arquivos Iso")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Iso/" + i)    
    else:
        if not os.path.exists("Arquivos Outros"):
            os.mkdir("Arquivos Outros")
        os.rename(os.getcwd() + "/" + i, os.getcwd() + "/Arquivos Outros/" + i)
print("---------")

