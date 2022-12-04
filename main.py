import csv

#On ouvre le fichier qu'on doit trier
file = open('conso-annuelles_v1.csv', 'r',encoding='latin-1')
csvFile = csv.reader(file, delimiter=';')
List = []

#Suppression des lignes avec une colonne vide et de l'id Logement
for ligne in csvFile:
    if all(ligne):
        List.append(ligne)
        print("Suppression Ligne")
for colonneID in List:
    del colonneID[1]
    print("Suppression Colonne")


#On rajoute les tableaux ListFinal ainsi que ListSortie qui nous serons utile pour sortir le code
ListFinal = []
ListSortie = []

#On calcule Ligne 1+2
Lignes = True

for row in List:
    #on change les , en .
    row[1] = row[1].replace(',', '.')
    row[2] = row[2].replace(',', '.')
    if not Lignes:
        #On calcule
        try:
            calc = float(row[1]) + float(row[2])
            row.append(calc)
            ListSortie.append(row)
            print("Calcule Ligne")
            #Si erreur
        except:
            break
            print("Erreur Calcule")
    else:
        row.append('total des deux années')
        ListFinal.append(row)
        Lignes = False

#On exporte les données dans le fichier conso-clean.csv
with open('conso-clean.csv', 'w', newline='',encoding='latin-1') as files:
    writer = csv.writer(files, delimiter=';')
    for line in ListFinal:
        writer.writerow(line)
        for row in ListSortie:
            writer.writerow(row)
        break