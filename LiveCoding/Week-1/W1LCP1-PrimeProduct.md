![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/Live%20W1.P1.png)

```python

def prime_product(m):
    if m <= 0:
        return False

    # Check if m is divisible by any prime number up to its square root
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            # i is a factor of m, check if both i and m/i are prime
            if is_prime(i) and is_prime(m // i):
                return True
            else:
                return False

    return False


def is_prime(n):
    if n < 2:
        return False

    # Check if n is divisible by any number up to its square root
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

n = int(input())
print(prime_product(n))

```
