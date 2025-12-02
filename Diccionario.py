consig = []
retiro = []
dic = {10901: {"nombres": "Catalina Forero", "contraseña": "Qwe1rt#a", "pin": 613902, "saldo": 10000}, 
       11123: {"nombres": "Miguel Triana", "contraseña": "A123bx$n", "pin": 190100, "saldo": 20000}}

crd = int(input("Bienvenido al sistema (tiene 3 oportunidades máximo para ingresar sus credenciales: "))
cont = 3
while(cont != 0):
    if (crd in dic):
        contr = input("Ingrese su contraseña: ")
        while(crd != dic[crd]["contraseña"] and cont != 0):
            if (contr in dic[crd]["contraseña"]):   
                print("---Menu Principal---")
                print("1. Ver saldo")
                print("2. Consignar")
                print("3. Retirar") 
                print("4. Ver movimientos")  
                print("5. Salir")
                
                opc = int(input("Digite una opcion del menú: "))
                while(opc != 5):
                    
                    match opc:
                        case 1:
                            print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                            
                            print("---Menu Principal---")
                            print("1. Ver saldo")
                            print("2. Consignar")
                            print("3. Retirar") 
                            print("4. Ver movimientos")  
                            print("5. Salir")
                            
                            opc = int(input("Digite una opcion del menú: "))
                            while(opc != 5):
                                
                                match opc:
                                    case 1:
                                        print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                        break
                                    
                                    case 2:
                                        print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                        add = int(input("Digite la cantidad de dinero a consignar (minimo $5000): "))
                                        while(add < 5000):
                                            print("El saldo a consignar es menor al monto minimo $5000")
                                            add = int(input("Digite la cantidad de dinero a consignar (minimo $5000): "))
                                        consig.append(add)
                                        dic[crd]["saldo"] += add
                                        print(f"La consignacion fue exitosa su saldo actual es de: ${dic[crd]["saldo"]}")
                                        break
                                    
                                    case 3:
                                        print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                        ret = int(input("Digite la cantidad de dinero a retirar (minimo $5000): "))
                                        while(ret < 5000):
                                            print("El saldo a retirar es menor al monto minimo $5000")
                                            ret = int(input("Digite la cantidad de dinero a retirar (minimo $5000): "))
                                        
                                        retiro.append(ret)
                                        dic[crd]["saldo"] -= ret
                                        print(f"El retiro fue exitoso su saldo actual es de: ${dic[crd]["saldo"]}")
                                        break
                                    
                                    case 4:
                                        print("---MOVIMIENTOS---")
                                        print(f"Sus consignaciones fueron: {consig}")
                                        print(f"Sus retiros fueron: {retiro}")   
                                        break
                                            
                                    case 5:
                                        break
                            break
                        
                        case 2:
                            print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                            add = int(input("Digite la cantidad de dinero a consignar (minimo $5000): "))
                            while(add < 5000):
                                print("El saldo a consignar es menor al monto minimo $5000")
                                add = int(input("Digite la cantidad de dinero a consignar (minimo $5000): "))
                            consig.append(add)
                            dic[crd]["saldo"] += add
                            print(f"La consignacion fue exitosa su saldo actual es de: ${dic[crd]["saldo"]}")
                            
                            print("---Menu Principal---")
                            print("1. Ver saldo")
                            print("2. Consignar")
                            print("3. Retirar") 
                            print("4. Ver movimientos")  
                            print("5. Salir")
                            
                            opc = int(input("Digite una opcion del menú: "))
                            while(opc != 5):
                                
                                match opc:
                                    case 1:
                                        print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                        break
                                    
                                    case 2:
                                        print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                        add = int(input("Digite la cantidad de dinero a consignar (minimo $5000): "))
                                        while(add < 5000):
                                            print("El saldo a consignar es menor al monto minimo $5000")
                                            add = int(input("Digite la cantidad de dinero a consignar (minimo $5000): "))
                                        consig.append(add)
                                        dic[crd]["saldo"] += add
                                        print(f"La consignacion fue exitosa su saldo actual es de: ${dic[crd]["saldo"]}")
                                        break
                                    
                                    case 3:
                                        print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                        ret = int(input("Digite la cantidad de dinero a retirar (minimo $5000): "))
                                        while(ret < 5000):
                                            print("El saldo a retirar es menor al monto minimo $5000")
                                            ret = int(input("Digite la cantidad de dinero a retirar (minimo $5000): "))
                                        
                                        retiro.append(ret)
                                        dic[crd]["saldo"] -= ret
                                        print(f"El retiro fue exitoso su saldo actual es de: ${dic[crd]["saldo"]}")
                                        break
                                    
                                    case 4:
                                        print("---MOVIMIENTOS---")
                                        print(f"Sus consignaciones fueron: {consig}")
                                        print(f"Sus retiros fueron: {retiro}")   
                                        break
                                            
                                    case 5:
                                        break
                            break
                        
                        case 3:
                            print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                            ret = int(input("Digite la cantidad de dinero a retirar (minimo $5000): "))
                            while(ret < 5000):
                                print("El saldo a retirar es menor al monto minimo $5000")
                                ret = int(input("Digite la cantidad de dinero a retirar (minimo $5000): "))
                            
                            retiro.append(ret)
                            dic[crd]["saldo"] -= ret
                            print(f"El retiro fue exitoso su saldo actual es de: ${dic[crd]["saldo"]}")
                            
                            print("---Menu Principal---")
                            print("1. Ver saldo")
                            print("2. Consignar")
                            print("3. Retirar") 
                            print("4. Ver movimientos")  
                            print("5. Salir")
                            
                            opc = int(input("Digite una opcion del menú: "))
                            while(opc != 5):
                                
                                match opc:
                                    case 1:
                                        print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                        break
                                    
                                    case 2:
                                        print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                        add = int(input("Digite la cantidad de dinero a consignar (minimo $5000): "))
                                        while(add < 5000):
                                            print("El saldo a consignar es menor al monto minimo $5000")
                                            add = int(input("Digite la cantidad de dinero a consignar (minimo $5000): "))
                                        consig.append(add)
                                        dic[crd]["saldo"] += add
                                        print(f"La consignacion fue exitosa su saldo actual es de: ${dic[crd]["saldo"]}")
                                        break
                                    
                                    case 3:
                                        print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                        ret = int(input("Digite la cantidad de dinero a retirar (minimo $5000): "))
                                        while(ret < 5000):
                                            print("El saldo a retirar es menor al monto minimo $5000")
                                            ret = int(input("Digite la cantidad de dinero a retirar (minimo $5000): "))
                                        
                                        retiro.append(ret)
                                        dic[crd]["saldo"] -= ret
                                        print(f"El retiro fue exitoso su saldo actual es de: ${dic[crd]["saldo"]}")
                                        break
                                    
                                    case 4:
                                        print("---MOVIMIENTOS---")
                                        print(f"Sus consignaciones fueron: {consig}")
                                        print(f"Sus retiros fueron: {retiro}")   
                                        break
                                            
                                    case 5:
                                        break
                            break
                        
                        case 4:
                            print("---MOVIMIENTOS---")
                            print(f"Sus consignaciones fueron: {consig}")
                            print(f"Sus retiros fueron: {retiro}")   
                            
                            print("---Menu Principal---")
                            print("1. Ver saldo")
                            print("2. Consignar")
                            print("3. Retirar") 
                            print("4. Ver movimientos")  
                            print("5. Salir")
                            
                            opc = int(input("Digite una opcion del menú: "))
                            while(opc != 5):
                                
                                match opc:
                                    case 1:
                                        print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                        
                                        print("---Menu Principal---")
                                        print("1. Ver saldo")
                                        print("2. Consignar")
                                        print("3. Retirar") 
                                        print("4. Ver movimientos")  
                                        print("5. Salir")
                                        
                                        opc = int(input("Digite una opcion del menú: "))
                                        while(opc != 5):
                                            
                                            match opc:
                                                case 1:
                                                    print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                                    break
                                                
                                                case 2:
                                                    print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                                    add = int(input("Digite la cantidad de dinero a consignar (minimo $5000): "))
                                                    while(add < 5000):
                                                        print("El saldo a consignar es menor al monto minimo $5000")
                                                        add = int(input("Digite la cantidad de dinero a consignar (minimo $5000): "))
                                                    consig.append(add)
                                                    dic[crd]["saldo"] += add
                                                    print(f"La consignacion fue exitosa su saldo actual es de: ${dic[crd]["saldo"]}")
                                                    break
                                                
                                                case 3:
                                                    print(f"Su saldo es de: ${dic[crd]["saldo"]}")
                                                    ret = int(input("Digite la cantidad de dinero a retirar (minimo $5000): "))
                                                    while(ret < 5000):
                                                        print("El saldo a retirar es menor al monto minimo $5000")
                                                        ret = int(input("Digite la cantidad de dinero a retirar (minimo $5000): "))
                                                    
                                                    retiro.append(ret)
                                                    dic[crd]["saldo"] -= ret
                                                    print(f"El retiro fue exitoso su saldo actual es de: ${dic[crd]["saldo"]}")
                                                    break
                                                
                                                case 4:
                                                    print("---MOVIMIENTOS---")
                                                    print(f"Sus consignaciones fueron: {consig}")
                                                    print(f"Sus retiros fueron: {retiro}")   
                                                    break
                                                        
                                                case 5:
                                                    break
                                        break
                                
                        case 5:
                            break
                break
        
                
            else:    
                print(f"Documento invalido digite de nuevo")
            cont = cont - 1
            contr = input(f"Ingrese su contraseña le quedan {cont} oportunidades: ")
    else:
        print("Credencial invalida")
        cont = cont - 1
        crd = int(input(f"Ingrese sus credenciales le quedan {cont} oportunidades: "))
    
