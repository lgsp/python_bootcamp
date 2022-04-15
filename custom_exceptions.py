class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dog_name = input("What is your dogs name: ")
    if any(char.isdigit() for char in dog_name):
        raise DogNameError
except DogNameError:
    print("Your dogs name can't contain a number")

        
    
