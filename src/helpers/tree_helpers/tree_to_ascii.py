from __future__ import annotations
from src.core.tree import *

def tree_to_ascii(tree: TreeNode) -> str:
    return "\n".join(tree_to_ascii_recursive(tree))

def tree_to_ascii_recursive(tree: TreeNode) -> list[str]:
    if not tree.children:
        return [f' {tree.name} ']
    
    if len(tree.children) == 1:
        return handle_one_child_ascii(tree)
    
    children_ascii = [tree_to_ascii_recursive(child) for child in tree.children]

    first = children_ascii[0]
    last = children_ascii[-1]
    middle = children_ascii[1:-1]

    resultant_ascii = [handle_first_child_ascii(first)] + \
                      [handle_middle_child_ascii(child) for child in middle] + \
                      [handle_last_child_ascii(last)]
    resultant_ascii = join_trees_with_separator(resultant_ascii)
    
    resultant_middle = len(resultant_ascii) // 2
    resultant_ascii[resultant_middle] = ('─┤ ' if resultant_ascii[resultant_middle][1] == '│' else '─┼─')+ resultant_ascii[resultant_middle][3:]

    return resultant_ascii

def handle_first_child_ascii(child_ascii: list[str]) -> list[str]:
    middle = len(child_ascii) // 2

    for i in range(len(child_ascii)):
        if i < middle:
            child_ascii[i] = '   ' + child_ascii[i]
        elif i == middle:
            child_ascii[i] = ' ┌─' + child_ascii[i]
        else:
            child_ascii[i] = ' │ ' + child_ascii[i]
    
    return child_ascii

def handle_middle_child_ascii(child_ascii: list[str]) -> list[str]:
    middle = len(child_ascii) // 2
    
    for i in range(len(child_ascii)):
        if i != middle:
            child_ascii[i] = ' │ ' + child_ascii[i]
        else:
            child_ascii[i] = ' ├─' + child_ascii[i]
    
    return child_ascii

def handle_last_child_ascii(child_ascii: list[str]) -> list[str]:
    middle = len(child_ascii) // 2

    for i in range(len(child_ascii)):
        if i < middle:
            child_ascii[i] = ' │ ' + child_ascii[i]
        elif i == middle:
            child_ascii[i] = ' └─' + child_ascii[i]
        else:
            child_ascii[i] = '   ' + child_ascii[i]

    return child_ascii

def join_trees_with_separator(children_ascii: list[str]) -> list[str]:
    start = children_ascii[0]
    for i in range(1,len(children_ascii)):
        start += [' │ '] + children_ascii[i]
    
    return start

def handle_one_child_ascii(tree: TreeNode) -> list[str]:
    child_ascii = tree_to_ascii_recursive(tree.children[0])
    middle = len(child_ascii) // 2

    for i in range(len(child_ascii)):
        if i != middle:
            child_ascii[i] = '   ' + child_ascii[i]
        else:
            child_ascii[i] = '───' + child_ascii[i]    

    return child_ascii
