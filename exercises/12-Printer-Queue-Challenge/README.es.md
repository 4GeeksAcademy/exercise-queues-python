## 12 - Reto de Cola de Impresion

## Que vas a aprender

En este reto final combinaras cola, prioridad y acumulados.
Simularas una cola de impresion mas cercana a un caso real.

## Que debes implementar

Crea la clase `PrintQueue` con:

- `add_job(name, pages, priority)`
- `next_job()` procesa y devuelve el siguiente trabajo (nombre)
- `pending_pages()` devuelve el total de paginas pendientes

Reglas:

- Prioridad menor significa mayor urgencia.
- Si dos trabajos tienen la misma prioridad, conserva orden de insercion.

## Guia paso a paso

1. Representa cada trabajo con nombre, paginas y prioridad.
2. En `add_job`, inserta en la estructura respetando prioridad.
3. En empate de prioridad, agrega despues de los ya existentes con esa prioridad.
4. En `next_job`, procesa y retorna el nombre del siguiente trabajo.
5. Si no hay trabajos, `next_job()` retorna `None`.
6. En `pending_pages`, suma paginas de trabajos pendientes.
7. Crea `printer`, procesa 3 trabajos y guarda resultados en `processed`.
8. Guarda paginas pendientes finales en `pages_left`.

## Ejemplo rapido

Si agregas trabajos con prioridades 3, 1 y 2:

- El de prioridad 1 sale primero.
- Luego prioridad 2.
- Luego prioridad 3.

## Nota

Este reto evalua orden por prioridad y consistencia de datos pendientes al mismo tiempo.

## Variables requeridas

- `printer`: instancia de `PrintQueue`
- `processed`: lista con 3 trabajos procesados
- `pages_left`: paginas pendientes al final
