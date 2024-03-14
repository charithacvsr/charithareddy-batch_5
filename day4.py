#day:4
# -----> while loop
# -----> break using while loop
# eg:1
# iterate from 20 to 30 and break the loop
'''
i=20
while i<31:
    print(i)
    i+=1
    if i ==27:
        break
    i+=1    
s1 = "hello world to all"
'''
'''
# eg:2
i = 27
while i==27:
   print(i)
   if i == 27:
    break
    i==27
'''
'''
# -----> continue

# eg:1
i=20
while i<31:
    i=i+1
    if i==1:
        continue
    print(i)
    '''
'''
for val in range(20,30):
   if val==27:
       continue
       print (val)
'''
# eg:5
# while to iterate from 12 to 22
# find the sum of all numbers
'''
i=12
sum=0
while i<23:
    sum=sum+i
    i+=1
# print(sum)
'''
# eg:6
# find the average of value from 20 to 25
'''
i=20
sum=0
count=0
while i<=30:
     sum= sum+i
     count+=1
     i+=1
print(sum/count)  
'''
# -----> nested for loop
# eg:1


'''
for i in range(1,3+1):
    for j in range(1,4+1):
        print(i,j)


'''
'''
for row in range(4)
   for col in range(4)
       print("*",end=" ")     
   print()

'''
'''
 
sum=0
for row in range(5):
   for col in range(5):
    sum=sum+1
    print(sum,end=" ")     
   print()
'''

'''
# to print starts in right angle triangle


for row in range(0,6):
   for col in range(0,row):
      print("*",end="")
    print()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
'''

'''
for row in range(0,6):
  for col in range(row,6):
     print("*",end="")
  print()
'''
'''
for row in range(5):
  for col in range(5):
    if col==0 or col==5-1 or row==0 or row ==5-1:
       print("*",end=" ")
    else:
       print("",end="")
    print()  


  '''
'''
for row in range (0,5):
   for col in  range(0,6):
      if ((row==0 and col==3) or(row==1 and(col>=2 and col<=4)) or (row==2 and (col>=1 and col<=5))):
         print("*", end="")
      else:
         print("",end="")
      print()   

'''
'''

#------> list


#-----> datatypes
# primary

# number---> int,float,complex
number
string
boolean
none


collection
list
tuple
set
dictionary

# list
1* if the collection of elements are surronded by square brackets it is consider
       to be as list
       # eg
       11=[4,7,9,9.89,"hello",7+9j,[8,9,0]]
# characterstics of list
1*list have  to be surronding by[]
2*it is mutable (the elements in the list are changable)
3*evry elements inside list will be ordered format
4*the elements inside list will be ordered format
5*it can hold duplicate values
6* its heterogenous



# to access the elements in list
11=[1,4,1,7,89,7,7.5,"p","i']
    print(11)



 # ----> indexing
*** in the collection data types list likee
    list
    tuple
    string
the elements will be alloted
*** with pre-defined unique called index value

    # WE HAVE 2 TYPES OF INDEXING
 *** postive indexing ---> starts with 0 from left hand side
 *** negative indexing --->starts with -1 from right hand side
    # postive indexing
    print(lst1[0])

    # NEGATIVE INDEXING
    LST1=[1,4,1,7,89.7,7.5,"p","i"]
    print(lst1[-1])

'''

    # SLICING
LST1=[1,4,1,7,89.7,7.5,"p","i"]
LST1[start_index:end_index:step]
    print(lst1[0:4])
    print(LST1[6:8])
    print(LST1[3:6])
    print (LST1[:5])
    print (LST1[3:])
    print (LST1[:])

    print(LST1[0:7:1])# lst1[0:7] --->both are same
    print(lst1[0:7:2])


trail =int(input())





lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print (lst1[-4:-1])
print(lst1[-1:-4]) ---> []
print (lst1[-7:-1])
print (lst1[-7:-1:2])



# ! to insert to the element inside list

appened() ---> used to add element at last position of list
l1=[9,8,0,6]
l1.appened("car")
print(l1)



    
















       
