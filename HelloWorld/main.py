def imprimir(texto):
    for x in range(1):
        print(texto)

imprimir("<Programando>.........")
imprimir("<concluido>")
def imprimir(texto):
    for x in range(1):
        print(texto)

def suma(numero1,numero2):
        return numero1 + numero2
imprimir(suma(1,0))

print ("Quieres aprender programacion?")
print("Si")

imprimir("<Programando>.........")
imprimir("<concluido>")
def imprimir(texto):
    for x in range(1):
        print(texto)

first_name = "Demian "
last_name = "Ragknos "
full_name = first_name +""+ last_name

print("Hola "+(full_name))
#print(type(first_name))
#print(type(last_name))

imprimir("<Programando>.........")
imprimir("<concluido>")
def imprimir(texto):
    for x in range(1):
        print(texto)

age = 1
#age += 0
print("Tu nivel de usuario es: "+str(age))
#print(type(age))

imprimir("<Programando>.........")
imprimir("<concluido>")
def imprimir(texto):
    for x in range(1):
        print(texto)

height = 1.99  #print("%")
print("Tu porcentaje en esta leccion es: "+str(height)) 
print("%")
#print(type(height)("%"))

imprimir("<Programando>.........")
imprimir("<concluido>")
def imprimir(texto):
    for x in range(1):
        print(texto)

human = "si"
print("Eres un Humano? "+str(human))
#print(type(human))

imprimir("<Programando>.........")
imprimir("<concluido>")
def imprimir(texto):
    for x in range(1):
        print(texto)

nombre = "Demian"
Dia = "Sabado 11 de Marzo de 2023"
Programador = "Si"

nombre, Dia, Programador = "Demian", "Sabado 11 de Marzo de 2023", "Si"

print("Tu nombre es:")
print(nombre)
print("Hoy es: ")
print(Dia)
print("Eres programador?")
print(Programador)

imprimir("<Programando>.........")
imprimir("<concluido>")
def imprimir(texto):
    for x in range(1):
        print(texto)


#("este_vale") = 20
#("y_esto_vale") = 30
#("Y_esto_vale") = 40

#= ("esto_vale") = 20
#= ("y_esto_vale") = 30
#= ("Y_esto_vale") = 40
print ("esto_vale =20")
print ("y_esto_vale = 30")
print ("Y_esto_vale = 40")

print("Tu nombre tiene:")
print(len(nombre))
print("digitos")
print("La i se encuentra un digito despues de:")
print(nombre.find("i"))
print(nombre.capitalize())
print(nombre.upper())
print(nombre.lower())
print("Tu nombre tiene numeros?")
print(nombre.isdigit())
print(nombre)
print("Tu nombre tiene letras?")
print(nombre.isalpha())
print("Se modificara una letra en tu nombre")
print(nombre.replace("e","a"))
print(nombre *3)

imprimir("<Programando>.........")
imprimir("<concluido>")
imprimir("Verificado, Gracias")
def imprimir(texto):
    for x in range(1):
        print(texto)

print("Bienvenido")

x = 1 #int
y = 2.0 #float
z = 3 #str

x = float(x)
y = int(y)
z = float(z)

print(x)
print(int(y))
print(z*3)

print("X es "+str(x))
print("Y es "+str(y))
print("Z es "+str(z))

nombre = input("Cual es tu nombre?: ")
#edad = 16
edad = int(input("Cual es tu edad?: "))
edad = edad + 1
height = float(input("Cuanto mides?: "))
print("Hola "+nombre)
print("Tienes"+str(edad)+" veces 365 dias")
print("Mides "+str(height)+"cm ")

pi: 3.1416
a= 1
b= 2
c= 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(420))
print(max(a,b,c))
print(min(a,b,c))

first_name = nombre[:3]
last_name = nombre[:4]
idk_name = nombre[0:6:2]
nombre_alreves = nombre[::-1]
print(first_name)
print(last_name)
print(idk_name)
print(nombre_alreves)

sitio_web = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
corte = slice(13,-8)
print(sitio_web[corte])

mascotas = int(input("Cuantas mascotas tienes?: "))
if mascotas >= 4:
        print("Tienes muchas mascotas!")
else:
    print("Tienes muy pocas mascotas!")

if mascotas <= 1:
    print("No tienes mascota!")

temperatura =int(input("A que temperatura estamos?: "))

if not(temperatura >=0 and temperatura <=30):
    print("La temperatura esta muy mal :(")
    print("Quedate en casa ")
elif not(temperatura < 0 or temperatura >30):
    print("La temperatura esta muy bien :D")
    print("Disfruta el dia :p")

Comida_favorita = ""

while len(Comida_favorita) == 0:
    Comida_favorita = input("Cual es tu comida favorita?")
    
print("Tu comida favorita es: "+Comida_favorita)


