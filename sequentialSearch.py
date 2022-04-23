def findSearch(WORD):
    array = ["Awais niaz","Usman Niaz","Tayyab Niaz",""]
    for i in array:
        if i == WORD:
            return True


    return False

print(findSearch("Awais niaz"))