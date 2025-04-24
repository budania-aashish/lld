"""
    In the world of software development, complexity can often be the enemy of progress.

    The KISS principle, which stands for "Keep it Simple, Stupid" is a design philosophy
    that emphasizes the importance of simplicity in software development.

    It suggests that software should be designed to be easy to understand, modify, and
    extend, rather than complex and convoluted.

"""

# overly complex
def factorial(n):
    if n<0:
        print("Factorial not possible")
        return -1
    if n==0:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result*=i
    return result


# keep it simple 
import math

def factorial_value(n):
    if n<0:
        print("Factorial not possible")
        return -1
    return math.factorial(n)