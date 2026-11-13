# A program that stores vectors with modifiable numbers of components and uses them to perform calculus-based arithmetic
# Eventually the program will be adapted for a TI-84 Python Plus calculator

# Creates a basic memory for the instance
vectorlist = []
pointlist = []
lower_alphabet = "abcdefghijklmnopqrstuvwxyz"

# Defines a point in space by its number of components and values of the components
class point():

    def __init__(self, components):
        self.components = components
        self.compnum = len(components)

    # Prints the components of a point in conventional (x,y,z) format
    def __str__(self):
        return "(" + str(self.components) + ")"    

# Creates a new instance of a point with a user input number of components
def new_point():
    component_number = int(input("Number of components? "))
    comps = []
    # Appends the component values to an ordered list of coordinates
    for c in range(0, component_number):
        comps.append(int(input("component value? ")))
    # Transforms the list of components into a tuple and adds the tuple to the instance's memory
    comps = tuple(comps)
    pointlist.append(point(comps))
    # Outputs the point for use when new_point() is called in another function
    return(tuple(comps))

# Prints all points in the instance's memory in the format [number in the list]. [point]
# For example: 1. (3,9,7) \n 2. (4,7,5)
def show_points():
    listnum = 0
    for v in pointlist:
        listnum += 1
        print(str(listnum) + ". " + str(v))

# Prompts user to select a point by inputting the corresponding number in show_points()
def select_point():
    listnum = 0
    for v in pointlist:
        listnum += 1
        print(str(listnum) + ". " + str(v))
    pchoice = int(input("Which point? (Or 0 to exit) "))
    while True:
        # Verifies the input is a valid number on the list of points
        try:
            pointlist[pchoice-1]
            break
        except:
            if pchoice != 0:
                print("Invalid choice! ")
                pchoice = int(input("Which point? (Or 0 to exit) "))
            elif pchoice == 0:
                break
    return pointlist[pchoice-1]

# Defines a vector by its number of components and values of the components
class vector():

    def __init__(self, components):
        self.components = components
        self.compnum = len(components)

    # Prints the vector in conventional <x,y,z> format
    def __str__(self):
        return "<" + str(self.components) + ">"


    # Takes an input scalar, s, and multiplies it with a selected vector <x,y,z> with the equation:
    # s * <x,y,z> = <s*x, s*y, s*z>

    def scalar_multiply(self):
        newvec = []
        scalar = int(input("Scalar value? "))
        for c in self.components:
            newvec.append(c * scalar)
        # Prints the resulting vector
        print(vector(tuple(newvec)))
        # Appends the resulting vector to the local memory
        return vector(tuple(newvec))

    # Takes a vector as an arguement and returns the magnitude of that vector
    def magnitude(self):
        total = 0
        for c in self.components:
            total += c**2
        print("Magnitude = sqrt(" + str(total) + ")")
        return total**1/2

    # Divides all components of a selected vector by the vector's magnitude. Returns the unit vector for selected vector.
    def unit_vector(self):
        mag = self.magnitude()
        unitvec = []
        for c in self.components:
            unitvec.append(float(c/mag))
        print(vector(tuple(unitvec)))
        return vector(tuple(unitvec))

    # Adds correlating components of two vectors (v1, v2) and returns the resulting vector.
    def add_vectors(self, other):
        newcomps = []
        # Checks if v1 has a greater number of components than v2.
        if self.compnum > other.compnum:
            longcompnum = self.compnum
        # If previous line passes, assumes # of components in v2 has to be greater than or equal to v1.
        else:
            longcompnum = other.compnum
        # Attempts to add corresponding components of v1 and v2
        for c in range(0, longcompnum):
            try:
                newcomps.append(self.components[c] + other.components[c])
        # If raw addition fails, checks which vector has lesser components and treats missing components as 0
        # Addition by zero is arbitrary but is added to show how the program is adjusting
            except:
                if self.compnum > other.compnum:
                    newcomps.append(self.compnum + 0)
                elif self.compnum < other.compnum:
                    newcomps.append(other.compnum + 0)
        newvec = vector(tuple(newcomps))
        vectorlist.append(newvec)
        print(str(newvec))

    # Computes the dot product of two vectors 
    # If u = <x1, y1, z1> and v = <x2, y2, z2>
    # Then u *dot* v = (x1)*(x2) + (y1)*(y2) + (z1)*(z2)
    def component_dot_product(self, other):
        product = 0
        # Checks if vectors have equal number of components
        try:
            self.compnum == other.compnum
        # Ends function and returns error message if components are not equal
        except:
            return("Vectors have differing number of terms ")
        # Multiplies corresponding components together and += them to a variable
        for c in range(0, self.compnum):
            product += (self.components[c] * other.components[c])
            print("The dot product is " + str(product))
        return product

    # Computes the cross product of two three component vectors 
    # If u = <u1, u2, u3> and v = <v1, v2, v3>
    # Then u x v = <u2*v3 - u3*v2, u3*v1 - u1*v3, u1*v2 - u2*v1>
    def cross_product(self, other):
        try:
            self.compnum == other.compnum
        except:
            return("Vectors have differing number of terms ")

        #Assigns all components to a variable in the equation
        u1 = self.components[0]
        u2 = self.components[1]
        u3 = self.components[2]
        v1 = other.components[0]
        v2 = other.components[1]
        v3 = other.components[2]

        x = (u2 * v3) - (u3 * v2)
        y = (u3 * v1) - (u1 * v3)
        z = (u1 * v2) - (u2 * v1)

        new_comps = [x,y,z]
        # Creates a new vector object with the cross product's result
        cross_prod_vec = vector(tuple(new_comps))
        print("The cross product is " + str(cross_prod_vec))
        return(cross_prod_vec)


    # Quick, unoptimized function that converts a vector with a reasonable number of components into a equation in coordinate vector form
    # For example, if the vector is <1,2,3>, then the function returns 1i + 2j + 3k
    def decompose_to_coordinate(self):
        print("Coordinate vector form:")
        alpha_iter = 8
        for c in self.components:
            print(lower_alphabet[alpha_iter] + str(c))
            alpha_iter += 1

    # Calculates the distance between a line and a point
    # Let d be distance, v the direction vector for the line, and PQ the vector from a point on v, P, to the targeted point Q. Then:
    # d = magnitude(v x PQ) / magnitude(v)
    # Requires user to find the vector PQ
    def distance_to_point(self, point):
        print("Input vector to the point: ")
        point = new_vector()

        crossprod = self.cross_product(point)
        return(crossprod.magnitude()/point.magnitude)
        

# Creates a new instance of a vector with a user input number of components
def new_vector():
    component_number = int(input("Number of components? "))
    comps = []
    for c in range(0, component_number):
        comps.append(int(input("component value? ")))
    comps = tuple(comps)
    return(vector(comps))

# Prints all vectors in the instance's memory in the format [number in the list]. [point]
# For example: 1. <6,8,2> \n 2. <5,1,3>
def show_vectors():
    listnum = 0
    for v in vectorlist:
        listnum += 1
        print(str(listnum) + ". " + str(v))

# Prompts user to select a vector by inputting the corresponding number in show_vectors()
def select_vector():
    listnum = 0
    for v in vectorlist:
        listnum += 1
        print(str(listnum) + ". " + str(v))
    vchoice = int(input("Which vector? (Or 0 to exit) "))
    # Verifies the input is a valid number on the list of points
    while True:
        try:
            vectorlist[vchoice-1]
            break
        except:
            if vchoice != 0:
                print("Invalid choice! ")
                vchoice = int(input("Which vector? (Or 0 to exit) "))
            elif vchoice == 0:
                break
    return vectorlist[vchoice-1]

# A basic menu to navigate the program's funtions
def print_menu1():
    print("Press 1 to create a new vector")
    print("Press 2 to show current vectors")
    print("Press 3 to multiply a vector by a scalar")
    print("Press 4 to calculate magnitude of a vector")
    print("Press 9 to see more options")
    print("Or 0 to exit")

def print_menu2():
    print("Press 1 to calculate a unit vector")
    print("Press 2 to add two vectors")
    print("Press 3 to find a dot product")
    print("Press 4 to find a cross product")
    print("Press 9 to see more options")
    print("Or 0 to exit")

#The true/false work as toggles for the two menus that are altered when an input of 9 is recieved
menu1 = True
menu2 = False

# Prints the 1st menu on start-up
print_menu1()

while True:
    menu_choice = input("Input the number of an option then hit enter. ")
    if menu1 == True:
        if menu_choice == "1":
            vectorlist.append(new_vector())
        elif menu_choice == "2":
            show_vectors()
        elif menu_choice == "3":
            select_vector().scalar_multiply()
        elif menu_choice == "4":
            select_vector().magnitude()

    if menu2 == True:
        if menu_choice == "1":
            select_vector().unit_vector()
        elif menu_choice == "2":
            select_vector().add_vectors(select_vector())
        elif menu_choice == "3":
            print(str(select_vector().component_dot_product(select_vector())))
        elif menu_choice == "4":
            print(str(select_vector().cross_product(select_vector())))

    # Changes menus by inverting true/false state of menu 1 and menu 2 for the next loop iteration
    if menu_choice == "9":
        if menu1 == True:
            print_menu2()
            menu1 = False
            menu2 = True
        elif menu2 == True:
            print_menu1()
            menu2 = False
            menu1 = True
    elif menu_choice == "0":
            break
