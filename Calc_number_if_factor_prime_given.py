# Created by RAHUL S H on 4/4/20

'''
All the input and output are accepted through the console.
Prints the number if given input in the following manner

INPUT:
First line is the number of test cases  (T)
Next T  lines consists of the x and k where 
x is the number of factors and 
k is prime factors

Ex:
2 =Test cases
4 2 = x and y

OUTPUT
One line answer for each test case printing number if exixts and 0 if no number exists
Ex:
6
As 6 has factors 1,2,3,4 which is equal to x
and has 2,3 as prime factors which is equal to k
'''

from math import sqrt

siz_array = 1000002
pfactors = []
pfactors.append(0)
# print(pfactors[0])

def primeNumberGenerator():
    # Create array of numbers and store the smallest prime factor of that number
    for i in range(1, siz_array):
        if i % 2 == 0:
            pfactors.append(2)
        else:
            pfactors.append(i)
    for i in range(3, int(sqrt(siz_array))):
        if pfactors[i] == i:
            for j in range(i * i, siz_array, i):
                if pfactors[j] == j:
                    pfactors[j] = i
    # print(pfactors)
primeNumberGenerator()

def numberOfDivisors(a):
    no_factor = 1
    no_prime_factors = 1
    cnt_primes_power = 1
    res = []
    if a == 1:
        res.append(no_factor)
        res.append(no_prime_factors)
        return (res)
    else:
        # store the smallest prime number that divides
        prime_divisor = pfactors[a]
        quotient = a // pfactors[a]
        while quotient != 1:
            if pfactors[quotient] == prime_divisor:
                cnt_primes_power += 1
            else:
                prime_divisor = pfactors[quotient]
                no_prime_factors += 1
                no_factor *= (cnt_primes_power + 1)
                cnt_primes_power = 1
            quotient = quotient // pfactors[quotient]
        no_factor *= (cnt_primes_power + 1)
        res.append(no_factor)
        res.append(no_prime_factors)
        return (res)

for i in range(int(input())):
    x, k = map(int, input().split())
    flag=0
    for i in range(2, 1000000):
        if pfactors[i]==i and x==2 and k==1:
            print(2)
            flag=1
            break
        elif pfactors[i]!=i:
            # print(numberOfDivisors(i))
            final_res = numberOfDivisors(i)
            # print(final_res[1])
            if final_res[0] == x and final_res[1] == k:
                flag=1
                print(i)
                break
    if flag==0:
        print(0)


