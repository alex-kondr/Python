message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
decoded_message = ""
for ch in message:
    if ch.isalpha():
        if ch.islower():
            pos = ord("z") - ord(ch)
            pos = (pos + offset) % 26
            ch = chr(ord("z") - pos)
        else:
            pos = ord("Z") - ord(ch)
            pos = (pos + offset) % 26
            ch = chr(ord("Z") - pos)

    decoded_message += ch
print(decoded_message)
