#핸젤과 그레텔 길찾기
import random

def push(data):
  global SIZE, stack,top
  if (isStackFull()):
    return 
  top +=1
  stack[top] = data

def isStackFull():
  global SIZE, stack, top
  if top >=SIZE-1 :
    return True
  else :
    return False

def isEmpty():
  global SIZE, stack, top
  if top==-1:
    return True
  else :
    return False

def pop():
  global SIZE, stack, top
  if (isEmpty()):
    return None
  data = stack[top]
  stack[top]=None
  top-=1
  return data

SIZE = 10
top = -1
stack = [None for _ in range(SIZE)]


if __name__ == "__main__":

  stone = ["a","b","c","d","e","f"]
  random.shuffle(stone)

  print("과자집 가는 길: ", end=" ")
  for i in stone:
    push(i)
    print(i,'-->',end=" ")
  print("과자집")

  print("우리집에 오는 길:", end=" ")
  while True:
    i = pop()
    if i==None:
      break
    print(i,"-->",end=' ')
  print("우리집")