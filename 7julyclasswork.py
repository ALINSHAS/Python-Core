# Q1.Define a function that takes 2 numbers and returns their product
def product(n1,n2):
    pro=n1*n2
    return pro

result=product(3,5)
print("product: ",result)
# Q2.Define a function that takes a string and returns number of vowels
def count_vo(s):
    count = 0
    v = "aeiouAEIOU"
    for i in s:
        if i in v:
            count += 1
    return count
result = count_vo("hello")
print("Count:", result)

# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
def rectangle_area(l,b):
    area=l*b
    return area
result=rectangle_area(3,5)
print("Area : ",result)
# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
def new_list(l):
    new=[i for i in l if i %2==0]
    return new
result=new_list([45,78,90,12,35])
print(result)

# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
def new_list(l):
    new=[]
    for i in l:
        s=str(i)
        sum=0
        for j in s:
            sum=sum+int(j)
        new.append(sum)
    return new
result=new_list([123, 345, 111, 678, 134, 809])
print(result)
# new=[6,12,3,21,8,17]