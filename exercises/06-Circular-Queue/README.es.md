## 06 - Cola Circular

## Que vas a aprender

En este ejercicio vas a usar una cola circular de tamano fijo.
La idea clave es reutilizar posiciones libres cuando el frente avanza.

## Que debes implementar

Implementa una clase `CircularQueue` con capacidad fija y metodos:

- `enqueue(value)`
- `dequeue()`
- `peek()`
- `is_empty()`
- `is_full()`

Reglas:

- Si `enqueue` falla porque esta llena, devuelve `False`.
- Si `dequeue` falla porque esta vacia, devuelve `None`.

## Guia paso a paso

1. Crea un arreglo fijo para los datos.
2. Lleva control de indices de frente y final.
3. Lleva un contador de elementos para saber vacio/lleno facilmente.
4. En `enqueue`, inserta en final y avanza circularmente.
5. En `dequeue`, saca desde frente y avanza circularmente.
6. En `peek`, retorna el frente sin remover.
7. Ejecuta la secuencia pedida y guarda los resultados en `scenario`.

## Ejemplo rapido

Con `CircularQueue(3)` y esta secuencia:

1. enqueue(1)
2. enqueue(2)
3. enqueue(3)
4. enqueue(4)
5. dequeue()
6. enqueue(4)
7. peek()

El cuarto enqueue debe fallar al inicio, luego se libera espacio con `dequeue()` y el siguiente enqueue debe funcionar.

## Nota

En una cola circular, los indices regresan al inicio cuando llegan al final del arreglo.

## Variables requeridas

- `cq`: `CircularQueue(3)`
- `scenario`: lista de resultados de esta secuencia:
  - enqueue(1), enqueue(2), enqueue(3), enqueue(4), dequeue(), enqueue(4), peek()
