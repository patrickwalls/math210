def is_prime(n):
    "Determine if a positive integer n is prime."
    if n <= 1:
        return False
    for d in range(2, round(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

def primes_up_to(N):
    "Create the list of primes p less than or equal to N."
    return [ p for p in range(2,N+1) if is_prime(p) ]

def primes_interval(a,b):
    "Create the list of primes p contained in the closed interval [a,b]."
    return [ p for p in range(a,b+1) if is_prime(p) ]

def divisors(n):
    "Create the list of positive divisors of an integer n."
    return [ d for d in range(1,n+1) if n % d == 0 ]

def prime_divisors(n):
    "Create the list of prime divisors of an integer n."
    return [ p for p in range(2,n+1) if (n % p == 0 and is_prime(p)) ]

def twin_primes(N):
    "Create the list of twin primes [p,p+2] with p less than or equal to N."
    prime_list = primes_up_to(N)
    return [ [p,p+2] for p in prime_list if p + 2 in prime_list ]

def twin_primes_interval(a,b):
    "Create the list of twin primes [p,p+2] with p in the closed interval [a,b]."
    prime_list = primes_interval(a,b+2)
    return [ [p,p+2] for p in prime_list if p + 2 in prime_list ]


#def sum_of_squares(n):
#    "Return the list of pairs [a,b] of integers such that n = a**2 + b**2 with 1 <= a <= b."
#    return [ [a,b] for b in range(1,round(n**0.5)+1) for a in range(1,b+1) if n == a**2 + b**2 ]

