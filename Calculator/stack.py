'''
PA4 by Antonio Guizar Orozco 11-20-2022
Stack implementation used in tree.py and calculator.py
'''
class Stack:
     def __init__(self):
        self.items = []

     def isEmpty(self):
        return self.items == []

     def push(self, item):
        self.items.append(item)

     def pop(self):
        return self.items.pop()

     def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]

     def size(self):
        return len(self.items)

# a driver program for class Stack
if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]
    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())
    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
    print('No assertion errors :)')