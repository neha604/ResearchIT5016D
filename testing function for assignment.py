import csv

class user():
    #constructer
    def __init__(self):
        self.staff_name=staff_name
        self.ID=ID
        self.email=email
        self.description=description
        self.ticketNo
        self.ticket_submit=0
        self.ticket_resolved=0
        self.ticket.open=0


    def get_details(self):
        self.staff_name   = input("Enter Name   : ")
        self.ID            =input("enter ID  :  ")
        self.email         =input("enter email : ")
        self.description: str = input("description of the issue  ")
        self.ticketno= 2000+1

    def passw(self):
        Y = self.ID[0:2]
        Z = self.staff_name[0:3]
        p = Y + Z

        passw(8978,neha)
        print("your new password is", p)



#child class
class IThelpdesk(user):
    def __init__(self,staff_name,ID,email,description,):
        super().__init__(staff_name,ID,email,description,)
        self.ticket_created=0

    def ticket(self,submit):
        self.submit = 1
        self.ticket_created=self.ticket_created+self.submit
        print("ticket created : ",self.ticket_created)



def solved(self,submit):
        self.submit=1
        if self.submit>self.ticket_created:
            print("No ticket to resolve: ticket created : " ,self.ticket_created)
        else:
            self.ticket_created=self.ticket_created-self.submit
            print("ticket Resolved :", self.ticket_created)









