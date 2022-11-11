# we are learning to write simple functions with default values provided.

# we are naming our function get_aatribute and passing two arguments "query"
# and "default".


def get_attribute(query,default):
    
#our question will be combination of query plus deafult answer provided if user
# will leave space .

    question=query+'['+default+']?'
    answer=input(question)
    if(answer==" "):
        answer=default
    print('you chose',answer)
    return answer

#we are calling our function as below:

hair=get_attribute("what color hair","brown")

hair_lenght=get_attribute("whats hair length", "short")

eye_colour=get_attribute("whats the colour of eye","blue")

birth_mark=get_attribute("Do you have birth mark","on my arm")

# we can choose as many attributes as we want and give default values if not entered.
