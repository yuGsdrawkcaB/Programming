# Follows a flowchart method that prompts the user to perform a sequence of tests to prove convergence or divergence of a series.
# Flow chart used as a template is included in the file

print("For all prompts, 1 for yes or 0 for no") 
print("") 
while True: 
    q = input("Does lim n -> inf. a(n) = 0? ") 
    if q == "0":
        print("a(n) diverges") 
        break 
    elif q == "1": 
        pass 
     
    print("") 
    print("p-series test") 
    q = input("Does a(n) = 1/n^p , n => 1? ") 
    if q == "1": 
        q2 = input("Is p > 1?") 
        if q2 == "1": 
            print("E [a(n)] converges") 
        elif q2 == "0": 
            print("E [a(n)] diverges") 
        break 
    elif q == "0": 
        pass 
 
    print("") 
    print("geometric series test") 
    q = input("Does a(n) = a * (r)^n ? ") 
    if q == "1": 
        q2 = input("Is abs(r) < 1?") 
        if q2 == "1": 
            print("n=1 E inf [a(n)] = (a/1-r) or series conv. to a(r^k)/(1 - r)") 
        elif q2 == "0": 
            print("E [a(n)] diverges") 
        break 
    elif q == "0": 
        pass 
     
    print("") 
    print("alternating series test") 
    q = input("For ((-1)^n) * a(n), is a(n) positive, decreasing, and lim n -> inf. a(n) = 0? ") 
    if q == "1": 
        print("E [a(n)] converges") 
        break 
    elif q == "0": 
        pass 
     
    print("") 
    print("telescoping series test") 
    q = input("Can a(n) be changed into the form of one value subtracted from another? ") 
    if q == "1": 
        print("Write out terms and attempt to cancel") 
        q2 = input("For  lim n -> inf. s(n) = s, is s finite? ") 
        if q2 == "1": 
            print("E [a(n)] converges to s") 
        elif q2 == "0": 
            print("E [a(n)] diverges") 
        break 
    elif q == "0": 
        pass 
     
    print("") 
    print("comparison test") 
    comptest = False 
    while True: 
        q = input("Try comparison test? ") 
        if q == "1": 
            print("Pick b(n)") 
            q2 = input("Does E [b(n)] converge? ") 
            if q2 == "1": 
                q3 = input("Is 0 =< a(n) =< b(n)? ") 
                if q3 == "1": 
                    print("E [a(n)] converges") 
                    comptest = True 
                    break 
                elif q3 == "0": 
                    pass 
            if q2 == "1": 
                q3 = input("Is 0 =< b(n) =< a(n)? ") 
                if q3 == "1": 
                    print("E [a(n)] diverges") 
                    comptest = True 
                    break 
                elif q3 == "0": 
                    pass 
        elif q == "0": 
            break 
    if comptest == True: 
        break 
     
    print("") 
    print("limit comparison test") 
    limcomptest = False 
    while True: 
        q = input("Try limit comparison test? ") 
        if q == "1": 
            print("Pick b(n)") 
            input("Does lim n -> inf. a(n)/b(n) = c > 0 where c is finite?") 
            q3 = input("Does n=1 E inf. [b(n)] converge? ") 
            if q3 == "1": 
                print("E [a(n)] converges") 
                limcomptest = True 
                break 
            elif q3 == "0": 
                print("E [a(n)] diverges") 
                limcomptest = True 
                break 
        elif q == "0": 
            break 
    if limcomptest == True: 
        break 
  
    print("") 
    print("integral test") 
    q = input("Can the integral of a(n) from x to inf. be taken? ") 
    if q == "1": 
        print("If the integral converges, E [a(n)] converges. If the integral diverges, E [a(n)] diverges ") 
    elif q == "0": 
        pass 
     
    print("") 
    print("ratio test") 
    q = input("Is lim n -> inf. abs[a(n+1)/a(n)] != 1? ") 
    if q == "1": 
        q2 = input("Is lim n -> inf. abs[a(n+1)/a(n)] < 1? ") 
        if q2 == "1": 
            print("E [a(n)] converges absolutely") 
        elif q2 == "0": 
            print("E [a(n)] diverges") 
    elif q == "0": 
        pass 
     
    print("") 
    print("root test") 
    q = input("Is lim n -> inf. nthroot{abs[a(n)]} != 1? ") 
    if q == "1": 
        q2 = input("Is lim n -> inf. nthroot{abs[a(n)]} < 1? ") 
        if q2 == "1": 
            print("E [a(n)] converges absolutely") 
        elif q2 == "0": 
            print("E [a(n)] diverges") 
    elif q == "0": 
        pass 