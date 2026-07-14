# Escribe tu solucion aqui.


class PriorityQueue:
	def __init__(self):
		self.items = []

	def enqueue(self, value, priority):
		# TODO: guarda una tupla (priority, value).
		# TODO: ordena para que menor prioridad numerica salga primero.
		pass

	def dequeue(self):
		# TODO: retorna el valor con mayor prioridad (numero mas bajo).
		# Si no hay elementos, retorna None.
		pass

	def peek(self):
		# TODO: retorna el proximo valor sin remover.
		pass


# Escenario del test (no modificar nombres).
pq = PriorityQueue()
pq.enqueue("low", 5)
pq.enqueue("urgent", 1)
pq.enqueue("normal", 3)
order = [pq.dequeue(), pq.dequeue(), pq.dequeue()]
