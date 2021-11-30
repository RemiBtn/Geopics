from textblob import TextBlob  # importation de "l'analyseur" de texte
import sys


def get_adjectives(text):
    """retourne les adjectifs présents dans text (qui est sous forme de TextBlob)

    Args:
        text (TextBlob): Un texte sous forme TextBlob

    Returns:
        liste: liste des adjectifs présents dans text 
    """
    return [word for (word, tag) in text.tags if tag == "JJ"]


def get_key_words(l):
    """Prends en argument une liste l de chaînes de caractères
    Retourne un dictionnaire avec comme clés les noms et adjectifs présents dans les chaînes de caractères
    et comme valeurs la fréquence de ces mots dans l'ensemble des chaînes de caractères

    Args:
        l (liste de chaîne de caractères): Correspond aux textes de tweets 

    Returns:
        Dictionnaire : contient les noms et adjectifs en clés et leur fréquence respective en valeurs
    """
    dic = {}
    mots_interdits = ['rt', 'le', 'la', 'les', 'de', 'du', 'un', 'une', 'des', 'je', 'j ’ ai', 'il', 'elle', 'nous', 'vous', 'ils', 'elles', 'I', 'i', 'm', ' ’', 'of', '’ s',
                      'a', 's', 'suis', 'est', 'sommes', 'sont', 'sera', 'seront', 'était', 'étaient', '\' ve', '\' m', '’ ve', '’ m', 'pour', 'que', '+', '-', 'en', 'aux']
    # on fait une liste de mots interdits
    for texte in l:
        text = TextBlob(texte)
        words = text.noun_phrases + get_adjectives(text)
        for word in words:
            if (word.lemmatize() not in mots_interdits) and not(word.startswith('@')):
                dic[word.lemmatize()] = dic.get(word.lemmatize(), 0) + 1
    # S'il n'y a pas assez de mots clés, le lieu choisi ne peut pas être traité et on termine le programme
    if len(dic) < 8:
        print('Veuillez écrire un nom de lieu valable')
        sys.exit(1)  # permet l'arrêt du programme
    return dic


if __name__ == "__main__":  # test
    location = 'paris'

    l = ['paris is magical and magical', 'paris is so magical or beautiful',
         'paris is beautiful and extremely dirty']
    t = TextBlob('Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human (natural) languages.')

    print(get_adjectives(t))
    for k in range(3):
        print(get_adjectives(TextBlob(l[k])))

    print(get_key_words(location, l))


def reduction_dico(l, nb_keywords):
    """Renvoie le dictionnaire obtenu avec get_key_words avec nb_keywords mots et leur nombre
    d'apparitions, correspondant aux mots les plus fréquents

    Args:
        l (liste de chaîne de caractères): Correspond aux textes des tweets
        nb_keywords (entier): Nombre de mots-clefs qu'on veut avoir

    Returns:
        Dictionnaire : dictionnaire contenant les mots les plus fréquents et leurs fréquence
    """
    Dict = get_key_words(l)  # on prend le résultat de get_key_words
    sortedDict = sorted(Dict.items(), key=lambda x: x[1], reverse=True)
    # on "trie" le dictionnaire obtenu en une liste de tuples
    # La première valeur du tuple est le mot, la seconde son nombre d'apparitions
    # x[1] signifie que l'on trie selon le nombre d'apparitions
    # reverse permet un tri par ordre décroissant

    dico_reduit = {}  # on crée un dictionnaire vide
    i = 0
    while len(dico_reduit) < nb_keywords:
        # tant que le dictionnaire ne contient pas nb_keywords mots
        dico_reduit[sortedDict[i][0]] = sortedDict[i][1]
        # on lui rajoute le mot le plus fréquent (pas encore ajouté) et son nombre d'apparitions
        i += 1
    return dico_reduit


# print(reduction_dico(location, l, 2))
