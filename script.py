class Perro:
    """Representa a las caracteristicas de un perro"""

    
    def __init__(self, nombre, edad, tamaño, raza, color):
        """Inicializa una instancia de Perro

        Parametros: 
            nombre (str): Nombre del perro
            edad (int): Edad del perro
            tamaño (str): Tamaño del perro
            raza (str): Raza del perro
            color (str): Color del perro
        """
        self._nombre = nombre
        self._edad = edad
        self._tamaño = tamaño
        self._raza = raza
        self._color = color


    #Getter y Setter de nombre
    @property
    def nombre(self):
        """Obtiene el nombre del perro"""
        return self._nombre


    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Modifica el nombre del perro"""
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self.nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacia")


    #Getter y Setter de edad
    @property
    def edad(self):
        """Obtiene la edad del perro"""
        return self._edad


    @edad.setter
    def edad(self, nueva_edad):
        """Modifica la edad del perro"""
        if isinstance(nueva_edad, int) and nueva_edad > 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un numero entero positivo")


    #Getter y Setter de tamaño
    @property
    def tamaño(self):
        """Obtiene el tamaño del perro"""
        return self._tamaño


    @tamaño.setter
    def tamaño(self, nuevo_tamaño):
        """Modifica el tamaño del perro"""
        if isinstance(nuevo_tamaño, str) and nuevo_tamaño.strip():
            self._tamaño = nuevo_tamaño
        else:
            raise ValueError("El tamaño no debe ser una cadena vacia")


    #Getter y Setter de raza
    @property
    def raza(self):
        """Obtiene la raza del perro"""
        return self._raza


    @raza.setter
    def raza(self, nueva_raza):
        """Modifica la raza de un perro"""
        if isisntance(nueva_raza, str) and nueva_raza.strip():
            self._raza = nueva_raza
        else:
            raise ValueError("La raza no debe ser una cadena vacia")


    #Getter y Setter de color
    @property
    def color(self):
        """Obtiene el color del perro"""
        return self._color


    @color.setter
    def color(self, nuevo_color):
        """Modifica el color de un perro"""
        if isisntance(nuevo_color, str) and nuevo_color.strip():
            self._color = nuevo_color
        else:
            raise ValueError("El color no debe ser una cadena vacia")
    



