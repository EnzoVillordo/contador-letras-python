#Se creara un codigo para validar la edad del usuario. Si es mayor puede ingresar, si no es mayor, no esta permitido el ingreso

edad_usuario = int(input("Bienvenido, por favor ingrese su edad para validar el ingreso: "))

permitido = True if edad_usuario >= 18 else False

if permitido:
    print("Puede ingresar al establecimiento")
else:
    print("No puede ingresar al establecimiento")
