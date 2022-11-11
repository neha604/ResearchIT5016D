import copy

class address:
    def __init__(self,street_address,suite,city):
        self.street_address=street_address
        self.suite=suite
        self.city=city

    def __str__(self):
        return f'{self.street_address},{self.suite},{self.city}'

class Employee():
    def __int__(self,name,address):
        self.name=name
        self.address=address

    def __str__(self):
        return f'{self.name},{self.address}'

class EmployeeFactory:
    main_office_employee=Employee('', address("12A east Dr",0,"london"))
    aux_office_employee= Employee('',address("13a east Dr",0,"london"))

    @staticmethod

    def __newemployee(proto,name,suite):
        result=copy.deepcopy(proto)
        result.name=name
        result.address.suite=suite
        return result

    @staticmethod

    def new_main_office_e(name,suite):
        return EmployeeFactory.__newemployee(EmployeeFactory.main_office_employee,name,suite)


    @staticmethod

    def new_aux_office_e(name,suite):
        return EmployeeFactory.__newemployee(EmployeeFactory.aux_office_employee,name,suite)

if __name__==' __main__':
    john=EmployeeFactory.new_main_office_e("john",100)
    jane=EmployeeFactory.new_aux_office_e("Jane",900)
    print(john)
    print(jane)