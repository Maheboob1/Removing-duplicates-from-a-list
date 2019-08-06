class Employee:
    No_of_emps=0
    raise_amt=1.04
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=fname+"."+lname+"@company.com"
    No_of_emps +=1

    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)


emp_1=Employee("Maheboob","Tumkur",45000)
emp_2=Employee("Luqman","Tumkur",50000)


print(Employee.fullname(emp_2))