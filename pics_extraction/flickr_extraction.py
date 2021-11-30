from pics_extraction.credentials_flickr import KEY, SECRET
from flickrapi import FlickrAPI
import requests  # to get image from the web
from PIL import Image
from io import BytesIO

FLICKR_PUBLIC = KEY
FLICKR_SECRET = SECRET


def flickr_setup():
    """Renvoie la connexion avec l'API de flickr

    Returns:
       Connexion avec l'API flickr 
    """
    return FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, cache=True)


def image_from_url(image_url):
    """Prend en argument l'url d'une image et renvoie l'image associée

    Args:
        image_url (chaîne de caractères): correspond à l'url d'une image

    Returns:
        Image :  Affichage de l'image correspondant à l'url 
    """
    r = requests.get(image_url, stream=True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        return Image.open(BytesIO(r.content))
    else:
        print("L'image de l'url {} n'est pas disponible".format(image_url))
        r = requests.get(
            'https://live.staticflickr.com/5246/5360100824_8ef1b2abb3.jpg', stream=True)
        # image error 404
        r.raw.decode_content = True
        return Image.open(BytesIO(r.content))


if __name__ == "__main__":
    print(image_from_url(
        "https://live.staticflickr.com/65535/50608285403_36517dbe81_o.jpg"))
