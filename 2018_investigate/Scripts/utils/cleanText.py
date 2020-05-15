import re

# Remove datetime
def removeDatetime(inputList):
    newlist = []
    for text in inputList:
        newtext = re.sub('\d+年\d+月?\d+日?', '', text)
        newtext = re.sub('\d+时(\d+分)?许', '', newtext)
        newlist.append(newtext)
    return newlist


def removeNonChinese(inputList):
    newlist = []
    for text in inputList:
        newtext = re.sub('[a-zA-Z]+', '', text)
        newtext = re.sub('\d+', '', newtext)
        newtext = newtext.replace("/", '')
        newtext = newtext.replace("／", '')
        newlist.append(newtext)
    return newlist

def contentTextOnly(inputList):
    newList = removeDatetime(inputList)
    newList = removeNonChinese(newList)
    return newList