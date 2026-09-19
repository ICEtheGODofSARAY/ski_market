from cryptography.fernet import Fernet

key = "ZlfNYpZ84mBbZtwp3HflMF-thAMi0_sMm_5gvgDz9b0="
#
#
cipher = Fernet(key)
#
# text = input("Введите текст: ").encode()
#
# encrypted = cipher.encrypt(text)
#
# print("Зашифровано:", encrypted.decode())
#
# decrypted = cipher.decrypt(encrypted).decode()
decrypted = cipher.decrypt(
    "gAAAAABqrrqnCqioYE3P9F0VzRgICl8RagOo42hixYpCwgPoAnLwNIikB3OWlALdec9k3o9iid2tt7YyIO-UBkriTR2uRj4qcPREC8G-VpcveYewWX1xybI=").decode()
#
print("Расшифровано:", decrypted)
