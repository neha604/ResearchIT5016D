#writing a code in which various queries can be asked with simple function
#this is a practice code copied from book.
#using default variable if no response is provided.

def get_attribute(query,default):
    question=query+'['+default+']?'
    answer=input(question)
    if(answer==" "):
        answer=default
    print("you chose",answer)
   
    

hair=get_attribute("what color hair","brown")

hair_lenght=get_attribute("whats hair length", "short")

eye=get_attribute("whats eye colour","blue")

gender=get_attribute("what gender","female")

glasses=get_attribute("Has glasses","no")

beard=get_attribute("Has beard","no")
