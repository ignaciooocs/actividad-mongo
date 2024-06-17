from main import connectdb

alumnos = [
    { 'nombre': 'Pedro', 'apellido': 'Gonzalez', 'edad': 19, 'email': 'pedro@gmail.com', 'carrera': 'Ingenieria Industrial', 'asignaturas': 4},
    { 'nombre': 'Juan', 'apellido': 'Perez', 'edad': 20, 'email': 'juan@gmail.com', 'carrera': 'Licenciatura en Matematicas', 'asignaturas': 5},
    { 'nombre': 'Maria', 'apellido': 'Lopez', 'edad': 21, 'email': 'maria@gmail.com', 'carrera': 'Tecnico en Mantenimiento', 'asignaturas': 5},
    { 'nombre': 'Luis', 'apellido': 'Hernandez', 'edad': 22, 'email': 'luis@gmail.com', 'carrera': 'Ingenieria Civil', 'asignaturas': 4},
    { 'nombre': 'Ana', 'apellido': 'Ramirez', 'edad': 23, 'email': 'ana@gmail.com', 'carrera': 'Licenciatura en Fisica', 'asignaturas': 5},
    { 'nombre': 'Carlos', 'apellido': 'Sanchez', 'edad': 24, 'email': 'carlos@gmail.com', 'carrera': 'Licenciatura en Biologia', 'asignaturas': 5},
    { 'nombre': 'Laura', 'apellido': 'Torres', 'edad': 25, 'email': 'laura@gmail.com', 'carrera': 'Licenciatura en Matematicas', 'asignaturas': 6},
    { 'nombre': 'Jorge', 'apellido': 'Vargas', 'edad': 26, 'email': 'jorge@gmail.com', 'carrera': 'Ingenieria en Sistemas', 'asignaturas': 6},
    { 'nombre': 'Sofia', 'apellido': 'Gutierrez', 'edad': 27, 'email': 'sofia@gmail.com', 'carrera': 'Ingenieria en Electricidad', 'asignaturas': 5},
    { 'nombre': 'Roberto', 'apellido': 'Ramirez', 'edad': 28, 'email': 'roberto@gmail.com', 'carrera': 'Tecnico en Mantenimiento', 'asignaturas': 4},
    { 'nombre': 'Lucia', 'apellido': 'Hernandez', 'edad': 29, 'email': 'lucia@gmail.com', 'carrera': 'Analista Programador', 'asignaturas': 6},
    { 'nombre': 'Pedro', 'apellido': 'Torres', 'edad': 30, 'email': 'pedro@gmail.com', 'carrera': 'Diseño Grafico', 'asignaturas': 7},
    { 'nombre': 'Maria', 'apellido': 'Sanchez', 'edad': 31, 'email': 'maria@gmail.com', 'carrera': 'Gastronomia', 'asignaturas': 5},
    { 'nombre': 'Luis', 'apellido': 'Ramirez', 'edad': 32, 'email': 'luis@gmail.com', 'carrera': 'Licenciatura en Matematicas', 'asignaturas': 6},
    { 'nombre': 'Ana', 'apellido': 'Gonzalez', 'edad': 33, 'email': 'ana@gmail.com', 'carrera': 'Ingenieria Civil', 'asignaturas': 5},
    { 'nombre': 'Carlos', 'apellido': 'Perez', 'edad': 34, 'email': 'carlos@gmail.com', 'carrera': 'Ingenieria Industrial', 'asignaturas': 5},
    { 'nombre': 'Laura', 'apellido': 'Hernandez', 'edad': 35, 'email': 'laura@gmail.com', 'carrera': 'Ingenieria en Sistemas', 'asignaturas': 8},
    { 'nombre': 'Jorge', 'apellido': 'Vargas', 'edad': 36, 'email': 'jorge@gmail.com', 'carrera': 'Ingenieria en Informatica', 'asignaturas': 6},
    { 'nombre': 'Sofia', 'apellido': 'Torres', 'edad': 37, 'email': 'sofia@gmail.com', 'carrera': 'Tecnico en Electricidad', 'asignaturas': 5}
]


def crear_coleccion():
    try:
        db = connectdb()

        db['alumnos'].drop()
        db['alumnos'].insert_many(alumnos)
        print('Coleccion creada')
    except:
        print('No se pudo crear la coleccion')


crear_coleccion()