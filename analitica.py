class Veterinaria:
    #Atributos
    paredes = 0
    color = ''
    mascotas = 0
    veterinarios = 0
    medicinas = ''
    
    #Constructor
    def __init__(self, color, medicinas, paredes, mascotas, veterinarios):
        self.color = color
        self.medicinas = medicinas
        self.paredes = paredes
        self.mascotas = mascotas
        self.veterinarios = veterinarios

    # Métodos
    def setParedes (self, paredes):
        self.paredes = paredes
    def setColor (self, color):
        self.color = color
    def setMedicinas (self, medicinas):
        self.medicinas = medicinas
    def getParedes (self):
        return self.paredes
    def getColor (self):
        return self.color
    def getMedicinas (self):
        return self.medicinas
    def veterinariosSaludando (saludo):
        print ("Buenos días ", saludo)
    veterinariosSaludando("Carlos")

v1 = Veterinaria ('Rojo', 'vacunas', 10, 20, 5)
print ('Las cantidad de mascotas son: ', v1.mascotas)

v2 = Veterinaria('Azul', 'cremas', 20, 10, 6)
print('La cantidad total de mascotas son ', v2.mascotas + v1.mascotas)

#2da clase
class Usuario(Veterinaria):
    nombreUsuario = ''
    apellidoUsuario = ''
    cedulaUsuario = 0
    telefono = 0
    sexo = ''

    #Constructor
    def __init__(self, medicinas, paredes, color ,mascotas, veterinarios, nombreUsuario, apellidoUsuario, cedulaUsuario, telefono, sexo):

        super().__init__( medicinas, paredes, color, mascotas, veterinarios)
        self.nombreUsuario = nombreUsuario
        self.apellidoUsuario = apellidoUsuario
        self.cedulaUsuario = cedulaUsuario
        self.telefono = telefono
        self.sexo = sexo

    def setMascotas (self, mascotas):
        self.mascotas = mascotas
    def setNombreUsuario (self, nombreUsuario):
        self.nombreUsuario = nombreUsuario
    def setApellidoUsuario (self, apellidoUsuario):
        self.apellidoUsuario = apellidoUsuario
    def getMascotas (self):
        return self.mascotas
    def getNombreUsuario (self):
        return self.nombreUsuario
    def getApellidoUsuario (self):
        return self.apellidoUsuario
    def usuarioSaludo (nombreSaludo, apellidoSaludo):
        print ("Buenas tardes ", nombreSaludo, apellidoSaludo)
    usuarioSaludo('Carlos', 'Gutierrez')
    

u1 = Usuario('Crema', 5, 'azul', 2, 5, 'Carlos', 'Ramirez', 123456789, 456789, 'Masculino')
print ('El usuario ', u1.nombreUsuario, '', u1.apellidoUsuario, ' tiene', u1.mascotas, 'mascotas en la veterinaria')

u3 = Usuario('Adaptil', 5, 'verde', 3, 5, 'Maria', 'Pérez', 4567891, 2587410, 'Femenino')
print (u3.nombreUsuario, u3.apellidoUsuario, 'tiene la cedula numero', u3.cedulaUsuario)
        
#3ra clase

class Animales(Veterinaria):
    # Atributos
    especie = ''
    colorAnimal = ''
    pesoAnimal = 0
    nombreAnimal = ''
    razaAnimal = ''

    #Método constructor
    def __init__(self, color, medicinas, paredes, mascotas, veterinarios, especie, colorAnimal, pesoAnimal, nombreAnimal, razaAnimal):
        super().__init__(color, medicinas, paredes, mascotas, veterinarios)
        self.especie = especie
        self.colorAnimal = colorAnimal
        self. pesoAnimal = pesoAnimal
        self.nombreAnimal = nombreAnimal
        self.razaAnimal = razaAnimal

    #Métodos
    def setMisMascotas (self, mascotas):
        self.mascotas = mascotas
    def setMisVeterinarios (self, veterinarios):
        self.veterinarios = veterinarios
    def setEspecie (self, especie):
        self.especie = especie
    def getMisMascotas (self):
        return self.mascotas
    def getMisVeterinarios (self):
        return self.veterinarios
    def getEspecie (self):
        return self.especie
    def sumatoriaPerros (perro1, perro2):
        sumatoria = int (perro1) + int (perro2)
        print ('El valor total de perros es: ', sumatoria)
    sumatoriaPerros (input ('Introduzca el primer valor de perros que desea sumar: '), input ('Introduzca el segundo valor de perros que desea sumar: '))

a1 = Animales('Azul', 'tetraciclina', 20, 1, 5, 'ave', 'verde', 1, 'Capri', 'psittacoidea')
print ('El loro', a1.razaAnimal, 'necesita el medicamento', a1.medicinas, 'en la veterinaria')

a2 = Animales('Azul', 'carprofeno', 20, 1, 5, 'mamífero', 'dorado', 5, 'Lola', 'pinsher')
print ('El perro', a2.razaAnimal, 'con peso de', a2.pesoAnimal, 'kg necesita de', a2.medicinas, 'para su mejoría')


#4ta clase 

class Veterinario(Veterinaria):

    #Atributos
    nombreVeterinario = ''
    apellidoVeterinario = ''
    edadVeterinario = 0
    idVeterinario = 0
    telefonoVeterinario = 0

    #Método constructor
    def __init__(self, color, medicinas, paredes, mascotas, veterinarios, nombreVeterinario, apellidoVeterinario, edadVeterinario, idVeterinario, telefonoVeterinario):
        super().__init__(color, medicinas, paredes, mascotas, veterinarios)
        self.nombreVeterinario = nombreVeterinario
        self.apellidoVeterinario = apellidoVeterinario
        self.edadVeterinario = edadVeterinario
        self.idVeterinario = idVeterinario
        self.telefonoVeterinario = telefonoVeterinario

    #Métodos
    def setVeterinarios (self, veterinarios):
        self.veterinarios = veterinarios
    def setNomVeterinario (self, nombreVeterinario):
        self.nombreVeterinario = nombreVeterinario
    def setApeVeterinario (self, apellidoVeterinario):
        self.apellidoVeterinario = apellidoVeterinario
    def getVeterinarios (self):
        return self.veterinarios
    def getNomVeterinario (self):
        return self.nombreVeterinario
    def getApeVeterinario (self):
        return self.apellidoVeterinario
    def sumatoriaEdadVeterinarios (vet1, vet2, vet3):
        sumaVets = int (vet1) + int (vet2) + int (vet3)
        print('La suma de las edades de los veterinarios es: ', sumaVets)
    sumatoriaEdadVeterinarios (input ('Introduzca la primera edad: '), input ('Introduzca la segunda edad: '), input ('Introduzca la tercera edad: '))

vt1 = Veterinario('Azul', 'bravecto', 20, 30, 5, 'Juan', 'Gómez', 25, 12378963, 317850917)
print('El veterinario llamado', vt1.nombreVeterinario, vt1.apellidoVeterinario, 'se encuentra en la veterinaria')

vt2 = Veterinario('Azul', 'bravecto', 20, 30, 5, 'Fernanda', 'Cifuentes', 27, 7896054, 312579063)
print('Los veterinarios llamados', vt1.nombreVeterinario, vt1.apellidoVeterinario, 'y', vt2.nombreVeterinario, vt2.apellidoVeterinario, 'están trabajando con', (vt2.mascotas+vt1.mascotas), 'mascotas')

#Clase 5

class Administrativo (Veterinaria):

    #Atributos
    idAdministrativo = 0
    nombreAdministrativo = ''
    apellidoAdministrativo = ''
    cargoAdministrativo = ''
    salarioAdministrativo = ''

    #Método constructor
    def __init__(self, color, medicinas, paredes, mascotas, veterinarios, idAdministrativo, nombreAdministrativo, apellidoAdministrativo, cargoAdministrativo, salarioAdministrativo):
        super().__init__(color, medicinas, paredes, mascotas, veterinarios)
        self.idAdministrativo = idAdministrativo
        self.nombreAdministrativo = nombreAdministrativo
        self.apellidoAdministrativo = apellidoAdministrativo
        self.cargoAdministrativo = cargoAdministrativo
        self.salarioAdministrativo = salarioAdministrativo

    #Métodos
    def setNombreAdmin (self, nombreAdministrativo):
        self.nombreAdministrativo = nombreAdministrativo
    def setApellidoAdmin (self, apellidoAdministrativo):
        self.apellidoAdministrativo = apellidoAdministrativo
    def setCargoAdmin (self, cargoAdministrativo):
        self.cargoAdministrativo = cargoAdministrativo
    def getNombreAdmin (self):
        return self.nombreAdministrativo
    def getApellidoAdmin (self):
        return self.apellidoAdministrativo
    def getCargoAdmin (self):
        return self.cargoAdministrativo
    def multiplicacionSalarial (sal1, sal2, sal3):
        multiplicacion1 = (int (sal1)* int (sal2) * int (sal3))
        print ('La multiplicación salarial es: ', multiplicacion1)
    multiplicacionSalarial (input('Introduzca el primer salario: '), input('Introduzca el segundo salario: '), input('Introduzca el tercer salario: '))


ad1 = Administrativo('Azul', 'ninguna', 20, 30, 10, 12378456, 'Fernando', 'Delgado', 'gerente', 3000000)
print ('El administrativo', ad1.nombreAdministrativo, ad1.apellidoAdministrativo, 'tiene un salario de','$', ad1.salarioAdministrativo, 'de pesos')

ad2 = Administrativo('Azul', 'ninguna', 20, 30, 10, 14769800, 'Mario', 'Rosero', 'subgerente', 2500000)
print ('los administrativos', ad2.nombreAdministrativo, ad2.apellidoAdministrativo, 'y', ad1.nombreAdministrativo, ad1.apellidoAdministrativo, 'ocupan los cargos más altos de la veterinaria' )