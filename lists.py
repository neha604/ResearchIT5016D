ticket_submit=0
ticket_resolved=0
ticket_reopen=0

class Ticket:
    def __init__(self,staffID,tcname,email,description):
        self.ID=(staffID)
        self.name=(tcname)
        self.contact=(email)
        self.issue=(description)

        if "password change" in description:
            print("yyy")
        else :
            print("yuoijhn")
 return (self)




def information (ID: object, name: object, email: object, description: object) -> object:
       print("printing tickets")


staffID: str= input("staffID  ")
tcname: str=input("ticket creater name  ")
email: str=input("contact email  ")
description: str=input("description of the issue  ")


Y=staffID[0:2]
Z=tcname[0:3]
p=Y+Z
print("your new password is" ,p)


information(staffID,tcname,email,description)

