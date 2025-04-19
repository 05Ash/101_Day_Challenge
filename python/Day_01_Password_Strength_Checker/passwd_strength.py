import string

# Variable declarations
# uppercase_chars = string.ascii_uppercase
# lowercase_chars = string.ascii_lowercase
# digits = string.digits
# special_characters = string.punctuation
# password_length : 0

class Chars:
    def __init__(self, chars_collection, input):
        self.chars_type = getattr(string, chars_collection, None)
        self.count = 0
        self.paswd = input
    def char_counter(self):
        for char in self.paswd:
            if char in self.chars_type:
                self.count += 1
        print(self.count)

class Passwords:
    def __init__(self, input):
        self.password = input
        self.length = len(input)
        self.strength = None
        self.feedback = None
        self.char_types = ["ascii_uppercase", "ascii_lowercase", "digits", "punctuation"]
        self.char_classes = [Chars(char_type, self.password) for char_type in self.char_types]
    def strength_calculator(self):
        if self.length < 6:
            self.strength = "Weak"
            self.feedback = "Try again!"
        elif




class1 = Passwords("Ashish")

class1.strength_calculator()


# def calculate_chars(string_to_test, char_type):

#     counter = 0
#     for char in string_to_test:
#         if char in char_type:
#             counter += 1
#     return counter
# password_properties ={
#     "uppercase" : {
#         "chars_type" : string.ascii_uppercase,
#         "count" : 0
#     },
#     "lowercase" : {
#         "chars_type" : string.ascii_lowercase,
#         "count" : 0
#     },
#     "digits" : {
#         "chars_type" : string.digits,
#         "count" : 0,
#     },
#     "special" : {
#         "chars_type" : string.punctuation,
#         "count" : 0,
#     }
# }

# list_of_passwords = []



# password = input("Please enter the password you want to check: ")
# password_length = len(password)

# for property in password_properties:
#     property[]
