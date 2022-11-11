#learning tuples
#difference between tuples & list is list contain sequence of data surrounded
#by [] and tuples contain list of data  surrounded by ()

#list occupy more memory than tuples
#tuples cannot be changed but made more quickly


bank_accounts=(("mark",32,"51 beach road","0987654323"),("ben",6000),("Sue",56878,"65 green lane"),
               ("tamara",-75))

print("The number of bank account is ", len(bank_accounts))

#showing name & balances

for i in bank_accounts:
    print("\nThe name is",i[0],"and the balance is $",i[1])

#showing only name with addresses

for i in bank_accounts:
    if len(i)>2:
        print("The name is ", i[0], "and the address is", i[2])


