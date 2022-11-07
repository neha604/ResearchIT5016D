#tickets stats

tickets_created=0

def statistic(tickets_created):
    tickets_created+=1
    print("tickets created {0}.\n".format(tickets_created))

    return tickets_created

x=input("tickets created is {0}.".format(tickets_created))

tickets_created = statistic(tickets_created)

tickets_created = statistic(tickets_created)


#tickets_resolved

tickets_resolved=0


def resolved(tickets_resolved):
    tickets_resolved+=1
    print("tickets resolved {0}.\n".format(tickets_resolved))

    return tickets_resolved

x=input("tickets resolved is {0}.".format(tickets_resolved))

tickets_resolved= resolved (tickets_resolved)

tickets_resolved= resolved (tickets_resolved)
