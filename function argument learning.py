#a function definition with required arguments
#arguments always go before keyword arguments orspecific order
def formal_greeting(name,title="Dr."):
    print("Greetings",title,name)

formal_greeting("jenkins")


#Variable argumets
# this functions takes 0 or more arguments

def family_members(*args):
    for name in args:
        print(name)

family_members("lucy","Matt","bob")

#fuction can also be called without passing any variable at all making it flexible


#*args or *a is common but can be called anything
def family_member(*names):
    for name in names:
        print(name)

family_member("john","Rick","Matt")

