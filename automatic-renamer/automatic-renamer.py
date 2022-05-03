import PySimpleGUI as sg
import sys
import os
import re


def renameTvShow(textShow):
    vecTextShow = []
    vecTextShow = textShow.replace(' ', '.').replace('-', '.').split('.')[:-1]
    vecNewName = []
    for text in vecTextShow:
        if re.match('([s])\d\d+([e])\d\d', text.lower()):
            vecNewName.append(text.lower().replace('e', ' Epi_').replace('s', 'Tem_'))
            break
        vecNewName.append(text.capitalize())
        
    newName = ' '.join(vecNewName)
    return newName

def renameMovie(textMovie):
    vecTextMovie = []
    vecTextMovie = textMovie.replace(' ', '.').replace('-', '.').split('.')[:-1]
    vecNewName = []
    for text in vecTextMovie:
        if re.match('(20)\d\d', text):
            vecNewName.append(text.capitalize())
            break
        vecNewName.append(text.capitalize())
        
    newName = ' '.join(vecNewName)
    return newName

def renameAnime(textAnime):
    vecTextAnime = []
    vecTextAnime = textAnime.replace(' ', '.').replace('-', '.').split('.')[:-1]
    vecNewName = []
    teste = False
    for text in vecTextAnime:
        if re.match('\d\d', text) or re.match('\d', text) and teste:
            vecNewName.append(text.capitalize())
            break
        if re.match('(episodio)', text):
            teste = True
    
    if len(vecNewName) == 0:
        for text in vecTextAnime:
            if re.match('\d\d', text) or re.match('\d', text):
                vecNewName.append(text.capitalize())
                break
            
    newName = ' '.join(vecNewName)
    return newName

def renameFile(new):
    if new == '':
        return
    
    oldName = sys.argv[1]
    diretorio = '\\'.join(sys.argv[1].split('\\')[:-1])+str('\\')
    newName = str(diretorio)+str(new)
    print(oldName)
    print(newName)
    os.rename(oldName,newName)  

def main():
    sg.theme('Black')
    filename = sys.argv[1].split('\\')[-1][:-1]
    extension = str('.') + filename.split('.')[-1]
    extensions = ['.srt','.mp4','.mkv','.avi']
    if extension not in extensions:
        extension = ''
    
    layout = [
        [sg.Text('Automatic Rename', size=(50, 1), justification='center')],
        [sg.Button('Series'), sg.Button('Movie'), sg.Button('Anime')],
        [sg.Text('From: '+str(filename), size=(50, 1), justification='center')],
        [sg.Text('To: '), sg.Input(key='-INPUT-')],
        [sg.Button('Rename'),sg.Button('Cancel')]    ]
    window = sg.Window(
        '', layout,
        font=('Arial', 12, 'bold'),
        element_justification='c'
    )
    while True:
        event, values = window.read()
        newName=''
            
        if event  == 'Series':
            newName = renameTvShow(filename)
            
        if event  == 'Movie':
            newName = renameMovie(filename)
            
        if event  == 'Anime':
            newName = renameAnime(filename)
            
        if newName != '':
            window['-INPUT-'].update(newName + str(extension))
        else:
            window['-INPUT-'].update(filename)
            
        if event == 'Rename':
            renameFile(values['-INPUT-'])
            break
    
        if event == 'Cancel' or event == sg.WINDOW_CLOSED:
            break
    
    window.close()

main()