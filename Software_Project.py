# IT Helpdesk Prototype

name = " "
staffid = 0
email = ""
desc = ""
tickets_created = 0
tickets_resolved = 0
tickets_tosolve = 0
x = 0


def create_ticket():
    global name
    global staffid
    global email
    global desc
    global tickets_created
    global x
    global p
    global w
    global s
    global tickets_resolved

    name = input("Enter Name :  ")
    staffid =input("Enter Staff ID :  ")
    email = input("Enter your email :  ")
    desc = input("Enter Description")
    x += 1
    ticket_no = 2000 + x
    print("your Ticket no is", ticket_no)

    p = name[0:3]
    w = staffid[0:2]
    s = p + w

    print("Your new password if required is :", s)

    print("...........")
    print("...........")


def ticketstats():
    print("Tickets Created : ", tickets_created)
    print("Tickets Resolved :", tickets_resolved)
    print("Tickets to Solve: ", tickets_tosolve)


def displayticket():
    print("Name: ", name)
    print("Staff ID: ", staffid)
    print("Description of issue: ", desc)



def created(tickets_created):
    tickets_created += 1
    print("tickets created {0}.\n".format(tickets_created))
    return tickets_created

b = input("tickets created is {0}.".format(tickets_created))

tickets_created = created(tickets_created)


def resolved(tickets_resolved):
    t = ticket_resolved + 1
    print("tickets resolved .\n",t)


def tosolve(tickets_tosolve):
    tickets_tosolve += 1
    print("tickets to solve {0}.\n".format(tickets_tosolve))
    return tickets_tosolve


# _Main_#
ch1 = 'Y'
while (ch1 == 'Y'):

    print(
        "Please select from following option \n 1.To submit a request \n 2.To Resolve a Ticket\n 3. To Display Ticket information \n 4.To display tickets Statisic")
    ch = int(input("Your Selection"))
    if (ch == 1):
        create_ticket()

    elif (ch == 2):
        resolved(tickets_resolved)
    elif (ch == 3):
        displayticket()
    elif (ch == 4):
        ticketstats()
    else:
        print("Please select from options available")
        print("Do you want to continue..Press Y")
        ch1 = input()
