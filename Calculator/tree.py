'''
PA4 by Antonio Guizar Orozco 11-20-2022
ExpTree class used in Calculator.py to build a tree data structure
Uses class Stack to construct the tree
'''
from stack import Stack
class BinaryTree:
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        #avoid double wrapping 
        if (type(rootObj) == BinaryTree or type(rootObj) == ExpTree):
            self.key= rootObj.getRootVal()
            self.leftChild= rootObj.getLeftChild()
            self.rightChild= rootObj.getRightChild()


    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key= obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

class ExpTree(BinaryTree):
    #takes postfix expression and uses it to build an ExpTree 
    def make_tree(postfix):
        operators= ['+', '-', '*', '/', '^']
        s= Stack()

        elements= postfix.split(' ')
        for element in elements:
            if element not in operators:
                if '.' in element: #if element has decimal, cast it to a float
                    s.push(ExpTree(float(element)))

                elif not element == ' ': #it is an integer otherwise
                    s.push(ExpTree(int(element)))
            else:
                node= ExpTree(element)
                node.insertRight(s.pop())
                node.insertLeft(s.pop())
                s.push(node)
        return s.pop()
    #preorder traversal  
    def preorder(tree):
        s = ''
        if tree:
            s+=str(tree.getRootVal())
            s+=ExpTree.preorder(tree.getLeftChild())
            s+=ExpTree.preorder(tree.getRightChild())
        return s
    #inorder traversal
    def inorder(tree):
        s = ''
        if tree:
            if tree.getLeftChild() and tree.getRightChild(): #if tree token is an operator
                s+='('
            s+=ExpTree.inorder(tree.getLeftChild())
            s+=str(tree.getRootVal())
            s+=ExpTree.inorder(tree.getRightChild())
            if tree.getLeftChild() and tree.getRightChild(): #if tree token is an operator
                s+=')'
        return s
    #postorder traversal
    def postorder(tree):
        s = ''
        if tree:
            s+=ExpTree.postorder(tree.getLeftChild())
            s+=ExpTree.postorder(tree.getRightChild())
            s+=str(tree.getRootVal())
        return s
    #traverses ExpTree to evaluate the result of the expression
    def evaluate(tree):
        operators= ['+', '-', '*', '/', '^']
        #if tree is empty do nothing
        if tree:
            if not tree.getRootVal() in operators:
                return tree.getRootVal()
            else:
                left_tree= ExpTree.evaluate(tree.getLeftChild())
                right_tree= ExpTree.evaluate(tree.getRightChild())
                if tree.getRootVal() == '+':
                    return left_tree + right_tree
                elif tree.getRootVal() == '-':
                    return left_tree - right_tree
                elif tree.getRootVal() == '/':
                    return left_tree / right_tree
                elif tree.getRootVal() == '*': 
                    return left_tree * right_tree
                elif tree.getRootVal() == '^':
                    return left_tree ** right_tree
    #prints ExptTree in infix notation
    def __str__(self):
        return ExpTree.inorder(self)
   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'
   
    # test an ExpTree
    postfix = '5 2 3 * +'
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0
    postfix = '5 2 + 3 *'
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
    print('No assert errors :)')