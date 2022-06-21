import socket
import urllib.parse

def pizzaSize(val = 1):
    if val == '1':
        return "small"
    elif val == '2':
        return "medium"
    elif val == '3':
        return "large"
    return "small"

def extraToppings(val:str = ''):
    toppings = []
    for chr in val:
        if  chr == '1':
            toppings.append("bacon")
        elif chr == '2':
            toppings.append("chesse")
        elif chr == '3':
            toppings.append("onion")
        elif chr == '4':
            toppings.append("mushroom")
    return list(dict.fromkeys(toppings))

if __name__ == '__main__':

    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = 'httpbin.org'
    PORT = 80

    formStr = b""

    name = input('Wpisz imie:')
    formStr += b"custname=" + name.encode() + b"&"
    tel = input('Wpisz telefon:')
    formStr += b"custtel=" + tel.encode() + b"&"
    email = urllib.parse.quote(input('Wpisz email:'))
    formStr += b"custemail=" + email.encode() + b"&"
    print("Wybierz rozmiar:")
    print("1. small")
    print("2. medium")
    print("3. large")
    size = pizzaSize(input())
    formStr += b"size=" + size.encode() + b"&"
    print("Wpisz liczby dodatków (puste, jesli nie chcesz):")
    print("1. Bacon")
    print("2. extra cheese")
    print("3. onion")
    print("4. mushroom")
    extraTopps = extraToppings(input())
    for topping in extraTopps:
        formStr += b"topping=" + topping.encode() + b"&"


    time = urllib.parse.quote(input("Wpisz czas:"))
    formStr += b"delivery=" + time.encode() + b"&"
    instrucs = input("Wpisz instrukcje:")
    formStr += b"comments=" + instrucs.encode() + b"&"

    formStr  = formStr[0:len(formStr) - 1]
    strLen = str(len(formStr)).encode()

    print(formStr)
    message = b"POST /post HTTP/1.1 \r\n" + \
              b"User-agent: Version/7.0.3 Safari/7046A194A \r\n" + \
              b"HOST: httpbin.org \r\n" + \
              b"Content-Type: application/x-www-form-urlencoded \r\n" + \
              b"Content-Length: " + strLen + b" \r\n" + \
              b"\r\n" + \
              formStr + \
              b"\r\n"
    try:
        sockIPv4.connect((HOST, PORT))
        sockIPv4.sendall(message)
        retVal = sockIPv4.recv(8192)
        print(retVal)

    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)

    sockIPv4.close()