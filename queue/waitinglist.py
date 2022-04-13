def isQueueFull():
  global SIZE, queue, front, rear
  if rear == SIZE-1:
    return True
  else :
    return False

def isQueueEmpty():
  global SIZE, queue, front,rear
  if front == rear:
    return True
  else :
    return False

def enQueue(data):
  global SIZE, queue, front, rear
  if (isQueueFull()):
    print("큐가 꽉 찼습니다")
    return
  rear +=1
  queue[rear] = data

def deQueue():
  global SIZE, queue, front, rear
  if (isQueueEmpty()):
    print("큐가 비었습니다")
    return None
  front+=1
  data = queue[front] #맨 앞에 있는 데이터부터 내보내기
  queue[front] = None

  for i in range(front+1,rear+1):
    queue[i-1] = queue[i] #현재 있는 데이터를 앞으로 전달
    queue[i] = None #현재 데이터는 None으로 바꾸기
  front =-1 #front를 -1로 바꾸기 (입구로 이동)
  rear -= 1 #rear가 가리키는 곳을 한칸 당기기

  return data

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == "__main__":
  enQueue("A")
  enQueue("bA")
  enQueue("sA")
  enQueue("dA")
  enQueue("wA")

  print("대기 줄 상태 :",queue)

  for i in range(rear+1):
    print(deQueue(),"님 식당에 들어감")
    print("대기 줄 상태 :",queue)
  print("식당 영업 종료")