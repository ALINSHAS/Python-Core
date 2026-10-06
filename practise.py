# def prime(n):
#     if n > 1:
#         for i in range(2,n):
#             if n%i==0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
#     else:
#         print("not prime")
# prime(2)
# def amstrong(n):
#     a=str(n)
#     l = len(a)
#     sum=0
#     for i in a:
#             sum+=int(i)**l
#     if sum == n:
#         print("amstrong")
#     else:
#         print("not amstrong")
# amstrong(153)
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# n=int(input("enter a number"))
# result=factorial(n)
# print(result)
# def pallindrome(n):
#     a=str(n)
#     pall=a[::-1]
#     if int(pall)==n:
#         print("pallindrome")
#     else:
#         print("not pallindrome")
#     return
# n=int(input("enter a number"))
# pallindrome(n)