

def afficher_Colonnes(rows = 5):
    for i in range(rows, -1, -1):
        
        for line in range(0, i+1):
            print(line, end='')
        print("\r")

afficher_Colonnes(5)