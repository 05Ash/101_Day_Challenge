import string

password=string.ascii_lowercase

def decode_encode(message,key,type):

    final_message=""
    key = key if type else key*(-1)
    for char in message:
        index=password.find(char)
        final_message+=password[(index+key)%26]

    return final_message

cipher_art="""
             ___   __   ____  ____   __   ____     ___  __  ____  _  _  ____  ____
            / __) / _\ (  __)/ ___) / _\ (  _ \   / __)(  )(  _ \/ )( \(  __)(  _ \\
           ( (__ /    \ ) _) \___ \/    \ )   /  ( (__  )(  ) __/) __ ( ) _)  )   /
            \___)\_/\_/(____)(____/\_/\_/(__\_)   \___)(__)(__)  \_)(_/(____)(__\_)
"""
