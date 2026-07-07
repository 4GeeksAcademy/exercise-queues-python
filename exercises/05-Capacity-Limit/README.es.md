## 05 - Limite de Capacidad

## Que vas a aprender

En este ejercicio vas a controlar el maximo de elementos en una cola.
Esto se usa mucho cuando hay recursos limitados, como memoria o slots.

## Que debes implementar

Crea una cola con capacidad maxima.

- Constructor: `Queue(capacity)`.
- `enqueue(value)`: devuelve `True` si inserta, `False` si esta llena.
- `is_full()`: devuelve si la cola alcanzo su capacidad.

## Guia paso a paso

1. Guarda `capacity` en el constructor.
2. Crea `self.items = []`.
3. En `is_full()`, compara `len(self.items)` con `capacity`.
4. En `enqueue()`, si esta llena retorna `False`.
5. Si no esta llena, agrega el valor y retorna `True`.
6. Crea `queue = Queue(2)`.
7. Intenta encolar 10, 20 y 30 y guarda los resultados en `enqueue_results`.

## Ejemplo rapido

Con capacidad 2:

- Encolar 10 -> `True`
- Encolar 20 -> `True`
- Encolar 30 -> `False`

Resultado esperado: `[True, True, False]`.

## Nota

Aunque falle un `enqueue`, la cola debe conservar sus elementos validos.

## Variables requeridas

- `queue`: `Queue(2)`
- `enqueue_results`: lista con los resultados de encolar 10, 20 y 30.
