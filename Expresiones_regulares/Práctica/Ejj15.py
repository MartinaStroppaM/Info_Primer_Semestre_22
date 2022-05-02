# Realizá un programa que validar si una cuenta de mail está escrita correctamente.

import re 

def validar_mail(mail):
    if (re.search("\w.*@\w*\.\w*", mail)) is not None:
        return "El mail ingresado es válido"
    else:
        return "Algo salió mal"

print(validar_mail("martism.2014@gmail.com"))