#Challenges Chapter 4

#Challenge 1

def squared(x):
    """
    Returns x squared
    :param x: int
    :return: int x squared
    """
    return x**2

print(squared(2))

#Challenge 2

def print_str():
    """
    Asks user for string & prints
    """
    y = input("Please write some words: ")
    print(y)
    return()

print_str()

#Challenge 3

def test(a,b,c,d=0,f=1):
    """
    Returns addition a+b+c+d+f
    :param a: int
    :param b: int
    :param c: int
    :param d: int (optional)
    :param f: int (optional)
    :returns nothing
    """
    return(a+b+c+d+f)

print(test(1,2,3))

#Challenge 4

def test_function(varInt):
    """
    Returns varInt divided by 2
    :param varInt: int
    :return: varInt divided 2
    """
    return(varInt/2)

def test_function_2(varInt2):
    """
    Returns varInt2 * 4
    :param varInt2: int.
    :return: int VarInt 2 multiplied by 4.
    """
    return(varInt2*4)

g = 2

print(test_function_2((test_function(g))))

#Challenge 5
def function_string_to_float(x):
    try:
        return(float(x))
    except ValueError:
        print("needs to be a number")

c=function_string_to_float("55.0")
print(c)
