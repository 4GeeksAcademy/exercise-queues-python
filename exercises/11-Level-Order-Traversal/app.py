# Escribe tu solucion aqui.


class TreeNode:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def level_order(root):
	# TODO: devuelve una lista con recorrido por niveles (BFS).
	# Si root es None, retorna []
	pass


# Arbol de ejemplo para el test (no modificar nombres).
root = TreeNode(
	1,
	TreeNode(2, TreeNode(4), TreeNode(5)),
	TreeNode(3),
)
traversal_result = level_order(root)
