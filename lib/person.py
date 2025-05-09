
#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Person", job="Sales"):
        if not isinstance(name, str) or len(name.strip()) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            self.name = "Person"
        else:
            self.name = name.title()
        
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self.job = "Sales"
        else:
            self.job = job
    
    def talk(self):
        print("Hello World!")
    
    def walk(self):
        print("The person is walking.")