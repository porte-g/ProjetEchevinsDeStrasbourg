#coding:utf-8

def XmlTei_to_Dataframe(CheminRelatifFichier):
    
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(open(CheminRelatifFichier, 'r'))

    ListeDicosPersonnes = []

    for persname in soup.find_all('persname'):

        DicoPersonne = {}

        for surname in persname.find_all('surname'):
            DicoPersonne['nom'] = surname.get_text()

        for forename in persname.find_all('forename'):
            DicoPersonne['prénom'] = forename.get_text()

        for genname in persname.find_all('genname'):
            DicoPersonne['surnom'] = genname.get_text()

        Roles = []
        for rolename in persname.find_all('rolename'):
            Roles.append(rolename.get_text())
            DicoPersonne['fonction'] = Roles

        for div1 in persname.find_parents('div1'):
            DicoPersonne['corps civique'] = div1['type']

        for div2 in persname.find_parents('div2'):
            DicoPersonne['Corporation'] = div2['type']

        for div3 in persname.find_parents('div3'):
            DicoPersonne['Poêle'] = div3['type']       

        ListeDicosPersonnes.append(DicoPersonne)

    #return (ListeDicosPersonnes)
    import pandas as pd
    dataframe = pd.DataFrame(ListeDicosPersonnes)
    return(dataframe)
