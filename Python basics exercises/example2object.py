'''x = 10  # Creating the int() instance
y = 5
print(id(x), id(y))
print(x is y)  # comparing the types '''
'''person = ["James", "Bond", "007", "Secret agent"]
person_copy = person
 print(id(person), id(person_copy))  
person += ["English"]
person_copy += ["Man"]
print(id(person), id(person_copy))
print(person, person_copy)
''' 

def hello(name):  # <- Parameter
    print(f"Hello {name} and welcome")
hello("Alan")  # <- Argument