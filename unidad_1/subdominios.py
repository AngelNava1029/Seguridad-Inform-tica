'''
programas para encontrar los subdominios de un sitio.
explicar que hace este script.
desarrollado por Angel Nava
'''
import requests
from os import path
import argparse
import sys

parse = argparse.ArgumentParser()

parse.add_argument('-t','--target',help='indica el dominio de la vistima')
parse=parse.parse_args()


def main():
    if parse.target:
        if path.exists('subdominios.txt'):
            wordlist= open('subdominios.txt','r')
            wordlist= wordlist.read().split('\n')

            for subdominio in wordlist:
                url="http://" + subdominio + "." + parse.target 
                #print(url)

                try:
                    requests.get(url ,timeout=3)
                except requests.ConnectionError: pass
                else: print("se encontro un subdominio: " + url)
            
            for subdominio in wordlist:
                url="https://" + subdominio + "." + parse.target 
                #print(url)

                try:
                    requests.get(url ,timeout=3)
                except requests.ConnectionError: pass
                else: print("se encontro un subdominio: " + url)

        else: print("no se encontro el archivo que contiene los archivos a buscar")
    else: print("no hay vistima")    

if __name__ == "__main__" :
    try :
        main()
    except KeyboardInterrupt : 
        sys.exit()    
             