import os
import shutil
# Creado por --> Jeisson Montenegro

# TODO: Carpeta destino

print('\t\t\t\tEscribe bien tu ruta por favor ...\n')
print('\t\t\t\tEJEMPLO DE RUTA 🤟🤟🤟:')
print('\t\t\t\tLinux➡️➡️➡️: /home/test/Descargas')
print(' \t\t\t\tWindows➡️➡️➡️: C:\\Users\\NAMETEST\\Desktop\\Archives')
folderA = input('Escribe la ruta a automatizar: ')


def main():
    createFolders()
    getExtension()


def getExtension():
    img = ['.bmp', '.gif', '.jpg', '.jpeg', '.tif', '.tiff', '.png']
    videos = ['.mp4', '.mov', '.wmv', '.avi',
              '.avchd', '.flv', '.webm', '.mpeg-2']
    musica = ['.mp3']
    documents = ['.docx', '.docm', '.dotx', '.xlsx',
                 '.pdf', '.xlsb', '.xlsm', '.xltx', '.ppt', '.pptx', '.txt']

    getAll = os.listdir(folderA)
    for stringListAll in getAll:
        extension = os.path.splitext(stringListAll)
        # print(str(stringListAll) + 'extension -->'+str(extension[1]))

        # TODO: recupero el nombre completo
        a = str(extension[0])+str(extension[1])
        if str(extension[1]) in documents:
            # print(str(extension[1]))
            print('Moviendo a Documetos')
            shutil.move(folderA+"/"+a, folderA+'/Documentos')
        elif str(extension[1]) in img:
            # print(str(extension[1]))
            print('Moviendo a Images')
            shutil.move(folderA+"/"+a, folderA+'/Images')
        elif str(extension[1]) in videos:
            # print(str(extension[1]))
            print('Moviendo a Videos')
            shutil.move(folderA+"/"+a, folderA+'/Videos')
        elif str(extension[1]) in musica:
            # print(str(extension[1]))
            print('Moviendo a Musica')
            shutil.move(folderA+"/"+a, folderA+'/Musica')
        else:
            # print(str(extension))
            if str(extension[1]) == '':
                pass
            else:
                print('Moviendo a Otros')
                shutil.move(folderA+"/"+a, folderA+'/Otros')


def createFolders():
    listFolderCreate = ["Images", "Videos", "Musica", "Documentos",
                        "Otros"]  # Lista de carpetas a crear
    for folders in listFolderCreate:
        # TODO: existe o no la carpeta (True, Flase)
        existFolder = os.path.isdir(folderA+'/'+str(folders))
        if existFolder == True:
            print('Ya existe la carpeta con nombre --->'+folders)
        else:
            print('Carpeta '+folders+' creada')
            os.mkdir(folderA+'/'+folders)


if __name__ == "__main__":
    main()
