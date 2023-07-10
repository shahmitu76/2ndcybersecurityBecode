x=input("Please enter the phrase for which you need the acronym ")#getting input from the user
listofword=list(x) #Change the string input to list
acronym=[] #define an empty list
acronym.append(listofword[0]) #adding first letter of the phrase into the list
for n in range(0,(len(listofword)-1)): #for loop iterates for 1 counter less than the total length of list
    if listofword[n] ==" ":#finding the next word
        acronym.append(listofword[n+1])
    n+=1
finalacronym= "".join(acronym) #Changing array into string without spaces
print(finalacronym)