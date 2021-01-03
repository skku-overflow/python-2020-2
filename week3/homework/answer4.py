

primes = []


def is_prime(i):
    # i: 1부터 100까지, 순서대로
    for divider in primes:
        if i % divider == 0:
            return False

    return True


class Primes:
    def __iter__(self):
        cur = 2

        for i in range(2, 100):
            if is_prime(i):
                primes.append(i)
                yield i


d = dict([(prime, idx) for idx, prime in enumerate(Primes(), 1)])
print(d)
