from collections import namedtuple
import datetime

#Guardamos las tuplas y diccionario 
SEPARADOR=('*'*50+'\n')
articulo = namedtuple("articulo",("Descripcion","Piezas","Precioventa"))

Ventas = {}
# Inicio del Menu

while True:
    print(SEPARADOR)
    print("MENÚ")
    print("1) Agregar datos")
    print("2) Consulta")
    print("4) Salir")
    respuesta = int(input("Elija una opción: "))
#Funcion del registro y abrimos una lista vacia 
    if respuesta == 1:
        Articulos_venta = []
        print(SEPARADOR)
        clave = input('ingrese una clave:')
        print(clave)
        fecha= datetime.datetime.now()
        fecha=fecha.strftime('%d/%m/%Y %H:%M:%S')
        print(fecha)
        Articulos_venta.append(fecha)
        TOTAL=0
        #Gurdamos los datos
        while True:
            print(SEPARADOR)
            descripcion = input("Introduzca la descripcion del articulo:\n")
            print(SEPARADOR)
            cantidad = float(input("Ingrese cantidad a vender del tipo de llanta:\n"))
            print(SEPARADOR)
            precio = float(input("Ingrese precio (sin IVA) por unidad:\n »$"))
            Venta=articulo(descripcion,cantidad,precio)
            TOTAL=TOTAL+precio*cantidad
            Articulos_venta.append(Venta)
            #Guardamos los datos 
            print(SEPARADOR)
            continuar = input ('Desea agregar otro(s) articulos?(S/N):')
            #Operaciones aritmeticas para determinar el precio de la compra
            if continuar == 'N':
                print(f'Precio sin IVA : $ {TOTAL}\n')
                IVA=TOTAL*16/100
                print(f'Iva de la compra : $ { IVA}\n')
                PRECIOFIN=TOTAL+IVA
                print(f'Precio total de compra : $ {PRECIOFIN}\n')
                Articulos_venta.append(TOTAL)
                venta_fin=[ valor for valor in Articulos_venta]
                Ventas[clave]=venta_fin
                print(Ventas)
                break
            
#Funcion de para hacer las consultas del registro 
    if respuesta == 2:
        while True:
            print(SEPARADOR)
            folio_consul = input('Ingrese el folio de la venta a consultar: \n')
            print('Venta consultada \n')
            consulta=[ valor for valor in Ventas[folio_consul]]
            print(consulta)
            TOTAL=consulta[-1]
            IVA=TOTAL*16/100
            TOTALFIN=TOTAL+IVA
            print(f'TOTAL : ${TOTAL}')
            print(f'IVA : ${IVA}')
            print(f'TOTAL FINAL : ${TOTALFIN}')
            continuar = input ('Desea consultar otra Venta?(S/N):')
            if continuar == 'N':
                break

#Funcion para salir del Menu 
    if respuesta == 3:
        break