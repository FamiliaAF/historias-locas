import random

nombres = [
   "Alex", "Luna", "Max", "Sofía", "Diego", "Emma", "Lucas",
   "Mía", "Santiago", "Valentina", "Rodrigo", "Isabella",
   "Mateo", "Camila"
]

adjetivos = [
   "misterioso", "brillante", "gigante", "diminuto", "mágico",
   "pegajoso", "veloz", "antiguo", "espacial", "invisible",
   "eléctrico", "congelado", "flotante", "explosivo",
   "parlante", "bailarín"
]

verbos = [
   "corría", "saltaba", "volaba", "nadaba", "cantaba",
   "bailaba", "cocinaba", "dibujaba", "exploraba",
   "escalaba", "inventaba", "buscaba"
]

lugares = [
   "bosque encantado", "castillo", "cueva", "playa", "montaña",
   "ciudad", "isla misteriosa", "desierto", "selva",
   "laboratorio", "espacio", "mercado", "escuela",
   "museo", "volcán"
]

objetos = [
   "espada", "libro", "piedra", "llave", "mapa", "linterna",
   "cofre", "telescopio", "brújula", "poción", "robot",
   "cristal", "medallón", "espejo", "portal"
]

def historia_terror():
   nombre = random.choice(nombres)
   adjetivo = random.choice(adjetivos)
   lugar1 = random.choice(lugares)
   lugar2 = random.choice(lugares)
   objeto = random.choice(objetos)
   verbo = random.choice(verbos)

   historia = (
      f"Esa noche, el ambiente era muy {adjetivo} en {lugar1}. "
      f"{nombre} caminaba solo cuando escuchó un ruido extraño "
      f"proveniente de {lugar2}.\n\n"
      f"Con el corazón acelerado, tomó un/una {objeto} y {verbo} "
      f"hacia la oscuridad.\n\n"
      "Desde ese día, nadie volvió a acercarse a ese lugar."
   )

   return historia

def historia_aventura():
   nombre = random.choice(nombres)
   companero = random.choice(nombres)
   adjetivo = random.choice(adjetivos)
   lugar1 = random.choice(lugares)
   lugar2 = random.choice(lugares)
   objeto = random.choice(objetos)
   verbo = random.choice(verbos)

   historia = (
      f"{nombre} siempre había soñado con vivir una aventura {adjetivo}. "
      f"Un día decidió viajar a {lugar1}, donde encontró un/una {objeto} especial.\n\n"
      f"Sin dudarlo, llamó a {companero} para acompañarlo. "
      f"Juntos enfrentaron muchos peligros y {verbo} "
      f"hasta llegar a {lugar2}.\n\n"
      "Al final comprendieron que la verdadera aventura "
      "no estaba en el destino, sino en el camino."
   )

   return historia

def historia_romance():
   nombre1 = random.choice(nombres)
   nombre2 = random.choice(nombres)

   while nombre2 == nombre1:
      nombre2 = random.choice(nombres)

   adjetivo = random.choice(adjetivos)
   lugar = random.choice(lugares)
   objeto = random.choice(objetos)
   verbo = random.choice(verbos)

   historia = (
      f"{nombre1} conoció a {nombre2} en un/una {lugar}. "
      f"Todo era tan {adjetivo} que parecía un sueño.\n\n"
      f"Compartieron un/una {objeto} y hablaron durante horas. "
      f"Con el tiempo, mientras {verbo} juntos, "
      "descubrieron que estaban enamorados.\n\n"
      "Así comenzó una historia que jamás olvidarían."
   )

   return historia

while True:
   print("║   📚 GENERADOR DE HISTORIAS LOCAS 📚   ║")
   print("1) Terror 👻")
   print("2) Aventura 🗺️")
   print("3) Romance 💕")
   print("4) Aleatoria 🎲")
   print("5) Personalizada ✍️")
   print("6) Salir 🚪")

   opcion = input("Elige una opción: ")

   if opcion == "1":
      historia = historia_terror()

   elif opcion == "2":
      historia = historia_aventura()

   elif opcion == "3":
      historia = historia_romance()

   elif opcion == "4":
      funcion = random.choice([historia_terror, historia_aventura, historia_romance])
      historia = funcion()

   elif opcion == "5":
      nombre = input("Nombre: ")
      companero = input("Compañero: ")
      adjetivo = input("Adjetivo: ")
      lugar1 = input("Lugar inicial: ")
      lugar2 = input("Lugar final: ")
      objeto = input("Objeto: ")
      verbo = input("Verbo: ")

      historia = (
         f"{nombre} siempre había soñado con vivir una aventura {adjetivo}. "
         f"Un día decidió viajar a {lugar1}, donde encontró un/una {objeto} especial.\n\n"
         f"Sin dudarlo, llamó a {companero} para acompañarlo. "
         f"Juntos enfrentaron muchos peligros y {verbo} "
         f"hasta llegar a {lugar2}.\n\n"
         "Al final comprendieron que la verdadera aventura "
         "no estaba en el destino, sino en el camino."
      )


   elif opcion == "6":
      print("¡Hasta luego! 👋")
      break

   else:
      print("Opción inválida.")

   # MOSTRAR HISTORIA
   print("\n═══════════════════════════════════════")
   print(historia)
   print("═══════════════════════════════════════")
