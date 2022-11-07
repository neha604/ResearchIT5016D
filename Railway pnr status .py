
#This is copied from youtube just for practice codes and to see how they work.
#Indian Railway Ticket Booking system

print("\n\nTicket Booking System\n")
restart = ('Y')

# While loop for more than one entry
# if user chooses N or no etc program will stop
#PNR status means Passenger Name Record

while restart != ('N','NO','n','no'):
	print("1.Check PNR status")
	print("2.Ticket Reservation")
	option = int(input("\nEnter your option : "))

	if option == 1:
		print("Your PNR status is t3")
		exit(0)

# asking input from user
	
	elif option == 2:
		people = int(input("\nEnter no. of Ticket you want : "))
		name_l = []
		age_l = []
		gender_l = []
		for p in range(people):
			name = str(input("\nName : "))
			name_l.append(name)
			age  = int(input("\nAge  : "))
			age_l.append(age)
			gender  = str(input("\nMale or Female : "))
			gender_l.append(gender)

		restart = str(input("\nDid you forgot someone? y/n: "))
		if restart in ('y','YES','yes','Yes'):
			restart = ('Y')
		else :
			x = 0
			print("\nTotal Ticket : ",people)
			for p in range(1,people+1):
				print("Ticket : ",p)
				print("Name : ", name_l[x])
				print("Age  : ", age_l[x])
				print("Gender : ",gender_l[x])
				x += 1
