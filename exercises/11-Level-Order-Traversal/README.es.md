## 11 - Recorrido por Niveles

## Que vas a aprender

En este ejercicio usaras una cola para recorrer un arbol binario por niveles.
Este recorrido tambien se conoce como BFS.

## Que debes implementar

Implementa:

- Clase `TreeNode(value, left=None, right=None)`.
- Funcion `level_order(root)` que devuelve una lista con el recorrido BFS.

Si el arbol esta vacio, devuelve una lista vacia.

## Guia paso a paso

1. Si `root` es `None`, retorna `[]`.
2. Crea una cola e inserta `root`.
3. Crea una lista para resultados.
4. Mientras la cola tenga nodos:
   - saca el nodo del frente.
   - agrega su valor a resultados.
   - encola su hijo izquierdo si existe.
   - encola su hijo derecho si existe.
5. Retorna la lista final.
6. Construye el arbol requerido y guarda resultado en `traversal_result`.

## Ejemplo rapido

Para este arbol:

- raiz 1
- hijos de 1: 2 y 3
- hijos de 2: 4 y 5

El recorrido por niveles esperado es: `[1, 2, 3, 4, 5]`.

## Nota

La cola garantiza que primero proceses todos los nodos de un nivel antes de pasar al siguiente.

## Variables requeridas

- `root`: arbol con esta estructura:
  - 1
  - hijos: 2 y 3
  - hijos de 2: 4 y 5
- `traversal_result`: resultado de `level_order(root)`
