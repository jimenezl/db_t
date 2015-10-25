"""
This is the file with your answer, do not rename or move it.
Write your code in it, and save it before submitting your answer.
"""

from os.path import abspath, dirname, join

def find_strong_pairs(number, upper_bound):
    """Returns of list prime numbers that form a "strong pair"
    with a given number.
    
    Args:
        number: The prime number given as input.
        upper_bound: The upper limit for what the value of
            paired prime can have
    Returns:
        An ordered list of prime numbers, less than the upper
        bound, that form a strong pair with the input 'number'.
    """
    # DO NOT modify the reference to the external file
    solution_directory = dirname(abspath(__file__))
    f = open(join(solution_directory, 'all_primes.txt'), 'r')

    def digitConcat(a,b):
        '''
        Concats two integers
        '''
        return int(str(a) + str(b))

    strong_pairs = []

    max_prime = max(digitConcat(number,upper_bound), digitConcat(upper_bound,number))

    primes = []
    for line in f:
        if int(line) > max_prime:
            break
        primes.append(int(line))

    f.close()

    answer = []

    for prime in primes:
        if prime > upper_bound:
            break
        primes.append(int(line))

        if (digitConcat(number,prime) in primes) and (digitConcat(prime,number) in primes):
            answer.append(prime)


    return answer

# This tests your code with the examples given in the question, 
# and is provided only for your convenience.
if __name__ == '__main__':
    print find_strong_pairs(3, 70)
    print find_strong_pairs(7, 100)