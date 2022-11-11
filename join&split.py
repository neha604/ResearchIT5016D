#splice,split(),join()

#below is list of names with variable names.
#matt is on index 0 while lily is on index -1 or 5

names= ["Matt","John","Peter","Maria","Pip","Lily"]
print(names[0])
print(names[0:2])
print(names[3:])
print(names[:5])
print(names[-1])


#split()
# We can split a string or list using split function

ird="123-789-345"
irdlist=ird.split("-")    #We split the string here
print(irdlist)

#splitting a sentence

b="Bill is in the garage"
print(b.split())       # this will split our string from space as no argument is passed

#join()

#lets take the same string

b=["bill","is","in","the","garage"]

#syntax = " ".join(variable which needs to join)

print(" ".join(b))