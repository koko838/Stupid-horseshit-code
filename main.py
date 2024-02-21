import math
def function(a, b, c):
    raiz0 = b**2 - (4 * a * c)
    if raiz0 < 0:
        print("There´s no real answer")
    else:
        print("x = " + str((-b + math.sqrt(raiz0))/(2 * a)))
        print("x = " + str((-b - math.sqrt(raiz0))/(2 * a)))
function(float(input("a = ")), float(input("b = ")), float(input("c = ")))
    


                            
            
           