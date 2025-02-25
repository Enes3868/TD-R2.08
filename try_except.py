import random
liste = []
for i in range(random.randint(10,20)):
    liste.append(random.randint(0,100))

while True:
    try:
        index=int(input("donnez un index: "))
        second_nb=float(input("second nombre: "))
        print(f"valeur dans la liste: {liste[index]}")
        print(liste[index]/second_nb)
    except IndexError:
        print(f"erreur: l'index {index} est en dehors dde la liste ([-{len(liste)}; {len(liste)-1}])...")
    except ValueError:
        print(f"erreur: la valeur saisie doit etre un nombre..?")
    except ZeroDivisionError:
        print(f"erreur: le second nombre ne doit pas etre nul car il est au denominateur...")
    except Exception as e:
        print(type(e))