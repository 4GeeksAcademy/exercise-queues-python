## 07 - Cola con Dos Pilas

## Que vas a aprender

En este ejercicio vas a implementar una cola usando dos pilas.
Aprenderas a combinar estructuras para obtener comportamiento FIFO.

## Que debes implementar

Implementa una clase `QueueWithStacks` usando:

- `in_stack` para `enqueue`.
- `out_stack` para `dequeue` y `peek`.

Metodos requeridos:

- `enqueue(value)`
- `dequeue()`
- `peek()`

Si esta vacia, `dequeue()` y `peek()` deben devolver `None`.

## Guia paso a paso

1. En `enqueue`, haz `append` en `in_stack`.
2. Cuando necesites sacar o ver frente y `out_stack` este vacia, mueve elementos desde `in_stack` a `out_stack` uno por uno.
3. En `dequeue`, devuelve `out_stack.pop()`.
4. En `peek`, devuelve `out_stack[-1]`.
5. Si ambas pilas estan vacias, retorna `None`.
6. Ejecuta la secuencia pedida y guarda resultados en `results`.

## Ejemplo rapido

Secuencia:

1. enqueue(5)
2. enqueue(6)
3. dequeue()
4. peek()
5. dequeue()
6. dequeue()

Debes observar orden FIFO y al final `None` cuando ya no quedan elementos.

## Nota

Mover datos de `in_stack` a `out_stack` invierte el orden y permite simular la salida por el frente.

## Variables requeridas

- `queue`: instancia de `QueueWithStacks`
- `results`: resultados de:
  - enqueue(5), enqueue(6), dequeue(), peek(), dequeue(), dequeue()
