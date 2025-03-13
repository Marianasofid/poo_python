# poo_python

- El paradigma de POO está basado en una abstracción del mundo real que nos va a permitir desarrollar programas de forma más cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos.

### Clase

- Una clase es un tipo de datos cuya variable es un tipo de objeto o instancias
- La clase es definición del concepto del mundo real y los objetos o instancias so el "propio" objeto del mundo real.
- Las clases están compuestas por dos elementos: atributos y métodos.

### Atributos 
- Información que almacena la clase. 

### Métodos
- Operaciones que pueden realizar las clases.

## Definición de una clase en Python 

```Python
class NombreClase:
def __init__(self, variable1, variable2):
        self.Atributo1 = valor1
        self.Atributo2 = valor2

def nombreMetodo(self):
        bloqueCodigo
```

### Componentes

```class```: palabra reservada en Python para definir una clase.

```NombreClase```: Nombre de la clase que quierrs crear.

```def```: Plabra reservada en Python que se utiliza para definir el constructor de la clase (método que se ejecuta la primera vez que usas una clase) como los diferentes métodos que tiene.

``` __init__ ```: Palabra reservada en Python para definir el método constructor de la clase. Es lo primero que se ejecuta cuando crear un objetop de una clase.

```(self, variableX)```: Parámetro del constructor de la clase. El parametro self es obligatorio y despues puedes tener tantos parametros como quieras. La forma de añadir parametros es la misma que en las funciones.

```self.AtributoX```: Forma de utilizacion y acceso a los atributos de la clase.

```nombreMetodo```: nombre de metodo de la clase.

```(self)```: Parametros del metodo. El parametro self es obligatorio y despues puedes tener tantos parametros como quieras. La forma de añadir parametros es la misma que en las funciones.

```bloqueCodigo```: Instrucciones que ejecutará el método.

- Cuando defines una clase debes tener en cuenta los siguientes puntos:
  - Puedes definir tantos atributos como necesites.
  - Puedes duefinir tantos métodos como necesites.
  - Puedes definir tantos parámetros en el constructor y en los métodos como necesites.
