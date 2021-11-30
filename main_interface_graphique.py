import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tweet_collection.collect import get_tweets
from tweet_analysis.key_words import get_key_words, reduction_dico
from pics_extraction.get_infos_images import get_dict, extract_url_dict
from display.interface_graphique import affichage_interface
from display.ttk_config import config_style


def lancement():
    '''Cette fonction lance la récupération des mots clés, des images et affiche le resultat'''
    lieu = ent_var.get() # on prend l'argument entré vie l'interface
    window.destroy()
    nb_tweets = 20
    nb_pics_par_keyword = [6, 4, 3, 3]
    # liste contenant les textes des tweets mentionnant le lieu
    tweets = get_tweets(lieu, nb_tweets)
    # on récupère les mots clés à partir de cette liste
    nb_keyword = len(nb_pics_par_keyword)*3
    keywords = reduction_dico(tweets, nb_keyword)
    # on extrait les URL des images associées aux mots clés
    url, compteur, img_keywords = [], 0, []
    # pour chaque mot clef, on cherche les urls des images associées
    for keyword in keywords:
        new_urls = extract_url_dict(keyword, nb_pics_par_keyword[compteur])
        # le système de compteur permet d'aller chercher des mots clés supplémentaire (les suivants dans la liste) si les premiers n'obtiennent pas d'image
        if new_urls and compteur < len(nb_pics_par_keyword):
            url.extend(new_urls)
            img_keywords.extend([keyword]*nb_pics_par_keyword[compteur])
            compteur += 1
        if compteur == len(nb_pics_par_keyword):
            break
    if compteur == len(nb_pics_par_keyword): # si on obtient assez de photo, on l'affiche
        affichage_interface(url, img_keywords)
    else:
        print('Nous n\'avons pas trouvé assez d\'images pour votre lieu. Veuillez réessayer avec un autre lieu s\'il vous plaît')


window = tk.Tk()
window.title("Geopics")
config_style()
first_frame = ttk.Frame(window)
first_label = ttk.Label(
    first_frame, text="Choisissez votre lieu", anchor="center", width=21)
ent_var = tk.StringVar()
entree = ttk.Entry(first_frame, textvariable=ent_var, width=15) # notre entrée
first_button = ttk.Button(first_frame, text="C'est parti", command=lancement)  # le button permettant d'appeler la fonction lancement
first_label.grid(row=0, column=0, pady=1)
first_frame.pack()
entree.grid(row=1, column=0, pady=3)
entree.focus_set()
first_button.grid(row=2, column=0, pady=3)
window.mainloop()
