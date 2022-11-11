#fabonacci using while function

print("\n The Fabonacci Sequence")
p="0"

while int(p)<=3:
    p=input("please enter a number corresponding to the position in the sequence(should "
            "be atlest 3:)")

q=0
while q<=0:
    q=int(input("please enter number of terms to generate (should be positive integar):"))
    print("\n ",q, "numbers in the sequence starting from term",p,":")

#convert p & q to integars

p,q=int (p),int(q)

#initialise term counters to zero

p_counter, q_counter = 2,0
