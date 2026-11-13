# Takes 4 letters representing alleles as arguements and returns a 2x2 punnett square for the alleles
# The program is designed for use on a TI-84 Python Plus calculator, so using pandas was not possible

# Example test case: A A A a for the four inputs

class genotype: 
    def __init__(self, a1, a2): 
        self.a1 = a1 
        self.a2 = a2 

    def __str__(self): 
        return self.a1 + self.a2 

         
# Determines if the first letter is capitalized, if not then returns the 2nd letter as the first.
def lettersort(letter1, letter2): 
        if letter2.upper() != letter2 and letter1.upper() == letter1: 
            return (letter1 + letter2) 
        else: 
            return (letter2 + letter1) 

         
# Makes the square diagram and sorts terms in each square by capitalization
def punnett_square(parent1, parent2): 
    print(str(parent1) + " + " + str(parent2)) 
    print("     " + parent1.a1 + "    " + parent1.a2 + "      ") 
    print("   ___________") 
    print(parent2.a1 + " | " + lettersort(parent1.a1, parent2.a1) + " |  " + lettersort(parent1.a2, parent2.a1) + " |") 
    print(parent2.a2 + " | " + lettersort(parent1.a1, parent2.a2) + " |  " + lettersort(parent1.a2, parent2.a2) + " |") 
    print("   ___________") 

genes = [] 
# Asks how many 2x2 squares to create
gene_num = int(input("Number of squares to be made? "))  

# Creates gene objects containing alleles that are safer to store and can be used in a larger, more complex program if ever needed.
loopnum = 0 
for g in range(gene_num): 
    print("gene " + str(loopnum)) 
    loopnum += 1 
    alpair = [] 
    for n in range(2): 
        A1 = input("Gene " + str(loopnum) + ", Allele 1? ")  
        A2 = input("Gene " + str(loopnum) + ", Allele 2? ") 
        alpair.append(genotype(A1, A2)) 
    genes.append([alpair[0], alpair[1]])  

for g in genes: 
    punnett_square(g[0], g[1])  