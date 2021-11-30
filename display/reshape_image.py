from PIL import Image


def change_taille(img, basewidth):
    """Cette fonction permet d'adapter l'image à la taille choisie

    Args:
        img (image au format jpeg): image que l'on veut modifier
        basewidth (float): taille à laquelle on veut adapter l'image
    """

    return img.resize((basewidth, basewidth), Image.ANTIALIAS)
