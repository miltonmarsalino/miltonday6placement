mylist = ['nachi','nirmal','nandi']
print(mylist)
mylist.append(input("enter the patient name"))
print(mylist)
p= str(input("enter your index to be remove"))
mylist.remove(p)
print(mylist)
s = str(input("enter vip name"))
mylist.insert(1,s)
print("successfully print vip name:\n", mylist)
