#Conjecture: For any b in metric space (N,d), <a,b> will never need any prime greater than the smallest prime > (a and b) 
#Verdict: Original conjecture is false

#Result: <1,405>, <1,495>, <1, 783>, and <1, 891> are counterexamples for dividing by 2 under 1000; under 2000: <1, 1269>, <1, 1377>, <1, 1395>, <1, 1444>, <1, 1917>, and <1, 1925>; under 3000: <1, 2511>, <1, 2781>, <1, 2871>, and <1, 2875>
#        No counterexamples for dividing by 3 under 3000
#        No counterexamples for dividing by 5 under 1000, under 2000: <1, 1024> and <1, 1444>
#        No counterexamples for dividing by 7 under 1000

import math
#Change brackets to curly braces to switch from list to set
big_prime_bank = [x for x in range(2, 18000) if all(x % y != 0 for y in range(2, int(math.floor(x**0.5))+1))]

filtered_bank = filter(lambda x: x > 9000, big_prime_bank)

#print(len(big_prime_bank))
#print (big_prime_bank)

#Counterexample search function: Take all primes in bank, add/subtract by 1, divide by every prime in the bank, return only and all integers


adj_primes = [x+1 for x in filtered_bank]
#print (adj_primes)

adj_primes_2 = [x-1 for x in filtered_bank]
#print (adj_primes_2)

adj_primes.extend(adj_primes_2)
#print (adj_primes)

#TEST AGAINST THESE
test_list = []
for p in adj_primes:
    if ((p / big_prime_bank[1]) == math.floor((p / big_prime_bank[1]))):
        test_list.append(int(p/3))
        
#print (sorted(test_list))        

#List of semi primes
semi_primes = []
for a in big_prime_bank:
    for b in big_prime_bank:
        if (a*b < 18000 and a*b > 9000):
            semi_primes.append(a*b)
#print(sorted(semi_primes))

#List of adjacent semi primes
adj_semi_primes = [x+1 for x in semi_primes]
#print (adj_semi_primes)

adj_semi_primes_2 = [x-1 for x in semi_primes]
#print (adj_semi_primes_2)

adj_semi_primes.extend(adj_semi_primes_2)
#print (sorted(adj_semi_primes))

#Two away from a prime

prime_and_two = [x+2 for x in big_prime_bank]
#print (prime_and_two)

prime_and_two_2 = [x-2 for x in big_prime_bank]
#print (prime_and_two_2)

prime_and_two.extend(prime_and_two_2)
#print (sorted(prime_and_two))

#Tilted prime list

tilted_semi_primes = []
for a in big_prime_bank:
    for b in adj_primes:
        if (a*b < 18000 and a*b > 9000):
            tilted_semi_primes.append(a*b)

#print (sorted(tilted_semi_primes))        

#Tertiary primes

tertiary_primes = []
for a in big_prime_bank:
    for b in big_prime_bank:
        for c in big_prime_bank:
            if (a*b*c < 18000 and a*b*c > 9000):
                tertiary_primes.append(a*b*c)
#print (sorted(tertiary_primes))            

#Taking test list and filtering out primes, semi primes, tertiary primes, adjacent primes, adjacent semi primes, tilted semi primes, two away from primes

#Filter out primes
final_list = list(filter(lambda x: x not in big_prime_bank, test_list))
#print (final_list)

#Filter out semi primes
final_list = list(filter(lambda x: x not in semi_primes, final_list))
#print (final_list)

#Filter out tertiary primes
final_list = list(filter(lambda x: x not in tertiary_primes, final_list))
#print (final_list)

#Filter out adjacent primes
final_list = list(filter(lambda x: x not in adj_primes, final_list))
#print (final_list)

#Filter out adjacent semi primes
final_list = list(filter(lambda x: x not in adj_semi_primes, final_list))
#print (final_list)

#Filter out tilted semi primes
final_list = list(filter(lambda x: x not in tilted_semi_primes, final_list))
#print (final_list)

#Filter out two away from primes
final_list = list(sorted(filter(lambda x: x not in prime_and_two, final_list)))

print ('If this is empty, then no counterexample: ')
print(final_list)

