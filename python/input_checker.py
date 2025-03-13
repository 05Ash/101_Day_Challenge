correct_input = False
def input_is_int(data):
    while not correct_input:
        try:
            data = int(data)
            return data
        except ValueError:
            data = input("Invalid input!!!\nEnter again: ")

def input_in_collection(data, collection):
    while not correct_input:
        if data in collection:
            return data
        else:
            data = input("Invalid input!!!\nEnter again: ")
