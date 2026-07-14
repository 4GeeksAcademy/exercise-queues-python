# Escribe tu solucion aqui.


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        # TODO: agrega `value` al final.
        pass

    def rear(self):
        # TODO: retorna el ultimo elemento sin removerlo. Si esta vacia, None.
        pass

    def clear(self):
        # TODO: elimina todos los elementos de la cola.
        pass

    def size(self):
        # TODO: retorna la cantidad de elementos.
        pass


# TODO: usa la cola y completa el escenario esperado por el test.
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
last_item = queue.rear()
queue.clear()
size_after_clear = queue.size()
