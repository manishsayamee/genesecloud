def findsmallestprime():
	isprime = list_primality(1000000)
	for i in range(len(isprime)):
		if not isprime[i]:

			continue

		n = [int(c) for c in str(i)]
		for mask in range(1 << len(n)):

			digits = do_mask(n, mask)
			count = 0
			for j in range(10):
				if digits[0] != 0 and isprime[to_number(digits)]:
					count += 1
				digits = add_mask(digits, mask)

			if count == 8:
				digits = do_mask(n, mask)
				for j in range(10):
					if digits[0] != 0 and isprime[to_number(digits)]:
						return str(to_number(digits))
					digits = add_mask(digits, mask)
	raise AssertionError("Not found")

def sqrt(x):
	assert x >= 0
	i = 1
	while i * i <= x:
		i *= 2
	y = 0
	while i > 0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y

def list_primality(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(sqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result


def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def do_mask(digits, mask):
	return [d * ((~mask >> i) & 1) for (i, d) in enumerate(digits)]


def add_mask(digits, mask):
	return [d + ((mask >> i) & 1) for (i, d) in enumerate(digits)]


def to_number(digits):
	result = 0
	for d in digits:
		result = result * 10 + d
	return result


if __name__ == "__main__":
	print(findsmallestprime())
    