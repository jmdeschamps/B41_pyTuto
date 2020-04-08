def toto():
    return 12


print("dans testimport",__name__)

if __name__ == '__main__':
    n=toto()
    print("fIN DU MODULE TESTIMPORT", n)