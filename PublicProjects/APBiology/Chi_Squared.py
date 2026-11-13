#Chi-square for AP Bio 
#X^2 = Σ(((o-e)^2)/e) 

classamount = int(input("How many classes? ")) 

degree_of_freedom = classamount - 1

classes = []

for i in range(classamount):
    # Stores all attributes of one data point to a tuple which is then added to a list
    one = input("Class name: ")
    two = float(input("Observed: "))
    three = float(input("Expected: "))
    instance = tuple([one, two, three])
    classes.append(instance)

print(classes)

#Changes the tuple into a dictionary that can then call values that were stored
tupletodic = {
    a: {
    "o_value": b, "e_value" : c}
     for a,b,c in classes
    }

#X^2 = Σ(((o-e)^2)/e)

summation = []

for tup in tupletodic:
    # Shows all necessary steps (Mostly if test questions ask to show work)
    o = tupletodic[tup]["o_value"] 
    e = tupletodic[tup]["e_value"] 
    sigma = ((o-e)**2)/e 
    print("for class " + tup + ":") 
    print("o-e = " + str(o-e)) 
    print("(o-e)^2 = " + str((o-e)**2))
    print("((o-e)^2)/e = " + str(((o-e)**2)/e))
    summation.append(sigma) 

reduced = sum(summation)
print("X^2 = " + str(reduced))

p_value = { 
    1 : { 
        "0.05" : "3.84", 
        "0.01" : "6.63" 
    },

    2 : { 
        "0.05" : "5.99" ,
        "0.01" : "9.21" 
    }, 

    3 : { 
        "0.05" : "7.81" ,
        "0.01" : "11.34" 
    },

    4 : { 
        "0.05" : "9.49",
        "0.01" : "13.28" 
    },

    5 : { 
        "0.05" : "11.07",
        "0.01" : "15.09" 

    },

    6 : { 
        "0.05" : "12.59", 
        "0.01" : "16.81" 
    },

    7 : { 
        "0.05" : "14.07",
        "0.01" : "18.48" 
    },

    8 : {
        "0.05" : "15.51",
        "0.01" : "20.09" 
    }
}

p = float(p_value[degree_of_freedom]["0.05"])
print("critical value = " + str(p))
if p > reduced:
    print("Unable to reject null hypothesis")
elif p < reduced:
    print("Reject null hypothesis")