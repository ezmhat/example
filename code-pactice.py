
# # {CMD:c:documents/school/cd ../..
# c:documents/mk(/)rmdir(del:filename) school/foldername}
_______
# int= integer number//
# float= actual number/
# string {str}=("_",'_') - ("don't")/('don\'t'){str}
# print (f"{variable} words") replaces a comma in a variable cobination with a string.
# sep= to seperate
# end=
# boolean- {True / False} type: class_bool
# bool(1)=True
# bool(0)=False
# bool("")=False
# bool("a")=True
# bool(none)=False
# True+True ==2
# 5+True =6


# ___ Variable practice
number_of_seconds=int(input("enter some number"))
total_hours = number_of_seconds // 3600
remaining_seconds=number_of_seconds % 3600
minutes=remaining_seconds//60
seconds=remaining_seconds% 60
total_days=total_hours//24
hours=total_hours%24
days=total_days%365
years=total_days//365
print("your number is" ,years,"years",days,"days",hours, "hours" ,minutes, "minuts" ,seconds,)

number=int(input("enter number"))
unit=number%10
ten=number//10%10
hundred=number//100
result=ten-(unit+hundred)
print(number,"number",unit,"unit", ten,"ten", hundred,"hundred")

myjob_salary=int(input("enter myjob salary"))
c_salary=int(input("enter c salary"))
scolarship=int(input("enter scolaship"))
additional_income=int(input("enter divers"))
english_course=int(input("enter price for e.c"))
gym=200
food=int(input("enter food expenses"))
additional_expenses=int(input("enter number"))
saving_of_the_month=myjob_salary+c_salary+scolarship+additional_income-english_course-gym-food-additional_expenses
print(saving_of_the_month)

score= 50
price=score*2
since=price/2
print (since)

height=int(input("your height"))
weight=int(input("your weight"))
bmi=weight/(height*height)
print (bmi)

hour=int(input("insert number of hours"))
salary_for_hour=75
vat=(salary_for_hour*hour)/100*17
total_salary=hour*salary_for_hour-vat
print (total_salary,"vat:",vat,)

radius=int(input("enter radius"))
lt=3.14
s=lt*radius*radius
p=2*lt*radius
print(s,"s",p,"p")

product_price=int(input("enter price"))
discount=int(input("enter discount"))
discount_amount=product_price/100
final_price=discount_amount*discount
print(final_price)

base=int(input("enter base"))
height=int(input("enter height"))
v=base*height
v_for_triangular=v/2
print("v",v,"v_for_triangular",v_for_triangular)

widt=int(input("enter widt"))
length=int(input("enter length"))
s=widt*length
print(s)

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=int(input("enter d"))
e=int(input("enter e"))
average=(a+b+c+d+e)/5
total=a*b*c*d*e
print(average,"average",total,"total")

celsius=int(input("enter celsius"))
Fahrenheit=int(input("enter Fahrenheit"))
Fahrenheit_to_celsius=celsius*9/5+32
celsius_to_fahrenheit=(Fahrenheit-32)*5/9
print(celsius_to_fahrenheit)

shekel=int(input("enter shekel"))
dollars=shekel*0.27
hindu_roupie=shekel*74.19
print (hindu_roupie,"roupie",dollars,"dollars" )

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
avi=b
beni=a
dor=c
a=dor
b=beni
c=avi
print(a,"a",b,"b",c,"c")
# >or when you have 2 variable
a=3
b=7
a,b=b,a
print("a",a,"b",b)

total_minutes=int(input("enter minutes"))
total_hours=int(input("enter hours"))
minutes=total_minutes%60
hours=total_hours+total_minutes//60
time_after_midnight=hours*60+minutes
print(time_after_midnight)

a=input("enter a")
b=input("enter b")
c=input("enter c")
d=input("enter d")
e=input("enter e")
f=input("enter f")
g=input("enter g")
print(a+b+c,d+e,f,sep='\n')

# ____Data type practice

# a=bool(1){True}
# b=False
# print (a)
# or
# and
# xor
# not
# nand[not and]
# biger >_< smoller
# = equal
# != not equal
# control flow: if True the operation will be perfomed
# in=bool array to check if an item is in the list

age=int(input("enter your age"))
valid?=>0<=40

input_number=input("insert number")
is_number=input_number=>"0" and input_number<="9"
print (is_number)

input_number=int(input ("insert number"))
input_number_two=int(input ("insert number"))
pair=if (input_number + input_number_two) %2==0:
	print ("it's odd")
else:
	print (False)

input_number=int(input("insert number"))
if input_number> 0:
	print("yea")
elif input_number< 2:
	print("change")
else:
	print("negative")

n1=int(input("number1"))
n2=int(input("number2"))
n3=int(input('number3'))
if n1>=n2 and n1>=n3 and n2>=n3:
	print ("n1","n2","n3")
elif n2>n1 and n2>=n3 and n1>n3:
	print("n2","n1","n3")
elif n1>=n2 and n1>=n3 and n3>n2:
	print("n1","n3","n2")
elif n2>=n3 and n2>n1 and n3>n1:
	print("n2","n3","n1")
elif n3>n1 and n3>n2 and n1>=n2:
 	print("n3","n1","n2")
elif n3>n2 and n3>n1 and n2>n1:
	print("n3","n2","n1")

x=int(input("insert number"))
units=x%10
tens=x//10
sum=units+tens
result=x%sum==0

age=float(input("enter your age"))
height=float(input("height"))
weight=float(input("weight"))
ratio_height_weight=height/weight
invalide_age=age<11 or age>120
if age>=11 and age<=20 and ratio_height_weight>=0.5 and ratio_height_weight<2:
	print(ratio_height_weight,"menu-a")
elif age>=11 and age<=20 and ratio_height_weight>=2 and ratio_height_weight<3.5:
	print(ratio_height_weight,"menu-b")
elif age>=11 and age<=20 and ratio_height_weight>=3.5 and ratio_height_weight<5:
 print(ratio_height_weight,"menu-c")
elif age>=21 and age<=40 and ratio_height_weight>=0.5 and ratio_height_weight<2:
	print(ratio_height_weight,"menu-a")

elif age>=21 and age<=40 and	ratio_height_weight>=2 and ratio_height_weight<3.5:
	print(ratio_height_weight,"menu-b")
elif age>=21 and age<=40 and	ratio_height_weight>=3.5 and ratio_height_weight<5:
	print (ratio_height_weight,"menu-a")
elif age>=41 and age<=120 and ratio_height_weight>=0.5 and ratio_height_weight<2:
	print(ratio_height_weight,"menu-a")
elif age>=41 and age<=120 and ratio_height_weight>=2 and ratio_height_weight<3.5:
	print(ratio_height_weight,"menu-c")
elif age>=41 and age<=120 and ratio_height_weight>=3.5 and ratio_height_weight<5:
	print(ratio_height_weight,"menu-c")
elif invalide_age:
	print("invalide_age")

	number=int(input("enter number"))
operator=input("enter operator")
number_t=int(input("enter number"))
if operator=="+":
    print(number+number_t)
elif operator=="-":
    print(number-number_t)
elif operator=="/":
    print(number/number_t)
elif operator=="*":
    print(number*number_t)
# debug=test code line by line
# while=loop
# dry-do'nt repeat yur self
# while-{bool-}if true-do action-WHILE. but if false-break the while.-to stop tap:CTRL D, or CTRL C.
# while exemple:
i=0
while i<=100:
	i=int(input("enter number"))
	# -to prevent an infinite loop
print(i)

# print 0-10
i=0
while i<=10:
    print(i)
    i +=1

i=0
while true:
	i +=1
if i>=50
	break
if i%2 ==1:
	continue
	print(i)

for i in range(0,5):
	print(i)

for i in range(0,30,3):
	print(i)

# range=number generator

for char in "python":
	print(char,end='')

# LIST
# creat list
my_list=[]
print(my_list {place}0){first}
print(my_list 1){second}
print(my_list -1){last}
# change in the list
my_list[1]="world"
# del. in the my_list
my_list.pop()
my_list.remove("abject")
# add to the and of my_list
my_list.append("new item")
# add to the list speciffic place
my_list.insert({place}1,"_")
# fontion
len(my_list)
sum(my_list)
max(my_list)
min(my_list)
reverse(my_list)
my_list.index

my_list=["cohen","levi","goldman","zerbib"]
my_list.insert(2,"hilou")
my_list.append("friedman")
print(my_list [2],len(my_list))

my_list=[["82","67","104"],["34","98","79"],["87","45","21"]]
print((my_list)[0])
my_list=[["82","67","104"],
         ["34","98","79"],
         ["87","45","21"]]
for student in range(len(my_list)):
for grade in range(len(my_list[0])):
   print(my_list ,(student),(grade),end="")



num=int(input("enter number"))
num_copy=num
reverse_nunber=0
my_list=
while num_copy>0:
	digit=num_copy%10
    num_copy=num_copy//10

reverse_nunber*=10
reverse_nunber+=digit
if_palindrome=number==reverse_nunber
print ("the number is palindrom",reverse_nunber)
else print("your number is not palindrom",reverse_nunber)

name=(input("enter your name"))
number=0
while number<1000:
    print(number,name)
    number +=1

i=int(input("enter your i"))
for i in range(i,100,3):
    print(i)

i=0
while i<1000:
    num=int(input("enter your number"))
    if num %7==0:
        print("boom")
    else:
        print(i)
    i +=1

i=int(input("enter your number"))
counter=0
while i>0 or i<0:
    number=int(input("enter your number"))
    if number==0:
      break
    counter=counter+number
print(counter)

i=int(input("enter your number"))
counter=0
while i>-1 or i<-1:
    print (counter)
    counter +=1
    number=int(input("enter your number"))
if number==-1:
    print(counter)

fuzz="fuzz"
buzz="buzz"
fuzz_buzz="fuzz buzz"
for i in range(1001):
    if i%3==0 and i%5==0:
        i=fuzz_buzz
    elif i%3==0:
        i=fuzz
    elif i%5==0:
        i=buzz
    print(i)

number= int(input("enter"))
stars=""
under_stars=""
for i in range(0,number):
    stars +="*" * i +"\n"
for n in range(number,-1,-1):
    under_stars +="*"  * n + "\n"
print(stars,under_stars,se


number=int(input("enter number"))
for i in range(1,number+1):
    print(" " * (number-i),f"{i} "* i)

my_list = []
for i in range(1,11):
  my_list.append(i)
my_list.insert(3,"100")
my_list.append("11")
my_list.insert(1,50)
my_list.remove("100")
list=my_list[1:5]
print(my_list.pop())
print(my_list)



shopping_list=[tomatoes, milk, beer, pizza]
print(o:2)


number = [1,2,3]
reverse_nunber= [::-1]
all= number+reverse_nunber
print (all)

list=[1,2,3]
list2=[4,5,6]
list3 = []
for i in range(len(list)):
    list3.append(list[i]+list2[i])
print(list3)

matrix=[[1,2,3]
        [4,6,7]
        [8,9,0]]
print([2][1]) =9

# matrix=[[1,2,3],[4,6,7],[8,9,0]]
# for i in range(len (matrix)):
#  row=matrix[i]
#  for y in range(len(row)):
#     print (row[y],end=" ")

numbers=input("number")
reverse =''
last = len(numbers)-1
for i in range(len(numbers)):
    leter = numbers[last - i]
    reverse = reverse + leter
if reverse==numbers:
    print("pilandrum")
else:
    print(no)

for variable in iterable:

number=range(0,8)
my_number=list(number)
my_short=list(range(8))
print(my_number)

for variable in range: loop number generator, acces to index in array\my_list, creating sequences in an array.

total_years=int(input("enter years"))
interest_pourcentage=int(input("enter interest pourcentage"))
for i in range(len(total_years)):
	print()


my_list=["a","c","d","s"]
for i in range(len(my_list)):
    # print(my_list[i]*2,end=' ')
    print(my_list[i],my_list[i+1])

    list_of_number=[8,5,98,56,33,21,87,6,2,1,7]
for index ,value in enumerate(list_of_number):
    # if index%2==1 and value%2==0:
        print(value)

number=0
list1=[]
for i in range(5):
    number = int(input("enter"))
    list1.append(number)
print(list1)

list1=[]
list2=[]
list3=[]
for i in range(200):
    # number=int(input("enter"))
    # list1.append(number)
    list1.append(i)
for index, value in enumerate(list1):
   if value % 2==0:
       list2.append(value)
   else:
       list3.append(value)
print(list2,list3,sep='\n')

list1=[2,3,8,9,7,6,78,65,45,89,76,32]
user=int(input("insert number"))
if user in list1:
    print ("true")
else:
    print("false")
num=list1.index(user)
print(num,list1[num])

maxi=0
list1=[]
for i in range(10):
    user=int(input("insert number"))
    if user>maxi:
        maxi=user
        list1.append(user)
print(maxi)
# print(max(list1))

list1=[]
sum1=0
a=True
for i in range(3):
    user=int(input("insert number"))
    list1.append(user)
    sum1 +=user

for y in range(len(list1)-1):
    if list1[y]>list1[y+1]:
        a=False
if a:
    print(sum1)
else:
    print(sum1/len(list1))




a= 0
num=0
sum1= 0
counter= 0
pair= 0
impair=0
big = MININT
small = MAXINT
while a==0:
    user1=input('insert number')
    if user1 != 'exit':
       sum1 += int(user1)
       num=int(user1)
       counter +=1

       if num % 2==0:
        pair +=1
       else:
        impair +=1
       if  num>big:
         big =num
       if num<small:
          small=num
    elif sum1 != 0 and user1 =="exit":
        a =1
average = sum1 /counter
print(counter,sum1,average,pair,impair,big,small)


for i in range(5):
    for j in range(5):
        if i ==j:
            print("*",end="")
        else:
            print(" ",end="")
        if i==j or i+j == 5-1:
        # if i<=j:
            print('*')
     print()    

# sum=0
# id=int(input("number"))
# flag=True
# while id>0:
#     current=id%10
#     id //=10
#     if flag:
#         current *=2
#     sum=current%10
#     current//=10
#     sum +=current
#     flag=not flag
# ress=10-(sum%10)%10
# print(ress)



# a = [1, 4, 0, 2, 8]
# # print(a[a.index(2)])
# # for i in a[::-1]:
# #     print(i,end="")
# # a.insert(0,5)
# # print(a)
# # print(a.pop())
# # a.pop()
# b=True
# user=int(input("insert number"))
# if user in a:
#         print(b)
# else:
#    b=False
#    print(b)
# print(a.index(0))


# ___str:

# -'hello'.upper() =>'HELLO'
# -'WORLD'.lower()=>'world'
# -'hello'.strip()=>'hello'
# -'cat'.replace('c','d')=>'bat'
# -'a,b,c'.split(',')=>['a','b','c']
# -','.join(['a','b','c'])
# -'hello world'.strip()
# -'hello world'.join()
sentence="what are you doing"
second_sentence="i dont"
print(sentence.lower()) 
print(sentence.upper())
print(sentence.capitalize())
print(sentence.count("a"))
print(sentence.find("z"))
print(sentence.replace("w", second_sentence))
print(sentence.join(second_sentence))
print(sentence.split(" "))
print(sentence.strip())
______

a =[]
b =-1
while b!= 0:
    user=int(input("insert number"))
    a.insert(0,user)
    if a [0] == 0:
      b += 1
c= a.pop(-1)
a.insert(0,c)
print (a)


matrix=[
[1, 2, 3],
[4, 5, 6],  
[7, 8, 9]
]
total=0
for i in matrix:
    for j in i:
        total +=j
print(total)

rows=3
colum=4
matrix=[]
for i in range(rows):
    row=[]
    for j in range (colum):
        row.append(i*j)
    matrix.append(row)
for row in matrix:
    print(row)
    
rows=10
colum=10
matrix=[]
for i in range(1,rows+1):
    row=[]
    for j in range (1,colum+1):
        row.append(i*j)
    print(row)

# tuple=list inchangable
my_dictionary={"elvet":44,"hole":56, 'b': True }
a= 0
num=0
sum1= 0
counter= 0
pair= 0
impair=0
big = MININT
small = MAXINT
while a==0:
    user1=input('insert number')
    if user1 != 'exit':
       sum1 += int(user1)
       num=int(user1)
       counter +=1

       if num % 2==0:
        pair +=1
       else:
        impair +=1
       if  num>big:
         big =num
       if num<small:
          small=num
    elif sum1 != 0 and user1 =="exit":
        a =1
average = sum1 /counter
print(counter,sum1,average,pair,impair,big,small)


my_dictionary [44]={'r':34,'t':65}
my_dictionary[34]='y'
my_dictionary['elvet']=22
my_dictionary.add(3456)
print(my_dictionary['elvet'],my_dictionary)

marks_data={'kodkode':{'class':{'name':'jerusalem2','marks':[90,85,94,78,83]}}}
print(marks_data['kodkode']['class']['marks'][1])
marks_data={}
marks_data['kodekode']={}
marks_data['kodekode']['class']= {}
marks_data['kodekode']['class']['name']='jerusalem2'
marks_data['kodekode']['class']['marks']=[90,85,94,78,83]
list.set
print(marks_data)

student={'david':{'id':3425,'age':324},'simon':{'id':4563,'age':567}}
for item in student:
	print(item)
	for inner_key in item:
		print(inner_key)
for items in student.items():
    print(items)


a= 0
num=0
sum1= 0
counter= 0
pair= 0
impair=0
big = MININT
small = MAXINT
while a==0:
    user1=input('insert number')
    if user1 != 'exit':
       sum1 += int(user1)
       num=int(user1)
       counter +=1

       if num % 2==0:
        pair +=1
       else:
        impair +=1
       if  num>big:
         big =num
       if num<small:
          small=num
    elif sum1 != 0 and user1 =="exit":
        a =1
average = sum1 /counter
print(counter,sum1,average,pair,impair,big,small)


a =[]
b =-1
while b!= 0:
    user=int(input("insert number"))
    a.insert(0,user)
    if a [0] == 0:
      b += 1
# c= a.pop(-1)
# a.insert(0,c)
print (a)



from ctypes import c_int64

list1=[]
a=[]
b=[]
counter=0
# counte2=0
for i in range(8):
  user1=int(input("number"))
  counter +=1
  if counter<= 2:
   a.insert(0,user1)
  else:
   b.insert(0,user1)
# counter2=int(counter/2)
for index,value in enumerate(a):
   for i in range(4):
    # if i>len(b)-2 or i<1:
    #  list1.append(a[i])
    else:
     if index%2==0:
        list1.append(a[i]*b[i+1])
     else:
        list1.append( a[i]+b[i-1])
print (list1)        

# 1:
word=input("word")
numbers=input("number")
convert=int(numbers)
print(word*convert)
# 2:
x=4
for i in range(x):
    s=""
    for j in range(i+1):
        s +=str(j+1)
    print(s)

d={"a":{3,4},2:7}
print(len(d["a"])+len(d))
# 3:
c=1
a=[]
b=[]
while c==1:
    user1=int(input("number"))
    a.append(user1)
    if user1==0:
        c=2
while c==2:
    user2=int(input("number"))
    b.append(user2)
    if user2==0:
        c=3

a=[1,2,3]
b=[1,2,3]
sum=0
if len(a)==len(b):
    for i in range(len(a)):
        sum +=a[i]*b[i]
    print(sum)
else:
    print("arrays must have the same length")

a = [1, 2, 3]
b = [1, 2, 3,4]
sum = 0
if len(a) == len(b):
    for i in range(len(a)):
        sum += a[i] * b[i]
    print(sum)
else:
    print("arrays must have the same length")

# 4:
list1=[]
list2=[]
for num in range(3):
    list1.append(num)
print(list1)
last=list1[-1]//2
length=len(list1)*2
data={"last":last,"length":length}
for i in range(data["length"]):
    if i<len(list1):
        item=list1[i]
        list2.append((item-1)**2)
    else:
        list2.append(1-(i%2))
print(list2)
isinlist=data['last']in list2
print(isinlist)
while list2:
    list1.append(list2.pop())
print(len(list1))
# 5:
a=[1,2,3]
counter=0
num=int(input("number"))
for i in a:
    if num<i:
        counter +=1
print(counter)

m=[1,2,3]
list1=[]
d=0
matrix=[]
for i in range(len(m)):
    d=m[i]
    for j in range(len(m)):
        list1.append(d)
    matrix.append(list1)
print(matrix)
sum=0
sum1=0
num=0
for i in matrix[0]:
    sum +=i
for i in range(len(matrix)):
    sum1 +=matrix[i][1]
num=matrix[0][1]
print(sum+sum1-num)




____function

# def function():
#     pass= skipping a function(like if not ready)
      """
      remark
      """
    # the function is over at the end of the indentation.  
# def matrix():
#    print ("name of the function is matrix")

def prinscope():
    global x
    print (x)
    x=1
    y=5
    print(x,y)
def hello():
    print("hello")
def userinput():
    user=int(input("number"))
    if user %2==0:
        print("even")
    else:
        print("odd")

def name():
    counter=1
    letter_d={}
    user=input("name")
    for l in user:
     if l ==" ":
         counter +=1
     elif l not in letter_d:
      letter_d [l]=1
     else:
      letter_d [l] +=1
    for key,value in letter_d.items():
      if key==" ":
        print("now",value +1)
      else:
        print(f"{key}:{value}")
   
def c_salary(hour,salry_per_hour):
  return hour*salry_per_hour

def c_tax(amount,tax):
   return amount*tax/100

def total_salary(brut_salar,tax)
    return brut_salar-tax

total = c_salary()
tax = c_tax()
salary = total_salary()
print('your salary is', salary)    

def mul(*number):
    t=1
    for num in number:
        t *=number
print (t)        

def print_helo(a,b):
    print('hello',a,b)
    

full_n=['a','b']
print(*full_n)

def registration(**kwargs)
   print(f"name:{kwargs["fn"]}{kwargs["ln"]})
registration(fn="nati",ln="dav")    


def week(days_number):
   day_of_week= {1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday", 7: "sunday"}
   # if days_number in day_of_week:
   #     return day_of_week[days_number]
   # else:
   #     return "invalid day"
   return day_of_week.get(days_number,"invalid day")

# logging
# {my pip}
# terminal:pip install numpy
# print(__name__)-if __name__ == "__main__":
#     print("run from this page")
# else:
#     print("I am imported")


__# debuger

# def func():
#    lit1=[1,2,3,4,5,6]
#    for i in lit1:
#        print(i)
#        lit1.pop(0)
#        print(lit1)



import time
import datetime
from time import localtime
from pynput import keyboard
localtime1=str(datetime.now)[:16]
datatime={}
words=""
sentence=""
counter=0
def printer(key):
     global words
     global sentence
     global counter
     if str(key) == 'key.space':
         words += " "
     else:
      words +=key.char
      sentence += str(words)
      local_time = time.ctime()
     if "show" in sentence :
       print(words)
       print(local_time)
       words=""
       sentence=""
     if key.char=='.':
       l.stop()
def timer():
    global localtime1
    global datatime
    if localtime1 in datatime:
     datatime
l = keyboard.Listener(printer)
# if __name__=="__main__":
l.start()
l.join()



def dividing(num):
    division=[]
    for i in range(1,num):
        if num % i==0:
          division.append(i)
    return division

def bigl(list_num):
 # list_num=[4,7,9,8,76,5]
 max_num=list_num [0]
 for i in list_num:
    if i>max_num:
        max_num=i
return max_num

def find_ms(ms):
 subs=[]
 strlen=len(ms)
 for start in range(strlen):
    for end in range(start,strlen):
        subs.append(ms[start:end+1])
 return subs





















































