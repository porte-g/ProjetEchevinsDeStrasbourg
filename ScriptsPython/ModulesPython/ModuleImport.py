#coding:utf-8

from pathlib import Path

def ImportTXT(NomFichier):
    RepertoireTXT = Path("../Sources/EditionsTXT/")
    DocumentTXT = RepertoireTXT / NomFichier
    SourceTXT = open(DocumentTXT)
    print(SourceTXT.read())

def ImportTEI(NomFichier):
    RepertoireTEI = Path("../Sources/EditionsXML/")
    DocumentTEI = RepertoireTEI / NomFichier
    SourceTEI = open(DocumentTEI)
    print(SourceTEI.read())
