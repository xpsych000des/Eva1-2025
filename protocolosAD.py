OSPF=110
EIGRP=90
BGP=20
protocolo=input("Ingresa el nombre del protocolo para conocer su distancia administrativa (OSPF - EIGRP - BGP). Procura usar mayúsculas para que el valor sea válido:")
if protocolo=="OSPF":
    print(f"La distancia administrativa es {OSPF}")
elif protocolo=="EIGRP":
    print(f"La distancia administrativa es {EIGRP}")
elif protocolo=="BGP":
    print(f"La distancia administrativa es {BGP}")
else:print("El protocolo que usted ha ingresado no es válido")