## 03 - Dequeue Seguro

## Qué vas a aprender

En este ejercicio vas a hacer que tu cola sea más robusta.
La idea es manejar casos vacíos sin errores.

## Qué debes implementar

Modifica `dequeue()` para que:

- Quite y retorne el frente cuando hay elementos.
- Retorne `None` cuando la cola esté vacía.

## Guía paso a paso

1. En `dequeue()`, primero revisa si la cola está vacía.
2. Si está vacía, retorna `None`.
3. Si tiene elementos, usa `pop(0)` para remover y retornar el frente.
4. Crea una cola vacía en `empty_queue`.
5. Guarda en `result_on_empty` el resultado de `empty_queue.dequeue()`.

## Ejemplo rápido

- Cola vacía: `dequeue()` devuelve `None`.
- Cola con `[7, 8]`: `dequeue()` devuelve `7` y la cola queda `[8]`.

## Nota

Manejar casos vacíos evita que el programa se rompa en producción.

## Variables requeridas

- `empty_queue`: cola vacía.
- `result_on_empty`: resultado de `dequeue()` en una cola vacía.
