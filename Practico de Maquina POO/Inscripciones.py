class Alumno:
    def __init__(self, nombre, fecha, materia, profesor, curso, division, nota):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__materia = materia
        self.__profesor = profesor
        self.__curso = curso
        self.__division = division
        self.__nota = nota

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def materia(self):
        return self.__materia

    @materia.setter
    def materia(self, materia):
        self.__materia = materia

    @property
    def profesor(self):
        return self.__profesor

    @profesor.setter
    def profesor(self, profesor):
        self.__profesor = profesor

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def division(self):
        return self.__division

    @division.setter
    def division(self, division):
        self.__division = division

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota
