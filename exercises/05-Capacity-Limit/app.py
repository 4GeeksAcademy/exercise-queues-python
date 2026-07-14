# Escribe tu solucion aqui.


class Queue:
	def __init__(self, capacity):
		self.capacity = capacity
		self.items = []

	def enqueue(self, value):
		# TODO: si la cola esta llena retorna False.
		# TODO: si hay espacio, agrega `value` y retorna True.
		pass

	def is_full(self):
		# TODO: retorna True si alcanzo la capacidad.
		pass


# TODO: completa los metodos para que este escenario pase.
queue = Queue(2)
enqueue_results = [queue.enqueue(10), queue.enqueue(20), queue.enqueue(30)]
