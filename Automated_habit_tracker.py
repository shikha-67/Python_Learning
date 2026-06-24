print(23,"\n","my name",complex(3,4))
name='shradha'
print(name)
print('my name is:',name)
# print("my name is: "+  name)
# print('''Triple quote''')
x="1"
print(type(x))
x=None
print(type(x))

a=23
b=34

# arithmatic operator + - * / % **
a=3
b=5
print("Arithmatic operator")
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#relational operator == , !=, < , > ,>=, <=
a=3 
b=9
print("Relational operator")
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)

#assignment operator =,+=, -=, *=, /=, %=, **=
a=10
b=5
print("operator =: ",a)
a+=b
print("operator +=: ",a)
a-=b
print("operator -=: ",a)
a*=b
print("operator *=: ",a)
a/=b
print("operator /=: ",a)
a%=b
print("operator %=: ",a)
a=8
a**=b
print("Operator **=: ",a)

print("89 and 0: ",89 and 0)
print("89 and 1: ",89 and 1)

print("0 or 89: ",89 or 0)
print("89 or 1: ",89 or 1)

print("not 89: ", not 89)
print("not 0: ",not 0)

print((a<b) and (a==b))

a="2"
b=5

print(int(a)+b)

# n=input("Enter a number: ")
# print("You entered this number: ",n)

# print("type of input:",type(n),"Value of n: ",n)

# n=int(input("Enter a number: "))
# print("type of input:",type(n),"Value of n: ",n)

# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# print("Sum of two numbers: ",n1+n2)


# a=int(input("Enter area of square: "))
# print("Area of sqare: ",a*a)

# n1=float(input("Enter first number: "))
# n2=float(input("Enter second number: "))
# print("Sum of two numbers: ",(n1+n2)/2)
# if(n1>=n2):
#     print("True")
# else:
#     print("False")

a='''I am 
learning python'''
print("Python strip used: ",a.replace("\n","fill in"))
print(a)
print(a[-1])
print(a[0])
print(a[:3])
print(a[-3:])
print(a[1:])

a="aABHDS"
a1='J'+a[2:]
print(a1)
a1=a.replace("AB","CD")
print(a1)
print(a1.upper())
print(a1.lower())

a="hdg"
print(a*8)
print(f"a variable: {a}")

print("my nam is {} , my age is {}, my class is {}".format("Hita",21,23))

s1 = "apna college"
print(s1.endswith("ege"))
 

print(s1.count('a'))

# n=int(input("Enter your marks : "))


# if(n>=90):
#     print("Grade A")
# elif(n<90 and n>=80):
#     print("Grade B")
# elif(n<80 and n>=70):
#     print("Grade C")
# else:
#     print("Grade D")


print(list("apna"))

n=[1,2,34]
n.extend([9,1])
print(n)
n.remove(2)
print(n)
n.pop()
print(n)

data={
    "name":"jake",
    "age":24
}
print(data)
print(data["name"])
print(data["age"])
data.pop("age")
print(data)


n=[1,2,3,2,1]
n_copy=n.copy()
n.reverse()
if(n==n_copy):
    print("palindrome")
else:
    print("not palindrome")


t=('c','a','d','a','b','b','a')
print(t.count('a'))
l=list(t)
l.sort()
print(l)



