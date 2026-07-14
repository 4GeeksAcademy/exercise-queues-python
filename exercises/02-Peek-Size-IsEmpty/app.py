# Escribe tu solucion aqui.


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        # TODO: agrega `value` al final de la cola.
        pass

    def dequeue(self):
        # TODO: remueve y retorna el primer elemento.
        pass

    def peek(self):
        # TODO: retorna el primer elemento sin removerlo.
        pass

    def size(self):
        # TODO: retorna la cantidad de elementos.
        pass

    def is_empty(self):
        # TODO: retorna True si la cola esta vacia, si no False.
        pass


# TODO: completa el escenario para probar tu implementacion.
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
front_item = queue.peek()
queue_length = queue.size()