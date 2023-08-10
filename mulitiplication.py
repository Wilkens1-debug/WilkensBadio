while True:
    a = int(input("Entrer votre nombre : "))
    nombre = 1
    print(f"La multiplication de {a} est: ")

    while nombre <= 10:
        r = a * nombre
        print(f"{a} * {nombre} = {r}")
        nombre += 1
    continuer = input("Voulez-vous continuer ? (Taper 'W' pour continuer, 'N' pour arrêter) ")
    if continuer.upper() != 'W':
        break
          
          
