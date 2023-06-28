"""
-- ПРИНЦИП РАБОТЫ --
    Удаление элемента из бинарного дерева поиска - задача, где нужно аккуратно
    учесть несколько возможных сценариев.

    1. Ищем удаляемый элемент, сохраняя ссылку на его родителя.
    2. Искомый элемент существует в дереве. Возможные варианты:

    - Искомый элемент является корнем дерева, и имеет менее 2 потомков.
        В этом случае корнем модифицированного дерева будет являться непустой ребенок
        или None в случае, когда корень не имеет детей.
    - Искомый элемент является листом.
        Просто перезаписываем ссылку на ребенка у родителя, записывая туда None.
    - Искомый элемент имеет одного потомка.
        Записываем в соответствующую ссылку родителя ссылку на существующего потомка.
    - Искомый элемент имеет два потомка. Основной, наиболее трудоемкий сценарий.
        1. Находим ближайший к искомому по значению следующий элемент в дереве.
        Поиск осуществляем в правом поддереве в нашей программе. При этом важно
        не нарушить ссылки и не "потерять" правое поддерево элемента который 
        мы ищем (функция get_closest)
        2. Вставляем найденный элемент вместо удаляемого, сохраняя ссылки на
        правое и левое поддерево. Если удаляемый элемент являлся корневым,
        возвращаем ссылку на элемент из шага 1 - это и есть обновленный корень
        модифицированного дерева. В противном случае, по аналогии с предыдущими
        кейсами, обновляем соответствующую ссылку родителя.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    Сложность программы для n удаляемых элементов - O(h * n).
    h - высота дерева, она зависит от того, насколько бинарное дерево 
    поиска сбалансированно.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(1).
"""
# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing


from typing import Optional


LOCAL = False
if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value

else:
    from node import Node


def remove_node_with_two_childen(root, parent_node, target_node) -> Node:
    # no need to search closest when target_node.right doesn't have left child
    if not target_node.right.left:
        closest_node = target_node.right
    else:
        closest_node = get_closest(target_node.right)
        closest_node.right = target_node.right
    closest_node.left = target_node.left

    # target_node is a root element
    if not parent_node:
        return closest_node

    if parent_node.left == target_node:
        parent_node.left = closest_node
    else:
        parent_node.right = closest_node
    return root


# find the right-most closest by value element to the one being removed
def get_closest(node) -> Node:
    parent_node = None
    while node.left:
        parent_node, node = node, node.left

    # in case our element has right subtre - we need to link it its parent
    parent_node.left = node.right
    return node


def remove(root, key) -> Optional[Node]:
    parent_node = None
    target_node = root

    # find the element to be removed
    while target_node and target_node.value != key:
        parent_node = target_node
        if key > target_node.value:
            target_node = target_node.right
        else:
            target_node = target_node.left

    if not target_node:
        return root

    # target_node is a root element and has one child or no children at all
    if not parent_node and not (target_node.left and target_node.right):
        return target_node.left or target_node.right

    # target_node has two children
    if target_node.left and target_node.right:
        return remove_node_with_two_childen(root, parent_node, target_node)

    # target_node is a leaf
    elif not target_node.left and not target_node.right:
        if parent_node.left == target_node:
            parent_node.left = None
        else:
            parent_node.right = None

    # target_node has only left child
    elif target_node.left:
        if parent_node.left == target_node:
            parent_node.left = target_node.left
        else:
            parent_node.right = target_node.left

    # target_node has only right child
    else:
        if parent_node.left == target_node:
            parent_node.left = target_node.right
        else:
            parent_node.right = target_node.right

    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


if __name__ == "__main__":
    test()
