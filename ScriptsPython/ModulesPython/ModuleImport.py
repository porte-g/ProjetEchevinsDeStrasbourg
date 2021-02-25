#coding:utf-8

from pathlib import Path

def ImportTXT(NomFichier):
    Repertoire = Path("../Sources/EditionsTXT/")
    DocumentTXT = Repertoire / NomFichier
    SourceTXT = open(DocumentTXT)
    print(SourceTXT.read())

def foo():
    print ("foo!")
