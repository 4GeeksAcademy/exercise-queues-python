class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        # Pista: usa arreglo fijo para representar la cola circular.
        self.items = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def is_empty(self):
        # TODO: retorna True si no hay elementos.
        pass

    def is_full(self):
        # TODO: retorna True si se alcanzo la capacidad maxima.
        pass

    def enqueue(self, value):
        # TODO: inserta al final usando aritmetica modular.
        # Debe retornar False si esta llena.
        pass

    def dequeue(self):
        # TODO: remueve el frente usando aritmetica modular.
        # Debe retornar None si esta vacia.
        pass

    def peek(self):
        # TODO: retorna el frente sin remover.
        pass


# Escenario del test (no modificar nombres).
cq = CircularQueue(3)
scenario = [
    cq.enqueue(1),
    cq.enqueue(2),
    cq.enqueue(3),
    cq.enqueue(4),
    cq.dequeue(),
    cq.enqueue(4),
    cq.peek(),
]