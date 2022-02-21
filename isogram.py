def is_isogram(word=None):
    word = str(word).lower()
    list = ['a', "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p","q","r","s","t","u","v","w","x","y","z"]
    for i in word:
        if word.count(i) > 1 and i in list:
            return False
    return True
    