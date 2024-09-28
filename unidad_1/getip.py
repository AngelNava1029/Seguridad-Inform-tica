
#primera forma:nslookup(url)
#primera forma:nslookup.io
#tercera forma mxtoolbox.com
#cuarta forma pythoncodigo

import socket
import argparse
import sys

parse= argparse.ArgumentParser()
parse.add_argument("-t", "--target", help="ingrese la URL sin http")
parse=parse.parse_args()

def getIpLokochon(url):
    try:
        ip = socket.gethostbyname(url)
        print(f"la direccion ip de la {url} es {ip}")
    except:
        print("no se pudo obtener la Ip")

def main():
    if parse.target:
        getIpLokochon(parse.target)

    else:
        print("ingrese una direccion ip sin http")

if __name__ == "__main__" :
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()