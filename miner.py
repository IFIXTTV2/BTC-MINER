import time 
import random
import string 
from colorama import init, Fore
init(convert=True)

LicenseKey = input('Clé de liscence: \n ')
print(Fore.CYAN + "Vérification... ")
time.sleep(3)
print(Fore.GREEN + "Clé Valide ")
time.sleep(1)
Wallet = input("Wallet: \n")
print(Fore.CYAN + "Vérification... \n ")
time.sleep(3)
print(Fore.GREEN + "Wallet Trouver! \n")
time.sleep(4)
print(Fore.RED + "Création de votre espace de minage en cours... \n")
time.sleep(5)

def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

tries = 0

while(True):
    if(tries > random.randint(1000, 1000000000000)): # changer la proba
            print(Fore.CYAN + "[-]" + Fore.RED + id_gen() + Fore.GREEN + "| Hash Valide " + "0.00354 BTC")
            print(Fore.GREEN + "Ajout a votre wallet")
            time.sleep(10)
            tries = 0
            print (Fore.GREEN + "Réussi!")
            time.sleep(1)
    else:
            print(Fore.CYAN + "[-]" + id_gen() + Fore.YELLOW + "| Hash Invalide")
            tries += 1
