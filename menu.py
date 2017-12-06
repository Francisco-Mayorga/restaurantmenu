# coding=utf-8

print "Bienvenido al programa menu"

menu = {}

while True:
    platodeldia = raw_input("Escriba aquí el plato del día: ")
    preciodelplato = raw_input("El precio del {} es: ".format(platodeldia))
    print "El plato del día es: " + platodeldia
    print "El precio del plato es: " + preciodelplato
    menu[platodeldia] = preciodelplato

    print " menu: {}" .format(menu)


    nuevo = raw_input("¿quieres escribir un nuevo plato del día? (si/no) ")

    if nuevo.lower() == "no":
        break

with open("menu.txt", "w+") as menu_file:
    menu_file.write("Menú del día:\n")
    for platodeldia in menu:
        menu_file.write("{}: {} Euros".format(platodeldia, preciodelplato))