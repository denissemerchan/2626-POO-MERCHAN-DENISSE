# Explicación del programa de programación orientada a objetos

Este documento explica en detalle el programa `TAREA SEMANA 2.py`, que utiliza una clase para representar un objeto del mundo real: una mascota.

## 1. ¿Qué es una clase?

Una clase es una plantilla o molde que define cómo se debe crear un objeto. En programación orientada a objetos, un objeto representa algo del mundo real con propiedades (atributos) y acciones (métodos).

En este programa, la clase se llama `Mascota` y representa una mascota.

```python
class Mascota:
```

Esto declara la clase `Mascota`.

## 2. El método `__init__`

El método `__init__` se ejecuta automáticamente cuando creamos una mascota nueva. Se usa para inicializar los atributos del objeto.

```python
    def __init__(self, nombre, especie, edad, duenio):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.duenio = duenio
```

- `self` es una referencia al objeto que se está creando.
- `nombre`, `especie`, `edad` y `duenio` son los datos que recibe la mascota.
- `self.nombre = nombre` asigna el valor recibido a un atributo del objeto.

### Atributos de la clase `Mascota`

- `nombre`: el nombre de la mascota.
- `especie`: el tipo de animal, por ejemplo, gato o perro.
- `edad`: cuántos años tiene.
- `duenio`: el nombre de la persona que cuida a la mascota.

## 3. Método `descripcion`

Este método devuelve una descripción de la mascota.

```python
    def descripcion(self):
        return f"{self.nombre} es un(a) {self.especie} de {self.edad} año(s) y su dueño(a) es {self.duenio}."
```

- `self` permite acceder a los atributos del objeto.
- La línea `return f"..."` crea una frase usando los datos de la mascota.

## 4. Método `cumplir_anios`

Este método simula que la mascota cumple un año más.

```python
    def cumplir_anios(self):
        self.edad += 1
        return f"¡Feliz cumpleaños, {self.nombre}! Ahora tiene {self.edad} año(s)."
```

- `self.edad += 1` aumenta la edad de la mascota en 1.
- Luego devuelve un mensaje indicando la nueva edad.

## 5. Bloque principal del programa

La parte siguiente se ejecuta cuando se corre el archivo directamente.

```python
if __name__ == '__main__':
```

Esto significa que el código dentro de este bloque solo se ejecuta si el archivo se abre directamente, no si se importa en otro módulo.

### Crear objetos `Mascota`

```python
    mascota1 = Mascota(nombre='Luna', especie='gato', edad=3, duenio='Denisse')
    mascota2 = Mascota(nombre='Max', especie='perro', edad=5, duenio='Alicia')
```

Estas líneas crean dos objetos diferentes con datos reales.

### Usar los métodos

```python
    print(mascota1.descripcion())
    print(mascota2.descripcion())
    print(mascota1.cumplir_anios())
    print(mascota2.cumplir_anios())
```

- `mascota1.descripcion()` muestra los datos de `mascota1`.
- `mascota2.descripcion()` muestra los datos de `mascota2`.
- `mascota1.cumplir_anios()` aumenta la edad de `mascota1` y muestra un mensaje.
- `mascota2.cumplir_anios()` hace lo mismo para `mascota2`.

## 6. Resumen de conceptos básicos

- Clase: plantilla para crear objetos. En este caso, `Mascota`.
- Objeto: instancia de una clase. Ejemplos: `mascota1`, `mascota2`.
- Atributo: dato que pertenece al objeto, como `nombre` o `edad`.
- Método: función dentro de la clase que define un comportamiento, como `descripcion()` o `cumplir_anios()`.
- `self`: referencia al objeto actual dentro de los métodos.
- `__init__`: se ejecuta al crear el objeto para definir sus valores iniciales.

## 7. ¿Por qué es útil esto?

Usar clases y objetos ayuda a organizar mejor el código cuando se trabaja con datos que tienen muchas propiedades y comportamientos. En lugar de manejar datos sueltos, se agrupan dentro de un objeto que sabe qué es y qué puede hacer.

¡Listo! Con esta explicación puedes entender cada parte del programa paso a paso.
