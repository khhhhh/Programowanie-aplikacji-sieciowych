import shutil

fileName = input()
try:
    shutil.copy(fileName ,"lab1zad2.png")
except:
    print("Taki plik nie został znalieziony!")
