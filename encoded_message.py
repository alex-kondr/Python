message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
# not_encoded = (" ", "!", ",")
encoded_message = ""
for ch in message:
    if ch.isalpha():
        if ch.islower():
            pos = ord(ch) - ord("a")  
            pos = (pos + offset) % 26
            ch = chr(pos + ord("a"))
            # pri
        else:
            pos = ord(ch) - ord("A")        
            pos = (pos + offset) % 26
            ch = chr(pos + ord("A"))

    encoded_message += ch
print(encoded_message)