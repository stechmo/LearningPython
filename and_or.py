#a = 200
#b = 33
#c = 500
#if a > b or a > c:
#    print("At least one of the conditions is True")
def printtruthtable(a):
    print(a(False,False))
    print(a(True,False))
    print(a(False,True))
    print(a(True,True))

def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return not a and b or a and not b

def XNOR(a, b):
    return not (not a and b or a and not b)

printtruthtable(XNOR)