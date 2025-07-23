# 1
# def cal_sum(n):
#     if n == 0:
#         return 0
#     return n + cal_sum(n - 1)

# n = int(input("Enter a number: "))
# result = cal_sum(n)
# print("Sum =", result)

# 2
# def cal_factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * cal_factorial(n - 1)
# n = int(input("Enter a number: "))
# result = cal_factorial(n)
# print("Factorial =", result)

# 3
def print_ele(list, index=0):
    if index < len(list):
        print(list[index], end=" ")
        print_ele(list, index + 1)
list = [1, 2, 3, 4, 5, 6]
print_ele(list)