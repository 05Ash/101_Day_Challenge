import cipher

print(cipher.cipher_art)

encryption_type=["decrypt","encrypt"]

while True:

    type=input("Do you want to encrypt or decrypt.\nPress 1 to encrypt and 0 to decrypt, and any other character to exit: ")

    if type not in "01":
        break


    message=(input(f"Please enter the message you want to {encryption_type[int(type)]}, without any spaces: ")).lower()

    if not message.isalpha():
        print("Incorrect Input!!!\n Please Try Again!!!")
        continue

    key=input("Please enter the key: ")

    if not key.isdigit():
        print("Incorrect Input!!!\n Please Try Again!!!")
        continue

    final_message=cipher.decode_encode(message,int(key),int(type))

    print(f"Your {encryption_type[int(type)]}ed is {final_message}.")
