## 09 - Cola de Tareas

## Que vas a aprender

En este ejercicio vas a modelar tareas reales con una cola.
Vas a combinar objetos y estructura FIFO en un flujo simple.

## Que debes implementar

Crea:

- Clase `Task(name, duration)` para representar cada tarea.
- Clase `TaskQueue` con:
	- `add_task(task)`
	- `next_task()`
	- `total_time()`

Reglas:

- `next_task()` devuelve la siguiente tarea de la cola.
- Si no hay tareas, `next_task()` devuelve `None`.
- `total_time()` suma duraciones pendientes.

## Guia paso a paso

1. Define la clase `Task` con nombre y duracion.
2. En `TaskQueue`, guarda tareas en una lista interna.
3. En `add_task`, agrega al final.
4. En `next_task`, saca del frente.
5. En `total_time`, suma `duration` de todas las tareas pendientes.
6. Crea `tasks` y agrega varias tareas.
7. Guarda en `first_task_name` el nombre de la primera tarea ejecutada.
8. Guarda en `remaining_time` el tiempo total restante.

## Ejemplo rapido

Si agregas tareas de 5, 3 y 2 minutos:

- La primera en salir debe ser la primera agregada.
- Si ejecutas una tarea, el tiempo restante baja en su duracion.

## Nota

En este reto, el orden importa tanto como los datos de cada tarea.

## Variables requeridas

- `tasks`: instancia de `TaskQueue`
- `first_task_name`: nombre de la primera tarea ejecutada
- `remaining_time`: tiempo total restante
