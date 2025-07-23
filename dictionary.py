# n={
#     "name": "Pratiksha",
#     "marks": {
#         "python" : 90,
#         "C" : 80,
#         "Web" : 100
#             }
#    }
# print(n["marks"]["Web"])

# # Dictionary Methods
# print(n.keys())
# print(n.values())
# print(n.items())
# print(n.get())

# 1
# n={
#     "table" :["a piece of furniture","list of facts & figures"],
#     "cat" :"a small animal"
    
# }
# print(n)

# 2
dictionary={}
n=3
for i in range(n):
    key = input("Enter a key:")
    value = input("Enter a value:")
    
    dictionary.update({key:value})
print(dictionary)