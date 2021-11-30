import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pics_extraction.flickr_extraction import image_from_url


def afficher(images):
    """Prends en argument une liste de 16 url d'images
    Affiche une mosaique de ces 16 images (sous forme 4*4)

    Args:
        images (liste): liste d'url d'images 
    """
    fig = plt.figure(figsize=(15*1.74, 15))
    for i in range(len(images)):
        img = image_from_url(images[i]) # on obtient l'image à partir de son url
        fig.add_subplot(4, 4, i+1)
        plt.axis('off') # n'affiche pas les axes
        plt.imshow(img)
    fig.subplots_adjust(wspace=0, hspace=0) # l'écart vertical et horizontal entre les images est nul
    plt.show()


if __name__ == "__main__":  # test
    url = 'https://live.staticflickr.com/65535/50608285403_36517dbe81_o.jpg'
    images = [url] * 16
    afficher(images)
