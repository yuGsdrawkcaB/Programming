#Solute Potential = -iCRT 

# i = ionization constant 

# C = Molar concentration 

# R = Pressure constant (0.0831 liter bars/mole K) 

# T = Temperature in degrees K (273 + degrees C of solution) 

 

common_i = {
    "sucrose" : 1.0, 
    "NaCl" : 2.0,  
} 

 

print(common_i) 

i = float(input("Ionization constant(i)? ")) 

C = float(input("Molar concentration(C)? ")) 

R = 0.0831 

print("R is constant (0.0831)") 

Temp = input("Temperature: Press 1 for Kelvin or 2 for Celcius: ") 

T = float(input("Temperature(T)? ")) 

if Temp == "2": 
    Tval = (f"({str(T)} +  273)") 

else: 
    Tval = T 

if Temp == "2": 
    T += 273 

math = i * C * R * T 

print("Solute Potential = -iCRT") 
print(f"{i} * {C} * {R} * {Tval}") 
print(f"-{math} bars") 