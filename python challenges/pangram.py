import string
def is_pangram(string_example):
    if string_example=='':
        return False
    else:
       example_list= list(string.ascii_lowercase)
       i=0
       print(example_list)
       for element in example_list:
            if element in string_example.lower():
                print(element)
            else:
                return False
       return True

        

'''y=is_pangram('the quick brown fish jumps over the lazy dog')
print(y)
'''