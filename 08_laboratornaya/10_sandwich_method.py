encrypted_message = input('Введите зашифрованное сообщение: ')
decrypted_message = ''
if len(encrypted_message) % 2 == 0:
    for i in range(1, len(encrypted_message) + 1, 2):
        decrypted_message += encrypted_message[i - 1]
    for i in range(len(encrypted_message), 0, -2):
        decrypted_message += encrypted_message[i - 1]
if len(encrypted_message) % 2 == 1:
    for i in range(1, len(encrypted_message) + 1, 2):
        decrypted_message += encrypted_message[i - 1]
    for i in range(len(encrypted_message) - 1, 0, -2):
        decrypted_message += encrypted_message[i - 1]
print('Расшифрованное сообщение:', decrypted_message)