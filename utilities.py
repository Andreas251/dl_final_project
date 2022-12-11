def cleanLine(text, pickle, re):
    file = open("preprocessing/bannedwords", 'rb')
    bannedwords = pickle.load(file)
    file.close()

    file = open("preprocessing/prereplacements", 'rb')
    replacements = pickle.load(file)
    file.close()

    file = open("preprocessing/postrep", 'rb')
    postreplacements = pickle.load(file)
    file.close()

    file = open("preprocessing/charstoclean", 'rb')
    charactersToClean = pickle.load(file)
    file.close()

    file = open("preprocessing/charstospace", 'rb')
    charactersToSpace = pickle.load(file)
    file.close()
    
    for x, y in replacements:
        text = text.lower()
        if x in text:
            text = text.replace(x, y)
    
    for char in charactersToClean:
        text = text.replace(char, "")

    for char in charactersToSpace:
        text = text.replace(char, " ")
 
    text = re.sub(r'[0-9]+', '', text)
    
    for x, y in postreplacements:
        text = text.lower()
        if x in text:
            text = text.replace(x, y)
            
    return text