# A function named concatenate_args that takes any number of string arguments in
# positional arguments format and concatenates them into a single string

def concatenate_args(*words):
    for word in words:
        print(f"My name is {word}")
    
#  A function named concatenate_kwargs that takes any number of string arguments 
#  in keyword arguments  format and concatenates them into a single string   
    
def concatenate_kwargs(**kwargs):
    for key,value in kwargs.items():
                print(f"{key}:{value}")

        
