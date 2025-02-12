def get_multiple_6():
    """
    Returns a multiple of 6 that was entered by the user.
    :return: isnt a number
    """

    while True:
        try:
            n = input("Please give me a multuple of 6: ")
            n = int(n) # convert to int
            # how to check if it is a multiple of 6?
            #if n % 6 == 0:
                #return n
            # another way to check
            if n / 6 == n//6:
                return n
            else:
                print("that is not a multiple of 6")
        except ValueError:
            print("You have not entered a number")

print(get_multiple_6())