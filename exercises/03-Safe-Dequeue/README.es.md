## 03 - Dequeue Seguro

## Que vas a aprender

En este ejercicio vas a hacer que tu cola sea mas robusta.
La idea es manejar casos vacios sin errores.

## Que debes implementar

Modifica `dequeue()` para que:

- Quite y retorne el frente cuando hay elementos.
- Retorne `None` cuando la cola este vacia.

## Guia paso a paso

1. En `dequeue()`, primero revisa si la cola esta vacia.
2. Si esta vacia, retorna `None`.
3. Si tiene elementos, usa `pop(0)` para remover y retornar el frente.
4. Crea una cola vacia en `empty_queue`.
5. Guarda en `result_on_empty` el resultado de `empty_queue.dequeue()`.

## Ejemplo rapido

- Cola vacia: `dequeue()` devuelve `None`.
- Cola con `[7, 8]`: `dequeue()` devuelve `7` y la cola queda `[8]`.

## Nota

Manejar casos vacios evita que el programa se rompa en produccion.

## Variables requeridas

- `empty_queue`: cola vacia.
- `result_on_empty`: resultado de `dequeue()` en una cola vacia.
