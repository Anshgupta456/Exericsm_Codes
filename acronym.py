def abbreviate(words):
    sentence = words
    var = sentence[0]
    for idx, val in enumerate(sentence):
        if val in [" ", "-","_"]:
            ind = sentence[idx+1]
            if ind in [" ", "-","_"]:
                continue
            else:
                var += ind
    return (var.upper())
