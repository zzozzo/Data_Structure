def input_data(friend, count):
  if count <0:
    print("연락 횟수는 0과 같거나 커야합니다.\n다시 입력해주세요.")
    return 

  cnt = 0
  lis.append(None) #리스트 맨 뒤에 공백을 추가해 새롭게 들어갈 원소 포함한 길이 반영 
  list_len = len(lis)

  #-1까지 탐색하게 될 경우 맨 앞과 맨 뒤가 연결되기 때문에 0 전까지 탐색할 수 있게 하
  for i in range(list_len-1,0,-1):

    if count >= lis[i-1][1]:
      lis[i]=lis[i-1]
      lis[i-1] = None
      cnt +=1
    else : break

  position = list_len-cnt-1
  lis[position]=(friend,count)

lis = [('다현',200),('정연',150),("쯔위",90),('사나',30),('지효',15)]
if __name__=="__main__":
  while True:
      print("종료를 원하면 엔터를 눌러주세요")
      name = input("추가할 친구--> ")

      #엔터만 입력시 종료 
      if name == '':
        break;
      
      cnt = int(input("카톡 횟수--> "))
      input_data(name, cnt)
      print(lis)