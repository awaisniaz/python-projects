import numpy as np
a = np.array([34,5,89,23,76])

def sortarray(array,seq=""):
    for i in range(len(array)):
        for j in range(len(array)):
            if(seq == "as"):
                if array[i] < array[j]:
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
            else:
                if array[j] < array[j]:
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp

    print(array,"as")

sortarray(a,"as")