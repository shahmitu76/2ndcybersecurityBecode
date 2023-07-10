import unittest
name="Alan Turing"
age=42
person=[name,age,"mathematician"]
print(person)
text= "Hello, my name is {0},I am {1} years old and I am a {2}.".format(person[0],person[1],person[2])
print(text)
age_type=type(age)
print(age_type)
if unittest.assertequal(name, "Alan Turing")==1:
    print(success)