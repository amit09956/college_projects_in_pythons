# def fun(x):
#     if x > 1:
#         fun(x//2)
#         fun(x//2)
#     print(x)
# fun(4)


# def fun(n):
#     if n>100:
#         return n-10
#     return fun(fun(n+11))
    
# print(fun(91))    

# def count(n):
#     if(n>=0 and n<=9):
#         print(n)
#         return
#     s=count(n/10)+n%10
#     print(n)
# count(123)
# l=[1,2,3,4,5,6,7,8]
# a=0
# b=0
# for i in range(len(l)-1,):
#     if(i%2==0):
#         a+=l[i]
#     else:
#         b+=l[i]  
# print(a-b)    
# n=int(input())
# temp
# c=[]
# st="abcbaaabbaa"
# for j in range(len(st)):
#     a=st[j]
#     for i in range(j,len(st)-1):
#         a=st[:i]
#         b=a[::-1]
#         if(len(a)>=2):
#             if(a==b):
#                 c.append(a)
# str=set(c)   
# l=list(str) 
#print(c)
# print(l[0]) 
# List1=["shubham","rahul","shlok ","bhola"]
# Uppercase=list(map(str.upper(),List1))
# print(Uppercase)
# a=input()
# print(a)
# import math




#===================queston number-1===============================
# try:
#     Number_of_apples=int(input("enter the number of apples:"))
#     if Number_of_apples>=0 and Number_of_apples<=1000:
#         box=Number_of_apples/10
#         number_of_boxes=math.ceil(box)
#         print(number_of_boxes)
        
#     else:
#         print("please enter the value under 1000 ")
# except(ValueError):
#     print("invalid input") 


#=====================question number-2
# sales=[] 
# number_of_sales=int(input("enter the number of salrs"))
# for i in range(number_of_sales):
#     try:
#        data=int(input("Enter the sales data"))
#        sales.append(data)
#     except(ValueError):
#         print("Enter the valid data")
# if len(sales)==0:
#     print("sales data is not available")
# average_sales=sum(sales)/number_of_sales
# count=0
# for s in sales:
#     if s>average_sales:
#         count+=1
# print(count)


# l=[1,2,3,4]
# ans=iter(l)
# print(next(ans))  # prints 1
# print(ans)

l=[1,2,3,4]
ans=reversed(l)
print(next(ans))
print(ans)






