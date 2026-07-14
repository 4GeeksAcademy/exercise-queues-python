# Escribe tu solucion aqui.


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        # TODO: agrega `value` al final de la cola.
        pass

    def dequeue(self):
        # TODO: si esta vacia retorna None; si no, retorna y remueve el primero.
        pass

    def is_empty(self):
        # TODO: retorna True si no hay elementos.
        pass


# TODO: completa el escenario para validar dequeue seguro.
empty_queue = Queue()
result_on_empty = empty_queue.dequeue()