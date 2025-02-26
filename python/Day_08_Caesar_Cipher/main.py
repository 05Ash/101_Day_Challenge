import cipher

print(cipher.cipher_art)

while True:

    encryption_type = (input("\nDo you want to encode or decode.\nPress any other character to exit.\n")).lower()
    if encryption_type not in ["encode", "decode"]:
        break

    message = (input(f"\nPlease enter the message you want to {encryption_type}, without any spaces:\n")).lower()

    key = input("\nPlease enter the key:\n")

    while not key.isdigit():
        print("Incorrect Input!!!\n Please Try Again!!!")
        continue

    final_message=cipher.decode_encode(message,int(key),encryption_type)

    print(f"\nYour {encryption_type}d message is {final_message}.")
