# sets={"python","java","C++","python","javascript","java","python","java","C++","C"}
# print(sets)
# print(len(sets))

# 2
text1=("Python is a great programming language")
text2=("Many developers love the Python language")
set1 = set(text1.split())
set2 = set(text2.split())
common_words = set1.intersection(set2)
difference=set1.difference(set2)
print("Common words:",common_words)
print("Difference:",difference)



