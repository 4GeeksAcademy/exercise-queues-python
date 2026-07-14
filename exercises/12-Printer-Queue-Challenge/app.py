# Escribe tu solucion aqui.


class PrintQueue:
	def __init__(self):
		self.jobs = []
		self._counter = 0

	def add_job(self, name, pages, priority):
		# TODO: agrega un job con formato:
		# (priority, orden_de_llegada, name, pages)
		# Despues, ordena por prioridad y luego por orden de llegada.
		pass

	def next_job(self):
		# TODO: retorna el nombre del siguiente job y lo remueve.
		# Si no hay jobs, retorna None.
		pass

	def pending_pages(self):
		# TODO: suma paginas pendientes de todos los jobs.
		pass


# Escenario del test (no modificar nombres).
printer = PrintQueue()
printer.add_job("report", 20, 3)
printer.add_job("invoice", 2, 1)
printer.add_job("slides", 15, 2)
printer.add_job("notes", 4, 1)
processed = [printer.next_job(), printer.next_job(), printer.next_job()]
pages_left = printer.pending_pages()
