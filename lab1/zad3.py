import re
ip = input("Podaj adres IP: ")
if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
    print("Adres IP jest poprawny")
else:
    print("Adres IP jest niepoprawny")