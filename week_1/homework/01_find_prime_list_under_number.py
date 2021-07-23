input = 10


def find_prime_list_under_number(number):
    prime = []
    for n in range(2, number + 1):
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            prime.append(n)


    return prime


result = find_prime_list_under_number(input)
print(result)