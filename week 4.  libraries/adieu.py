# https://cs50.harvard.edu/python/2022/psets/4/adieu/

# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

def main():
    import inflect
    names: list[str] = []

    # makes a list of names til ctrl+d is pressed
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break

    # uses iflect join method to make a string
    p = inflect.engine()
    print("Adieu, adieu, to " + p.join((names)))


if __name__ == '__main__':
    main()
