import tkinter as tk
import keyboard
import subprocess
import time

# Fonction pour mettre l'ordinateur en veille
def mettre_en_veille():
    subprocess.Popen(["rundll32.exe", "user32.dll,LockWorkStation"])

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

# Fonction pour quitter le programme
def quitter():
    root.destroy()

# Fonction principale
def main():
    global activite_clavier, derniere_activite
    # Vérifier s'il y a eu une activité du clavier
    if activite_clavier:
        activite_clavier = False  # Réinitialiser le drapeau
        print("Clavier")
        derniere_activite = time.time()

    # Vérifier si le délai de 1 minute est écoulé sans activité
    if time.time() - derniere_activite > 60:
        print("ANTI-CHOCOBLAST ! Pas de pain au raisin pour Manu !!!!")
        mettre_en_veille()  # Mettre en veille si aucun activité détectée
        derniere_activite = time.time()
        root.destroy()

    root.after(1000, main)  # Appeler la fonction main() toutes les 1000 millisecondes

# Configuration de la fenêtre principale
root = tk.Tk()

# Obtenir la résolution de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculer les coordonnées pour placer la fenêtre en haut à droite de l'écran
x = screen_width - 300
y = 0

# Définir la géométrie de la fenêtre
root.geometry("150x80+{}+{}".format(x, y))

# Style personnalisé pour la fenêtre de dialogue
root.configure(bg="#f0f0f0")  # Couleur de fond
root.attributes("-topmost", True)  # Toujours afficher la fenêtre au-dessus des autres
root.overrideredirect(True)  # Supprimer la barre de titre et les bordures de la fenêtre

# Contenu de la fenêtre
quitter_button = tk.Button(root, text="Quitter", command=quitter, bg="#E4080A")
quitter_button.pack(pady=5)

# Lancer la boucle principale
root.after(1000, main)  # Démarrer la fonction main() toutes les 1 ms
root.mainloop()
