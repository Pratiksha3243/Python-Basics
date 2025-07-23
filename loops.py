# 1(FOR Loop)
# for i in range(0,10,3):
#     print(i+3, end=" ")

# 2-print 1 to 100
# for i in range(1,100,1):
#       print("Hello",i,sep="")

# 3-print 100 to 1
# for i in range(100,0,-1):
#       print(f"Hello{i}")

# 4-print any table
# n=int(input("Enter a number:"))
# for i in range (1,11,1):
#    print(f"{n}x{i}={n*i}")

#(WHILE Loop)
# i = 1
# while(i <= 100):
#     print(i)
#     i+=1

# 2
# i=100
# while(i > 0):
#     print(i)
#     i-=1

# break & continue
# 3
# n=int(input("Enter the number:"))
# sum=0
# while(n>0):
#     sum=sum+n
#     n=n-1
# print("Sum:",sum)

# 4
n=int(input("Enter a number:"))
f=1
for f in range(1,n):
    f=f*n
    n=n-1
print(f)
    
