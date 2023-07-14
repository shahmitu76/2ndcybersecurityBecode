'''def hello(*name):
    if name:
        return 'Hello, '+ name[0] +'!'
        
    else:
        return 'Hello, World!'
        

'''
def hello(name): #doesn't work...one above works
    if len(name)==0:
        print(f"The string lenght is {len(name)}")
        return 'Hello, World!'  
    else:
        return 'Hello, '+ name +'!' 
        
