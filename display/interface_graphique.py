import tkinter as tk
from PIL import Image, ImageTk
from pics_extraction.flickr_extraction import image_from_url
from display.reshape_image import change_taille


def affichage_interface(urls, keywords):
    """Crée la fenêtre qui affiche les images et permet l'interaction avec l'utilisateur

    Args:
        urls (liste): contient les urls qui pointent sur les images à afficher
        keywords (liste): contient le mot clef affiché à chaque image
    """

    fenetre = tk.Tk()

    def get_coords():
        """Renvoie les coordonnées (x,y) du curseur de la souris s'il est sur une des images

        Returns:
            tuple: renvoie (True, x, y) si la souris est sur une image et (False, None, None) sinon
        """

        if state_image[0]:
            return True, fenetre.winfo_pointerx() - fenetre.winfo_rootx(), fenetre.winfo_pointery() - \
                fenetre.winfo_rooty()
        else:
            return False, None, None

    def on_image(event):
        """Change le statue de state_image lorsque l'on entre sur une image"""
        state_image[0] = True

    def out_image(event):
        """Change le statue de state_image lorsque l'on sort d'une une image"""
        state_image[0] = False

    def motion():
        """Inverse l'image par son keyword en rentrant sur une nouvelle image et rétablit l'image dont on vient de sortir"""

        state, x, y = get_coords()
        if state:  # on se trouve bien sur la fenetre
            row_img, column_img = y//IMAGE_SIZE, x//IMAGE_SIZE
            indice_image = column_img + 4*row_img
            # si l'image est différente de celle enregistrée au step d'avant, on efface
            # l'image et on affiche son mot clef
            if current_image[0] != indice_image and 0 <= indice_image <= 15:
                display_keyword(row_img, column_img)
                # cas particulier à l'initialisation (on a pas besoin d'afficher d'image)
                if current_image[0] != -1:
                    display_image(current_image[0]//4, current_image[0] % 4)
                current_image[0] = indice_image

    def display_keyword(row, column):
        """Efface l'image correspondant à la ligne et à la colonne données puis affiche son keyword à la place

        Args:
            row (int): ligne de l'image à effacer
            column (int): colonne de l'image à effacer
        """
        indice_image = column + 4*row
        if 0 <= indice_image <= 15:
            labels_images[indice_image].grid_forget()
            labels_keywords[indice_image].grid(row=row, column=column)

    def display_image(row, column):
        """Efface le label keyword correspondant à la ligne et à la colonne données puis affiche son image à la place

        Args:
            row (int): ligne du keyword à effacer
            column (int): colonne du keyword à effacer
        """
        indice_image = column + 4*row
        if 0 <= indice_image <= 15:
            labels_keywords[indice_image].grid_forget()
            labels_images[indice_image].grid(row=row, column=column)

    def step():
        '''Réinitialise la position et donc l'affichage du mot clef toutes les tant de ms'''
        motion()
        fenetre.after(10, step)

    IMAGE_SIZE = 150
    # on convertit les images dans un format compatible avec tkinter
    images = [ImageTk.PhotoImage(change_taille(
        image_from_url(link), IMAGE_SIZE)) for link in urls]
    labels_images = [tk.Label(fenetre, image=img)
                     for img in images]
    for i, label in enumerate(labels_images):
        label.grid(row=i//4, column=i % 4)
        # on associe l'entrée et la sortie d'image aux fonctions associées
        label.bind('<Enter>', on_image)
        label.bind('<Leave>', out_image)

    # liste qui contiendra le mot clef lorsque l'utilisateur passera sur une image
    text_labels, labels_keywords = [tk.StringVar() for i in range(16)], []
    for i in range(16):
        text_labels[i].set(keywords[i])
        labels_keywords.append(tk.Label(fenetre, textvariable=text_labels[i]))
        # même chose que pour les images
        labels_keywords[i].bind('<Enter>', on_image)
        labels_keywords[i].bind('<Leave>', out_image)

    # contient l'indice de l'image sur laquelle la souris se trouve en ce moment (sauf à l'initialisation)
    current_image = [-1]
    # contient False si l'on est pas sur une image et True sinon
    state_image = [False]
    step()
    fenetre.mainloop()


if __name__ == "__main__":
    affichage_interface(
        ['https://live.staticflickr.com/5246/5360100824_8ef1b2abb3.jpg']*16, ['test']*16)
