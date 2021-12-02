'''
Display all the details of application by a given author
'''

soft1={"Book name":'Java',
       "Author name":'James Gosling',
       "Version":'4.0',
       "Publishing year":"1995",
       "Price":345}
soft2={"Book name": 'Python',
       "Author name":'Guido Van Rossum',
       "Version":'3.0',
       "Publishing year":"1980",
       "Price":679}
soft3={"Book name": 'C',
       "Author name":'Brian Kernighan Dennis Ritchie',
       "Version":'2.0',
       "Publishing year":"1978",
       "Price":125}

print("Book 1:",soft1,"\n","Book 2:",soft2,"\n","Book 3:",soft3)
print()
print()
print()


'''
Sort the details of application in the increasing order of price
'''


if (soft1["Price"]<soft2["Price"]) and (soft1["Price"]<soft3["Price"]):
    print(soft1)
    print(soft2)
    print(soft3)

elif(soft2["Price"]<soft1["Price"]) and (soft2["Price"]<soft3["Price"]):
    print(soft2)
    print(soft1)
    print(soft3)
else:
    print(soft3)
    print(soft1)
    print(soft2)

print()
print()
print()


'''
Display the details of application published by a given publisher in a given year
'''
if (soft1["Publishing year"]<soft2["Publishing year"]) and (soft1["Publishing year"]<soft3["Publishing year"]):
    print(soft1)
    print(soft2)
    print(soft3)

elif(soft2["Publishing year"]<soft1["Publishing year"]) and (soft2["Publishing year"]<soft3["Publishing year"]):
    print(soft2)
    print(soft1)
    print(soft3)
else:
    print(soft3)
    print(soft2)
    print(soft1)
print()
print()
print()
'''
Sort the list of applications in the inceasing order of two fields, author and publishing year of the books
'''

if(soft1["Author name"],soft1["Publishing year"]>soft2["Author name"],soft2["Publishing year"]) and (soft1["Author name"],soft1["Publishing year"]>soft2["Author name"],soft2["Publishing year"]):
    print(soft3)
    print(soft2)
    print(soft1)
elif(soft2["Author name"],soft2["Publishing year"]>soft1["Author name"],soft1["Publishing year"]) and (soft2["Author name"],soft2["Publishing year"]>soft3["Author name"],soft3["Publishing year"]):
    print(soft2)
    print(soft1)
    print(soft3)
else:
    print(soft1)
    print(soft2)
    print(soft3)

'''
End of the Program or Task
'''
    

