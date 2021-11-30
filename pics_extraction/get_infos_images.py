'''Ce programme permet de récupérer des infos sur les images'''
from pprint import pprint
import flickrapi
from pics_extraction.credentials_flickr import KEY, SECRET


def get_dict(keyword, nb_pics):
    """Prend en argument un mot clef et son nombre de photos associé.
     Renvoie une liste contenant les dictionnaires de chaque image

    Args:
        keyword (chaîne de caractères): Mot-clef dont on veut les photos associées
        nb_pics (entier): Correspond au nombre de photos renvoyées

    Returns:
        liste: Liste qui contient les dictionnaires correspondant à chaque image
    """
    flickr = flickrapi.FlickrAPI(KEY, SECRET, format='parsed-json')
    extras = 'url_c'  # on souhaite aussi récupérer l'url de l'image dans le dictionnaire
    result = flickr.photos.search(
        text=keyword, per_page=nb_pics*2, extras=extras, sort='relevance')  # tri par pertinence
    photos = result['photos']
    Liste = photos['photo']  # Liste de dictionnaires récupérés
    i = 0
    L = []
    try:
        while len(L) < nb_pics:  # on vérifie que les dictionnaires ont bien une url_c
            try:
                Liste[i]['url_c']  # Si c'est le cas (i.e pas d'erreur)
                L.append(Liste[i])  # on ajoute le dictionnaire à la liste
                i += 1
            except KeyError:
                i += 1
        return L
    except IndexError:
        return False


if __name__ == "__main__":  # test
    pprint(get_dict('Tour Eiffel', 3))


def extract_url_dict(keyword, nb_pics):
    """Prend en argument un mot clef et son nombre de photos associées. 
    Si la requête sur Flickr aboutit, renvoie une liste d'URL pour le mot clef rentré. 
    Sinon, renvoie une liste vide

    Args:
        keyword (chaîne de caractères): Mot-clef dont on veut les photos associées
        nb_pics (entier): Correspond au nombre de photos renvoyées

    Returns:
        liste: Liste d'url si la requête flickr aboutit, liste vide sinon
    """
    # on récupère la liste de dictionnaires
    Listedictionnaire = get_dict(keyword, nb_pics)
    if Listedictionnaire:  # si on n'obtient pas d'erreur avec get_dict
        L = []
        for dict in Listedictionnaire:
            L.append(dict['url_c'])  # on récupère les url
        return L
    else:  # si on a eu une erreur, on renvoie un message
        print('Le mot clef {} n\'avait pas d\'image correspondante'.format(keyword))
        return []


if __name__ == "__main__":  # test
    print(extract_url_dict('Tour Eiffel', 5))
