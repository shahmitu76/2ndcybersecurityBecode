#Write a program that will take a string of digits and give you all the contiguous substrings 
# of length `n` in that string
def slices(number,counter):
    if counter==0 or counter>len(number):
        return ValueError("Invalid counter")
    else:
        j=0
        m=0
        main_list=[]
        list_example=[]
        for j in range(len(number)):
            if m<=len(number):
                i=0
                print(f"j is {j}") 
                print(f"lenght of number is is {len(number)}")
                for i in range(int(counter)):
                    print(f"i is{i}")
                    print(f"counter is {counter}")
                    list_example.append(number[m])
                    print(f"list example is {list_example}")
                    m+=1
                print(m)
                #m=m+1
                main_list.append(list_example)
                list_example=[]
                #print(f"main list  is {main_list}")
        return main_list

x=slices("1234",3)
print(x)






