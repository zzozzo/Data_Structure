#회문검사
#책에 없는 예제

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

def push(data):
  global SIZE, stack, top
  for i in data:
    stack.append(i)
    top+=1

stack = []
top = -1
SIZE = len(stack)

if __name__ == "__main__":
  string = input("회문을 입력해주세요: ")
  string = [c for c in string if c.isalpha()]
  string = "".join(string)
  string = list(string.lower())

  push(string)
  cnt = 0
  
  for i in string:
    char = pop()
    if char != i:
      print("회문이 아닙니다")
      break

    else:
      # print(f"회문이 될거야 : {cnt+1}/{len(string)}")
      cnt+=1
      if cnt == len(string):
        print("회문입니다")