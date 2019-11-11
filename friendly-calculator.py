#Analyzes 2 inputs and shows all the computations you can do with it
#Could be expanded to include area and circumferences, distance between eachother on a graph, etc.
#Problems so far: the 2nd part of the division function doesn't display the full decimal. 

class AnythingCalculator:
    def __init__(self):
        self.pi = 3.14159265359
        self.number_1 = input('What is the first number?: ')
        self.number_2 = input('What is the second number?: ')

        try:
            self.number_1 = int(self.number_1)
        except:
            print("The first number is not a valid integer")
            return

        try:
            self.number_2 = int(self.number_2)
        except:
            print("The second number is not a valid integer")
            return

    def addition(self):
        print("If you added {0} and {1} you would get ...".format(self.number_1, self.number_2))
        print(self.number_1 + self.number_2)
        print("")

    def subtraction(self):
        print("If you subtracted {0} from {1} you would get ...".format(self.number_1, self.number_2))
        print(self.number_1 - self.number_2)
        print("")
        print("If you subtracted {0} from {1} you would get ...".format(self.number_2, self.number_1))
        print(self.number_2 - self.number_1)
        print("")

    def multiplication(self):
        print("If you multiplied {0} and {1} you would get ...".format(self.number_1, self.number_2))
        print(self.number_1 * self.number_2)
        print("")

    def division(self):
        print("If you divide {0} by {1} you would get ...".format(self.number_1, self.number_2))
        print(self.number_1 / self.number_2)
        print("")
        print("If you divide {0} by {1} you would get ...".format(self.number_2, self.number_1))
        print(self.number_2 / self.number_1)
        print("")

    def exponents(self):
        print("If you squared {0}, you would get...".format(self.number_1))
        print(self.number_1**2)
        print("")
        print("If you squared {0}".format(self.number_2))
        print(self.number_2**2)
        print("")
        print("If {0} was the base, and {1} was the exponent, you would get...".format(self.number_1, self.number_2))
        print(self.number_1** self.number_2)
        print("")
        print("If {0} was the base, and {1} was the exponent, you would get...".format(self.number_2, self.number_1))
        print(self.number_2** self.number_1)
        print("")

    def area(self):
        print("If {0} and {1} were the length and width of a rectangle, the perimeter of that rectangle would be...")
        print((self.number_1 + self.number_2)*2)
        print("")
        print("If {0} and {1} were the base and height of a triangle, the area of that triangle would be...")
        print((self.number_1 * self.number_2)/2)
        print("")
        print("If {0} was the radius of a circle, that circle would have an area of...")
        print(self.pi * (self.number_1 ** 2))
        print("")
        print("If {0} was the radius of a circle, that circle would have an area of...".format(self.number_2))
        print(self.pi * (self.number_2 ** 2))
        print("")
        print("If {0} was the radius of a circle, that circle would have an circumference of...".format(self.number_1))
        print(2 * self.pi * self.number_1)
        print("")
        print("If {0} was the radius of a circle, that circle would have an circumference of...".format(self.number_2))
        print(2 * self.pi * self.number_2)
        print("")

    def modulus(self):
        print("If you modulo {0} by {1} you would get ...".format(self.number_1, self.number_2))
        print(self.number_1 % self.number_2)
        print("")
        print("If you modulo {0} by {1} you would get ...".format(self.number_2, self.number_1))
        print(self.number_2 % self.number_1)
        print("")

calc = AnythingCalculator()
calc.addition()
calc.subtraction()
calc.division()
calc.exponents()
calc.area()
calc.modulus()

print('Interesting.')