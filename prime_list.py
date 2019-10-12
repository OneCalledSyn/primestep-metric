#Reminder to optimize bounds later
prime_bank = {x for x in range(2, 10000) if all(x % y != 0 for y in range(2, x))}
print(len(prime_bank))

#Prints the list of available primes:
#print(sorted(prime_bank))

def primestep(a,b) :
    
    path_length = 0
    #max_prime = ?
    
    if a > b :
        return primestep(b,a)
        
    elif (a == b):
        return path_length

    elif (a+1 == b or a-1 == b):
        path_length += 1
        return (path_length)
    
    #fix condition to be boolean
    elif ((a*p == b) for p in prime_bank):
                path_length += 1
                return path_length
                
    else:
        print("I am not smart enough to code that yet.")
        
#def taylorbrainidea ():
    #Call on list of primes and check if a*p == b, if true go into third elif statement
        
#Call function here
print(primestep(2,6))
