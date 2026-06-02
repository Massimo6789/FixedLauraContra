import random
caracteres = "zyx)(%&<wasujdnwuifgj*/+-1583.2.:;duyqwo9rnbhc°!"#$%&/()=?¡¿'¨*[][]gdcjuesncxqwpr"
longitud = int(input("Ingresa de que longitud quieres tu contraseña, por favor hazlo en números"))
contra = ""
nueva_contra = ""
for i in range(longitud):
    letras = random.choice(caracteres)
    contra += letras
print(contra)
#Cambie de nombre las variables cambio_contrasena y contrasena a cambio_contra y contra ya que se ve raro sin la enie y tambien es mas consistente a como las demas variables la llaman
cambio_contra = input("¿Deseas cambiar tu contraseña? Responde (si) o (no)")
#Cambie de nombre "nueva_longi" a "nueva_long" ya que es mas simple y depaso tambien se asimila a la palabre longitude que es la traduccion
if cambio_contra == "si":
    nueva_long = int(input("Ingresa de nuevo de qué longitud deseas tu contraseña, recuerda hacerlo en números"))
    for i in range(nueva_long):
        nuevas_letras = random.choice(caracteres)
        nueva_contra += nuevas_letras
    print(nueva_contra)
elif cambio_contra == "no":
    print ("Entendido, cambio realizado.")
    #Proyecto funciona sin ningun error eso es algo bueno.
    #El unico problema que tenia no era grande ya que solo eran cambios a variantes para que resalten mas y tambien para que sean consistentes.
    #Muy buen trabajo para el compa que haya hecho este proyecto.