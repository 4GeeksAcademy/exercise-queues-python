# Escribe tu solucion aqui.


class QueueWithStacks:
	def __init__(self):
		self.in_stack = []
		self.out_stack = []

	def _shift(self):
		# TODO: mueve datos de in_stack a out_stack cuando out_stack este vacio.
		pass

	def enqueue(self, value):
		# TODO: agrega `value` en in_stack y retorna True.
		pass

	def dequeue(self):
		# TODO: aplica _shift y retorna el frente de la cola.
		# Si no hay elementos, retorna None.
		pass

	def peek(self):
		# TODO: aplica _shift y retorna el frente sin remover.
		pass


# Escenario del test (no modificar nombres).
queue = QueueWithStacks()
results = [
	queue.enqueue(5),
	queue.enqueue(6),
	queue.dequeue(),
	queue.peek(),
	queue.dequeue(),
	queue.dequeue(),
]
