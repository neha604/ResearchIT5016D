#Ceaser cipher is a cryptography or encryption techniques in which each letter
#in plaintext is replaced by a letter some fixed number of positions down the alphabets.
#for eg with a left shift of letter 3,D would be replaced by A,E would become B etc.


#we are using dictionary to index the letter & letter to index
#zip maps a number to a letter
# a will be mapped to 0 , b would be mapped to 1 and we make dictionary out of it.



alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ "

letter_to_index=dict(zip(alphabet,range(len(alphabet))))

# reversing the above

index_to_letter=dict(zip(range(len(alphabet)),alphabet))


#function to encrypt
def encrypt(message,shift=4):
    cipher=""

    for letter in message:
        index = (letter_to_index[letter] + shift) % len(alphabet) #we map letter to
        #number and add the shift into number.
        shifted_letter = index_to_letter[index]

        cipher+=shifted_letter

    return cipher  #return our ciphered text

#function to decrypt the message

#we are now decrypting ciphered text
def decrypt(ciphered_text,shift=4):
    decrypted=""
    for letter in ciphered_text:

         index = (letter_to_index[letter] - shift) % len(alphabet)
         shifted_letter = index_to_letter[index]

         decrypted += shifted_letter

    return decrypted # return decrypted message

def main():
    message="HAIL CAESAR OUR HERO"
    encrypted_message=encrypt(message,shift=4)
    decrypted_message=decrypt(encrypted_message, shift=4)

    print("Original message:"+message)
    print("Encrypted message: "+encrypted_message)
    print("decrypted_message: "+decrypted_message)

main()
