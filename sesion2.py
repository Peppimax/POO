class Smart:
    def __init__(self, tipo, serial, costo) -> None:
        self.tipo = tipo
        self.serial = serial
        self.costo = costo

    def __str__(self) -> str:
        return f"Objeto: {self.serial}"    
    
    def actualizar_costo(self, costo):
        if costo > 500000:
           self.costo = costo
        else:
            print("Costo no valido... Digite un valor mayor a 500000")



if __name__ == "__main__":
    dispositivos = []
    print("-"*60)
    while True:
                                                         #Se usan para que no hallan problemas con las Mayus-Minus                                                 #lower
        op = input("¿ Quiere agragar otro ?  S/N: ").upper()
        if op == "S":
            #CREAMOS UN OBJETO Y LISTA
            tipo = input("Tipo de dispositivo : ")
            serial = input("Serial del dispositivo: ")
            costo = int(input("Costo del dispositivo: "))
            obj = Smart(tipo, serial, costo)
            dispositivos.append(obj)
        elif op == "N":
            break
        else:
            pass    
    for s in dispositivos:
        print(s)    # Aqui me refiero al objeto completo


    print("-"*60)

    #Resto de operaciones CRUD
    while True:
        op =int(input("""Que desea hacer:
                      1. Buscar y actualizar
                      2. Eliminar
                      3. Salir
                      """))
        if op == 3:
            break
        elif op == 1:
            #Buscar y editar
            serial = input("Digite el serial a buscar: ")
            for s in dispositivos:
                if serial == s.serial:
                   print(f"Encontrado!! Objeto: {s.tipo} - {s.serial} - {s.costo}")
                   costo = int(input("Digite el nuevo costo: "))
                   s.actualizar_costo(costo)
                   break
            else:
                print("No encontrado...")          

        elif op == 2:
            #Eliminar: pop(eliminar por indice), remove (eliminar por valores)
            tam = len(dispositivos)
            contador = 0
            for s in dispositivos:
                contador
                print (f"{contador}. objetos: {s.tipo} - {s.serial} - ${s.costo}")
                contador += 1
            borrar =int(input(f"Cual objeto quiere eliminar? 1-{tam} "))#(f) Salida predevariable
            dispositivos.pop(borrar-1)
        else:
            print("Opcion Incorrecta, selecciona de nuevo")
        
