## 02 - Peek, Size e Is Empty

## Que vas a aprender

En este ejercicio vas a agregar metodos de consulta a una cola.
Estos metodos te permiten ver informacion sin cambiar el estado de la estructura.

## Que debes implementar

Extiende la clase `Queue` con:

- `peek()`: devuelve el elemento del frente sin removerlo.
- `size()`: devuelve la cantidad de elementos actuales.
- `is_empty()`: devuelve `True` si la cola esta vacia y `False` en caso contrario.

## Guia paso a paso

1. Mantén `self.items` como lista interna.
2. En `peek()`, retorna `self.items[0]` si hay elementos.
3. Si no hay elementos en `peek()`, retorna `None`.
4. En `size()`, retorna `len(self.items)`.
5. En `is_empty()`, compara el tamaño con cero.
6. Crea `queue`, encola "A", "B", "C" y guarda:
	- `front_item = queue.peek()`
	- `queue_length = queue.size()`

## Ejemplo rapido

Si la cola tiene `['A', 'B', 'C']`:

- `peek()` debe devolver `A`.
- `size()` debe devolver `3`.
- `is_empty()` debe devolver `False`.

## Nota

`peek()` no debe eliminar elementos. Solo observa el frente.

## Variables requeridas

- `queue`: instancia de `Queue`.
- Encola "A", "B", "C".
- `front_item`: resultado de `peek()`.
- `queue_length`: resultado de `size()`.
