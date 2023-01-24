def Create_stack():
    stack_init = []
    return stack_init

def StackCheck(stack_len):
    return len(stack_len) == 0

def push(stackpush, value):
    stackpush.append(value)
    return push


def pop(stackpop):
    if StackCheck(stackpop):
        return 'the stack is Empty'
    
    return stackpop.pop()

mystack = []
mystack = Create_stack()
print(pop(mystack))
push(mystack,'1')
print(mystack)
push(mystack,'2')
print(mystack)
push(mystack,'3')
print(mystack)
push(mystack,'4')
print(mystack)

print('pop item is:', pop(mystack))
print(mystack)
print('pop item is:', pop(mystack))
print(mystack)
print('pop item is:', pop(mystack))
print(mystack)
print('pop item is:', pop(mystack))
print(mystack)
print('pop item is:', pop(mystack))
print(mystack)

