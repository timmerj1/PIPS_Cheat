import numpy as np

def prime(n):
    """
    Returns n prime numbers as a numpy array.
    """
    # Your code here
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    result = []
    i = 2
    while len(result) < n:
        if is_prime(i) == True:
            result.append(i)
        i += 1
    return np.array(result)

# I do see my docstring. Keeping definitions in their own .py file has several benefits, like being able to reuse the same definitions for several different scripts without putting it in every single script, and you can more easily split files into different components.

if __name__ == '__main__':
    assert prime(1) == 2
    assert prime(10)[-1] == 29
    assert prime(100)[-1] == 541
    assert prime(30)[-30] == 2
    assert prime(1) != 3
    print("Tests passed")
