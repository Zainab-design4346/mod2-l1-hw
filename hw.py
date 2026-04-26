def multiply1(N,M):
    return N*M

def multiply2(N, M):
    sum = 0
    for i in range(M):
        sum = sum + N
    return sum

num_n = int(input("Enter N: "))
num_m = int(input("Enter M: "))

result1 = multiply1(num_n, num_m)
print(f"The product of {num_n} and {num_m} is {result1}")

result2 = multiply2(num_n, num_m)
print(f"The product of {num_n} and {num_m} is {result2}")