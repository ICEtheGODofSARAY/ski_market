from cryptography.fernet import Fernet
from django.shortcuts import redirect, render
from cipher.forms import ContactForm, KeyForm, CipherForm


def contact(request):
    key_form = KeyForm(request.POST)
    cipher_form = CipherForm(request.POST)
    if request.method == "POST" and key_form.is_valid():
        print(key_form.cleaned_data)
    if request.method == "POST" and cipher_form.is_valid():
        print(cipher_form.cleaned_data)
        cipher = Fernet("ZlfNYpZ84mBbZtwp3HflMF-thAMi0_sMm_5gvgDz9b0=")
        decrypted = cipher.decrypt("gAAAAABqrrqnCqioYE3P9F0VzRgICl8RagOo42hixYpCwgPoAnLwNIikB3OWlALdec9k3o9iid2tt7YyIO-UBkriTR2uRj4qcPREC8G-VpcveYewWX1xybI=").decode()
        print("Расшифровано:", decrypted)
    return render(request, "cipher/contact.html", {"key_form": key_form, "cipher_form": cipher_form})