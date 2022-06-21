import shutil

print("Wpisz nazwe pliku:", end="")
fileName = input()
try:
    shutil.copy(fileName ,"lab1zad1.txt")
except:
    print("Taki plik nie został znalieziony!")
