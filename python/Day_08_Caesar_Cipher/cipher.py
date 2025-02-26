import string

password=string.ascii_lowercase

def decode_encode(message,key,type):

    final_message=""

    key = key if type=="encode" else key*(-1)

    for char in message:
        index=password.find(char)
        if char.isalpha():
            final_message += password[(index+key)%26]
        else:
            final_message += char
    return final_message

cipher_art="""
             ___   __   ____  ____   __   ____     ___  __  ____  _  _  ____  ____
            / __) / _\ (  __)/ ___) / _\ (  _ \   / __)(  )(  _ \/ )( \(  __)(  _ \\
           ( (__ /    \ ) _) \___ \/    \ )   /  ( (__  )(  ) __/) __ ( ) _)  )   /
            \___)\_/\_/(____)(____/\_/\_/(__\_)   \___)(__)(__)  \_)(_/(____)(__\_)
"""
