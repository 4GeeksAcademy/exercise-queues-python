## 04 - Rear y Clear

## Que vas a aprender

En este ejercicio vas a consultar el ultimo elemento y reiniciar la cola.
Son operaciones comunes cuando quieres revisar estado y empezar de nuevo.

## Que debes implementar

Agrega a `Queue`:

- `rear()`: devuelve el ultimo elemento sin removerlo.
- `clear()`: vacia toda la cola.

Si `rear()` se llama sobre una cola vacia, devuelve `None`.

## Guia paso a paso

1. En `rear()`, revisa si hay elementos.
2. Si hay elementos, retorna `self.items[-1]`.
3. Si no hay elementos, retorna `None`.
4. En `clear()`, deja la cola vacia.
5. Crea `queue` con 1, 2 y 3.
6. Guarda `last_item` antes de limpiar.
7. Ejecuta `clear()` y luego guarda `size_after_clear`.

## Ejemplo rapido

Con cola `[1, 2, 3]`:

- `rear()` devuelve `3`.
- Despues de `clear()`, la cola queda `[]`.
- El tamaño final es `0`.

## Nota

`clear()` debe dejar la cola lista para reutilizarse sin crear otra instancia.

## Variables requeridas

- `queue`: cola con los elementos 1, 2 y 3.
- `last_item`: resultado de `rear()` antes de limpiar.
- `size_after_clear`: tamaño despues de llamar `clear()`.
