import keyboard
import os
import time

# Fonction pour mettre l'ordinateur en veille
def mettre_en_veille():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# Drapeau pour indiquer s'il y a eu une activité du clavier
activite_clavier = False
derniere_activite = time.time()

# Fonction de rappel pour détecter l'activité clavier
def detecter_activite_clavier(event):
    global activite_clavier, derniere_activite
    activite_clavier = True
    derniere_activite = time.time()

# Enregistrer la fonction de rappel pour l'activité clavier
keyboard.on_press(detecter_activite_clavier)

try:
    while True:
        # Vérifier s'il y a eu une activité du clavier
        if activite_clavier:
            activite_clavier = False  # Réinitialiser le drapeau
            derniere_activite = time.time()

        # Vérifier si le délai de 2 minutes est écoulé sans activité
        if time.time() - derniere_activite > 120:
            print("ANTI-CHOCOBLAST ! Pas de pain au raisin pour Manu !!!!")
            mettre_en_veille()  # Mettre en veille si aucun activité détectée
            derniere_activite = time.time()

        time.sleep(1)  # Garder le script en cours d'exécution
except KeyboardInterrupt: 
    keyboard.unhook_all()  # Désenregistrer tous les hooks de clavier
