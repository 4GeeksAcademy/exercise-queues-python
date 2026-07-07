## 01 - Fundamentos de Cola

## Que vas a aprender

En este ejercicio vas a construir tu primera cola en Python.
Una cola sigue la regla FIFO: el primero en entrar es el primero en salir.

Piensa en una fila de personas:

- La persona nueva se agrega al final.
- La persona que sale es la que esta al frente.

## Que debes implementar

Crea una clase `Queue` con una lista interna (`self.items`) y estos metodos:

- `enqueue(value)`: agrega un valor al final de la cola.
- `dequeue()`: remueve y retorna el valor del frente.

## Guia paso a paso

1. En `__init__`, crea `self.items = []`.
2. En `enqueue`, usa `append` para insertar al final.
3. En `dequeue`, usa `pop(0)` para sacar el primer elemento.
4. Crea una instancia llamada `queue`.
5. Encola `10` y `20`.
6. Guarda el resultado del primer `dequeue()` en `first_out`.

## Ejemplo rapido

Si haces:

1. `enqueue(10)`
2. `enqueue(20)`
3. `dequeue()`

Entonces:

- El valor retornado debe ser `10`.
- La cola debe quedar con `[20]`.

## Nota: imports

En este ejercicio no necesitas hacer imports para resolver la logica de la cola.
Con una clase `Queue` y una lista interna (`self.items`) es suficiente para completar el reto.

## Variables requeridas

- `queue`: instancia de `Queue`.
- Debes encolar `10` y `20`.
- `first_out`: resultado del primer `dequeue()`.
