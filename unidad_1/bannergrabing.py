import socket
import sys
import argparse

parse= argparse.ArgumentParser()
parse.add_argument("-t","--target" ,help="introduzca una ip")
parse=parse.parse_args()

def banner(ip,port): 
    s=socket.socket()
    s.connect((ip,port))
    print(str(s.recv(1024)))

def main():
    
    if parse.target:
        ip=parse.target
        #ip = socket.gethostbyname(parse.target)
        port=21

        banner(ip,port)
    else:
        print("ingrese un ip para continuar")    