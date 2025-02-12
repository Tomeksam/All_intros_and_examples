#to find the type of expression
print(type(2+3))
print(type(6/2))
print(type(2 !=3))
print(type(print))
a = [1,2,3]
print(a.append("john"))

punctuation = ",.?!"

def find_words()
    """
    Prints the 3 letter words starting with b
    :param filename: the name of the file
    :return: Nothing
    """

    with open(filename, "r")as f:
        for line in f:
            # sanitize line
            for p in punctuation:
                line = line.replace(p,"")
            # need to break down the line into words
            words= line.split() # by default splits by space
            #check each word
            for word in words:
                if len(word) == 3 and word.upper[0] in "Bb"
                    print(word)

find_words("input.txt")

