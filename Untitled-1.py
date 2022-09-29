


from lib2to3.pgen2.token import GREATER


def great_num(x,y):
    if x > y:
        print("{}".format(x) + " is GREATER than " + "{}".format(y))
    else:
        print("{}".format(y) + " is GREATER than " + "{}".format(x))


great_num(3,6)