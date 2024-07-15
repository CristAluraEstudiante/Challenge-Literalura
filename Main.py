import requests
import json

def buscar_libro_por_titulo(titulo):
    URL = f"https://gutendex.com/books?search={titulo}"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
        print('Libros encontrados:', formatted_data)
    else:
        print('Error en la solicitud, detalles:', response.text)

def listar_libros_registrados():
    URL = "https://gutendex.com/books"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
        print('Libros registrados:', formatted_data)
    else:
        print('Error en la solicitud, detalles:', response.text)

def listar_autores_registrados():
    URL = "https://gutendex.com/authors"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
        print('Autores registrados:', formatted_data)
    else:
        print('Error en la solicitud, detalles:', response.text)

def listar_autores_vivos_en_anio(anio):
    URL = "https://gutendex.com/authors"
    response = requests.get(URL)
    if response.status_code == 200:
        autores = response.json()['results']
        autores_vivos = [autor for autor in autores if autor['birth_year'] <= anio <= (autor['death_year'] if autor['death_year'] else anio)]
        formatted_data = json.dumps(autores_vivos, indent=4, ensure_ascii=False)
        print(f'Autores vivos en el año {anio}:', formatted_data)
    else:
        print('Error en la solicitud, detalles:', response.text)

def listar_libros_por_idioma(idioma):
    URL = f"https://gutendex.com/books?languages={idioma}"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
        print(f'Libros en idioma {idioma}:', formatted_data)
    else:
        print('Error en la solicitud, detalles:', response.text)

def menu():
    while True:
        print("\nMenú:")
        print("1. Buscar libro por título")
        print("2. Listar libros registrados")
        print("3. Listar autores registrados")
        print("4. Listar autores vivos en un determinado año")
        print("5. Listar libros por idioma")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            titulo = input("Introduce el título del libro: ")
            buscar_libro_por_titulo(titulo)
        elif opcion == "2":
            listar_libros_registrados()
        elif opcion == "3":
            listar_autores_registrados()
        elif opcion == "4":
            anio = int(input("Introduce el año: "))
            listar_autores_vivos_en_anio(anio)
        elif opcion == "5":
            idioma = input("Introduce el idioma (por ejemplo, 'en' para inglés): ")
            listar_libros_por_idioma(idioma)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()
