from collections import Counter
def characterCounter(words):
    string = [word for word in words]
    print(Counter(string))
characterCounter("TheCleverProgrammer")
    