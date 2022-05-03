import re
import sys

def renameTvShow(textShow):
    vecTextShow = []
    vecTextShow = textShow.replace(' ', '.').replace('-', '.').split('.')[:-1]
    vecNewName = []
    for text in vecTextShow:
        if re.match('([S])\d\d+(E)\d\d', text):
            vecNewName.append(text.replace('S', 'Tem_').replace('E', ' Epi_'))
            break
        vecNewName.append(text)
        
    newName = ' '.join(vecNewName)
    return newName

def renameMovie(textMovie):
    vecTextMovie = []
    vecTextMovie = textMovie.replace(' ', '.').replace('-', '.').split('.')[:-1]
    vecNewName = []
    for text in vecTextMovie:
        if re.match('(20)\d\d', text):
            vecNewName.append(text.replace('S', 'Tem_').replace('E', ' Epi_'))
            break
        vecNewName.append(text)
        
    newName = ' '.join(vecNewName)
    return newName

def renameAnime(textAnime):
    vecTextAnime = []
    vecTextAnime = textAnime.replace(' ', '.').replace('-', '.').split('.')[:-1]
    vecNewName = []
    teste = False
    for text in vecTextAnime:
        if re.match('\d\d', text) or re.match('\d', text) and teste:
            vecNewName.append(text)
            break
        if re.match('(episodio)', text):
            teste = True
    
    if len(vecNewName) == 0:
        for text in vecTextAnime:
            if re.match('\d\d', text) or re.match('\d', text):
                vecNewName.append(text)
                break
            
    newName = ' '.join(vecNewName)
    return newName

textShow = 'Young.Sheldon.S04E10.WEBRip.x264-ION10'
textMovie = 'Burrow.1978.vez.2.2020.1080p.WEB-DL.x264.AC3.HORiZON-ArtSubs.mp4'
textAnime = 'boku-no-hero-academia-51'
print(textShow.lower())
extension = textAnime.split('.')[-1]

extensions = ['srt','mp4','mkv','avi']
if extension not in extensions:
    extension = ''
        
print('extensao:' + str(extension))

newName = renameTvShow(textShow)
#newName = renameMovie(textMovie)
#newName = renameAnime(textAnime)
print(str('.')+str(sys.argv[0].split('.')[-1]))
print(sys.argv[0])
print('\\'.join(sys.argv[0].split('\\')[:-1])+str('\\')+str(newName)+str('.')+str(sys.argv[0].split('\\')[-1].split('.')[-1]))