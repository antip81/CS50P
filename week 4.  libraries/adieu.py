# https://cs50.harvard.edu/python/2022/psets/4/adieu/

# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

def main():
    i = 0
    names = []

    # makes a list of names til ctrl+d is pressed
    while True:
        try:
            names.append(input("Name: "))
            i += 1
        except EOFError:
            break

    adieu_print(names)


def adieu_print(names: list):
    curr = ""

    # makes a string of names
    # if list[index] is the "last index - 1" -> separator = " and "
    # if list[index] is the "last index" -> no separator needed
    # else -> separator = ", "
    for k in range(0, int(len(names))):
        if k == int(len(names) - 2):
            separator = " and "
            curr = curr + "".join(names[k] + separator)
        elif k == int(len(names) - 1):
            curr = curr + "".join(names[k])
        else:
            separator = ", "
            curr = curr + "".join(names[k] + separator)

    print("Adieu, adieu, to " + curr)


if __name__ == '__main__':
    main()
