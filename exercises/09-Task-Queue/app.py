# Escribe tu solucion aqui.

from dataclasses import dataclass


@dataclass
class Task:
	name: str
	duration: int


class TaskQueue:
	def __init__(self):
		self.items = []

	def add_task(self, task):
		# TODO: agrega la tarea al final de la cola.
		pass

	def next_task(self):
		# TODO: retorna/remueve la siguiente tarea.
		# Si no hay tareas, retorna None.
		pass

	def total_time(self):
		# TODO: retorna la suma de duracion de tareas pendientes.
		pass


# Escenario del test (no modificar nombres).
tasks = TaskQueue()
tasks.add_task(Task("setup", 5))
tasks.add_task(Task("build", 10))
tasks.add_task(Task("deploy", 8))
first_task = tasks.next_task()
first_task_name = first_task.name if first_task else None
remaining_time = tasks.total_time()
