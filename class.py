class Intern:
    def __init__(self,name,role,company):
        self.name=name
        self.role=role
        self.company=company
    def __str__(self):
        return f"{self.name} is a {self.role} at {self.company}"
P=Intern("Prateek Maheshwari","Backend Intern","Delhivery")
print(P)
