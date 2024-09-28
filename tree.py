from typing import Optional, List
from collections import deque

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val: str):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

    def __repr__(self):
        return f"TreeNode({self.val})"

# 根据前序和中序遍历重建二叉树
def build_tree_pre_in(preorder: List[str], inorder: List[str]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)
    root.left = build_tree_pre_in(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree_pre_in(preorder[mid+1:], inorder[mid+1:])
    return root

# 根据后序和中序遍历重建二叉树
def build_tree_post_in(postorder: List[str], inorder: List[str]) -> Optional[TreeNode]:
    if not postorder or not inorder:
        return None
    root_val = postorder[-1]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)
    root.left = build_tree_post_in(postorder[:mid], inorder[:mid])
    root.right = build_tree_post_in(postorder[mid:-1], inorder[mid+1:])
    return root

# 根据前序和后序遍历重建二叉树（仅适用于满二叉树）
def build_tree_pre_post(preorder: List[str], postorder: List[str]) -> Optional[TreeNode]:
    if not preorder or not postorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    if len(preorder) == 1:
        return root
    # 下一个根节点
    next_val = preorder[1]
    index = postorder.index(next_val)
    root.left = build_tree_pre_post(preorder[1:index+2], postorder[:index+1])
    root.right = build_tree_pre_post(preorder[index+2:], postorder[index+1:-1])
    return root

# 根据输入的两种遍历方式重建二叉树
def build_tree(traversal1: str, type1: str, traversal2: str, type2: str) -> Optional[TreeNode]:
    traversal1 = list(traversal1)
    traversal2 = list(traversal2)
    if ('pre' in type1 and 'in' in type2) or ('in' in type1 and 'pre' in type2):
        preorder = traversal1 if 'pre' in type1 else traversal2
        inorder = traversal2 if 'in' in type2 else traversal1
        return build_tree_pre_in(preorder, inorder)
    elif ('post' in type1 and 'in' in type2) or ('in' in type1 and 'post' in type2):
        postorder = traversal1 if 'post' in type1 else traversal2
        inorder = traversal2 if 'in' in type2 else traversal1
        return build_tree_post_in(postorder, inorder)
    elif ('pre' in type1 and 'post' in type2) or ('post' in type1 and 'pre' in type2):
        preorder = traversal1 if 'pre' in type1 else traversal2
        postorder = traversal2 if 'post' in type2 else traversal1
        return build_tree_pre_post(preorder, postorder)
    else:
        print("不支持的遍历类型组合。请选择两种不同的遍历类型（前序、中序、后序）。")
        return None

# 以字符画形式打印二叉树
def print_tree(root: Optional[TreeNode]):
    def display(node: Optional[TreeNode], prefix: str, is_left: bool):
        if node is not None:
            print(prefix, end='')
            print("├── " if is_left else "└── ", end='')
            print(node.val)
            # 准备下一级的前缀
            if is_left:
                new_prefix = prefix + "│   "
            else:
                new_prefix = prefix + "    "
            # 递归打印左子树和右子树
            if node.left or node.right:
                if node.left:
                    display(node.left, new_prefix, True)
                else:
                    print(new_prefix + "├── " + "None")
                if node.right:
                    display(node.right, new_prefix, False)
                else:
                    print(new_prefix + "└── " + "None")
    if root is not None:
        print(root.val)
        if root.left or root.right:
            if root.left:
                display(root.left, "", True)
            else:
                print("├── " + "None")
            if root.right:
                display(root.right, "", False)
            else:
                print("└── " + "None")
    else:
        print("Empty Tree")

# 新增：层序遍历（广度优先遍历）
def level_order_traversal(root: Optional[TreeNode]) -> List[str]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

# 主函数
def main():
    traversal_types = {
        '1': 'pre',
        '2': 'in',
        '3': 'post',
        '4': 'level'
    }

    print("请输入你要输入的两种遍历方式（前序、中序、后序）。")
    print("请选择第一种遍历类型：")
    print("1. 前序遍历（pre）")
    print("2. 中序遍历（in）")
    print("3. 后序遍历（post）")
    type1_input = input("请输入第一种遍历类型（1/2/3）：").strip()
    type1 = traversal_types.get(type1_input)
    if not type1:
        print("无效的遍历类型选择。请重新运行程序并选择1、2或3。")
        return
    traversal1 = input(f"请输入{type1}遍历序列（例如：ABCEHFIJDGK）：").strip().upper()

    print("\n请选择第二种遍历类型（与第一种不同）：")
    print("1. 前序遍历（pre）")
    print("2. 中序遍历（in）")
    print("3. 后序遍历（post）")
    type2_input = input("请输入第二种遍历类型（1/2/3）：").strip()
    type2 = traversal_types.get(type2_input)
    if not type2:
        print("无效的遍历类型选择。请重新运行程序并选择1、2或3。")
        return
    if type2 == type1:
        print("两种遍历类型必须不同。请重新运行程序并选择不同的遍历类型。")
        return
    traversal2 = input(f"请输入{type2}遍历序列（例如：AHECIFJBDKG）：").strip().upper()

    # 重建二叉树
    root = build_tree(traversal1, type1, traversal2, type2)
    if root is None:
        print("无法构建二叉树。")
        return

    # 以字符画形式输出二叉树
    print("\n以字符画形式展示二叉树结构：")
    print_tree(root)

    # 执行层序遍历并显示结果
    print("\n层序遍历结果：")
    level_order = level_order_traversal(root)
    print(" -> ".join(level_order))

if __name__ == "__main__":
    main()
