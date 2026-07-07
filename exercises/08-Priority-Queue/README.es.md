## 08 - Cola de Prioridad

## Que vas a aprender

En este ejercicio vas a procesar elementos segun prioridad.
No siempre sale primero el que llego primero: sale primero el mas urgente.

## Que debes implementar

Crea una cola de prioridad simple donde numero menor significa prioridad mas alta.

Metodos requeridos:

- `enqueue(value, priority)`
- `dequeue()`
- `peek()`

Si esta vacia, `dequeue()` y `peek()` devuelven `None`.

## Guia paso a paso

1. Guarda cada elemento con su prioridad.
2. En `enqueue`, inserta el nuevo elemento en la posicion correcta por prioridad.
3. En `dequeue`, saca el elemento con mayor prioridad.
4. En `peek`, observa el siguiente elemento sin remover.
5. Crea `pq` y encola:
   - ("low", 5)
   - ("urgent", 1)
   - ("normal", 3)
6. Haz tres `dequeue()` y guarda los resultados en `order`.

## Ejemplo rapido

Con esas prioridades, el orden esperado de salida es:

1. `urgent`
2. `normal`
3. `low`

## Nota

Prioridad mas alta significa numero mas pequeno.

## Variables requeridas

- `pq`: instancia de `PriorityQueue`
- `order`: resultados de tres llamadas a `dequeue()` despues de encolar:
  - ("low", 5), ("urgent", 1), ("normal", 3)
