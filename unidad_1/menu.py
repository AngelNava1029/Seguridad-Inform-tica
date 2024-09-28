import os
opcion="0"
while opcion !=7:
    os.system("cls")
    
    print("Sistema Para Pruebas De Seguridad Informatico")
    print("Version 1.0 Desarrollado por Angel Nava")
    print("1. Busqueda de subdominios")
    print("2. Banner grabing")
    print("3.Wad")
    print("4.Escaneo de puertos")
    print("5.GetIp")
    print("6.GetIp2")
    print("7.Salir")

    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
      vistima= input("sea tan amable de indicar el subdominio:")
      os.system('python subdominios.py -t' + vistima) 
      input("presione enter para continuar") 
    elif opcion == 2:
        print("2")
    elif opcion == 3:
        print("3")
    elif opcion == 4:
        print("4")
    elif opcion == 5:
        vistima= input("sea tan amable de indicar la URL:")
        os.system('python getIp.py -t' + vistima) 
        input("presione enter para continuar") 
    elif opcion == 6:
        vistima= input("sea tan amable de indicar la URL:")
        os.system('python getIp2.py -t' + vistima) 
        input("presione enter para continuar")
print("finalizando") 