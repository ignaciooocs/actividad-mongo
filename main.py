from pymongo import MongoClient
from InquirerPy import inquirer 

def connectdb():
    try:
        client = MongoClient('mongodb://localhost:27017')
        db = client['trabajo-mongo-2']
        return db
    except:
        print('Error al conectarse a la base de datos')
        return False

# 2.1 Se muestren todos los documentos de la colección
def get_alumno():
    try:
        db = connectdb()
        alumnos = db['alumnos'].find()
        print_alumnos(alumnos)
    except:
        print('No se encontraron resultados')
        
# 2.2 Se muestren los documentos que cumplen con 1 condición (Dinamicamente)
def get_alumno_by_condition():
    db = connectdb()
    campo = inquirer.select(message="Elige el campo para filtrar:", choices=['name', 'apellido', 'edad', 'email', 'carrera', 'asignaturas']).execute()
    # elije entre las opciones de condicion 
    condicion = inquirer.select(message='Elige la condicion', choices=['== (igual que)', '!= (distinto que)', '> (mayor que)', '< (menor que)', '>= (mayor o igual que)', '<= menor o igual que']).execute()
    valor = inquirer.text(message="Ingresa el valor:",).execute()
    
    condicion = convertir_condicion(condicion)
    
    valor = convert_value(campo, valor)

    try:
        alumnos = db['alumnos'].find({campo: {condicion: valor}})
        print_alumnos(alumnos)
    except:
        print('No se encontraron resultados')

# 2.3 Se muestren documentos que cumplan con dos condiciones (ambas)
# 2.4 Se muestren documentos que cumplan con al menos una de dos condiciones dadas (cualquiera de ellas)
def get_alumno_by_two_conditions(operator):
    db = connectdb()

    campo_1 = inquirer.select(message="Elige el primer campo para filtrar:", choices=['name', 'apellido', 'edad', 'email', 'carrera', 'asignaturas']).execute()
    condicion_1 = inquirer.select(message='Elige la primer condición', choices=['== (igual que)', '!= (distinto que)', '> (mayor que)', '< (menor que)', '>= (mayor o igual que)', '<= menor o igual que']).execute()
    valor_1 = inquirer.text(message="Ingresa el primer valor:",).execute()

    campo_2 = inquirer.select(message="Elige el segundo campo para filtrar:", choices=['name', 'apellido', 'edad', 'email', 'carrera', 'asignaturas']).execute()
    condicion_2 = inquirer.select(message='Elige la segunda condición', choices=['== (igual que)', '!= (distinto que)', '> (mayor que)', '< (menor que)', '>= (mayor o igual que)', '<= menor o igual que']).execute()
    valor_2 = inquirer.text(message="Ingresa el segundo valor:",).execute()

    condicion_1 = convertir_condicion(condicion_1)
    condicion_2 = convertir_condicion(condicion_2)

    try:
        alumnos = db['alumnos'].find({operator: [{campo_1: {condicion_1: convert_value(campo_1, valor_1)}}, {campo_2: {condicion_2: convert_value(campo_2,valor_2)}}]})
        print_alumnos(alumnos)
    except:
        print('No se encontraron resultados')

# 2.5 Que permita establecer un nuevo valor (existiendo o no previamente el campo) en un documento
def updated_value():
    db = connectdb()

    campo_filtro = inquirer.select(message="elige el campo para filtrar el documento:", choices=['name', 'apellido', 'edad', 'email', 'carrera', 'asignaturas']).execute()
    valor_filtrar = inquirer.text(message="Escribe el valor para filtrar:").execute()

    campo = inquirer.text(message="Escribe el campo para actualizar:").execute()
    valor = inquirer.text(message="Escribe el nuevo valor:").execute()

    try:
        db['alumnos'].update_many({ campo_filtro: convert_value(campo_filtro, valor_filtrar) }, {"$set": {campo: convert_value(campo, valor)}})
        print(f'El campo "{campo}" se actualizó a "{valor}"')
    except:
        print('No se a actualizado el valor')

# 2.6 Que permita sumar un valor a un campo de todos los documentos
def sum_value():
    db = connectdb()

    campo = inquirer.select(message="elige el campo para filtrar el documento:", choices=['edad', 'asignaturas']).execute()
    valor = inquirer.text(message="Escribe el valor a sumar:").execute()

    try:
        db['alumnos'].update_many({}, {"$inc": {campo: int(valor)}})
        print(f'Al campo "{campo}" se le sumó "{valor}"')
    except:
        print('No se a sumado el valor')
# 2.7 Que actualice el valor de todos los documentos, solo si es mayor al valor previo que se tenía
def update_value_min():
    db = connectdb()

    campo = inquirer.select(message="elige el campo para actualizar:", choices=['edad', 'asignaturas']).execute()
    valor = inquirer.text(message="Escribe el nuevo valor:").execute()
    try:
        db['alumnos'].update_many({}, {"$max": {campo: convert_value(campo, valor) }})
        print(f'El campo "{campo}" se actualizó con el valor "{valor}"')
    except:
        print('No se a actualizado el valor')

# 2.8 La opción de borrar un documento, si es que cumple con un criterio dado
def delete_alumno():
    db = connectdb()

    campo = inquirer.select(message="elige el campo para filtrar el documento:", choices=['name', 'apellido', 'edad', 'email', 'carrera', 'asignaturas']).execute()
    valor = inquirer.text(message="Escribe el valor para filtrar:").execute()

    try:
        db['alumnos'].delete_one({ campo: convert_value(campo, valor) })
        print(f'El documento "{campo} = {valor}" se elimino de la base de datos')
    except:
        print('No se a eliminado el documento')

def command_selected(command):
    if command == "1. motrar todos los documentos":
        get_alumno()
    elif command == "2. buscar documento por condición":
        get_alumno_by_condition()
    elif command == "3. buscar documento por una u otra condición":
        get_alumno_by_two_conditions('$or')
    elif command == "4. buscar documento por dos condiciones":
        get_alumno_by_two_conditions('$and')
    elif command == "5. establecer un nuevo valor a un campo":
        updated_value()
    elif command == "6. sumar un valor a un campo de todos los documentos":
        sum_value()
    elif command == "7. actualizar un valor solo si es mayor al anterior":
        update_value_min()
    elif command == "8. eliminar un documento si cumple condición":
        delete_alumno()

    back_to_menu = inquirer.confirm(message="¿Regresar al menú principal?", default=True).execute()

    if not back_to_menu:
        exit()


def convertir_condicion(condicion):
    if condicion == '== (igual que)':
        return '$eq'
    elif condicion == '!= (distinto que)':
        return '$ne'
    elif condicion == '> (mayor que)':
        return '$gt'
    elif condicion == '< (menor que)':
        return '$lt'
    elif condicion == '>= (mayor o igual que)':
        return '$gte'
    elif condicion == '<= menor o igual que':
        return '$lte'
    
def print_alumnos(alumnos):
    print('\n---- Lista de usuarios ----\n')
    for alumno in alumnos:
        print('---------------------------')
        for k in alumno.keys():
            print(f'{k}: {alumno[k]}')
        print('\n')

def convert_value(campo, value):
    if campo == 'edad' or campo == 'asignaturas':
        return int(value)

    return value


options = [
    "1. motrar todos los documentos", 
    "2. buscar documento por condición", 
    "3. buscar documento por una u otra condición", 
    "4. buscar documento por dos condiciones", 
    "5. establecer un nuevo valor a un campo",
    "6. sumar un valor a un campo de todos los documentos",
    "7. actualizar un valor solo si es mayor al anterior",
    "8. eliminar un documento si cumple condición",
    "9. exit"
]

def main():
    while True:
        answer = inquirer.select(message="Selecciona una opción:", choices=options,).execute()

        if answer == '9. exit':
            break 
        
        if answer in options:
            command_selected(answer)

if __name__ == '__main__':
    main()

