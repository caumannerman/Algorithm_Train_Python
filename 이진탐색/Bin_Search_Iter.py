
#이미 정렬된 리스트
array1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

# target이 몇 번 째 인덱스에 있는지 그 번호를 return 해준다
def BS_iter(array, target, start, end):
# while문 안의 마지막 if문을 지우고 , while start <= end로 해주면 더 간결.
    while True:
        mid = (start + end) //2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
        # 이곳을 start >= end가 아니라 start > end로 해주는 이유는, 다음과 같다
        # start = 4, end = 5 인 상태고, target =5라고 생각해보자.
        # mid = (4+5) //2 로 4가 되고, 아래의 else문에 의해 start = mid +1 즉, start 는 5가 되어 start = end = 5가 된다.
        # 다시 한번 돌아와 mid = (5+5) //2 가 되어 mid = 5가 되고,  array[mid] == target이 되어 return mid로 정상종료가 된다.
        # 즉, start == end인 상태는 아직 함수가 mid를 반환하며 종료할 수 있는 가능성이 열려있는 상태이므로 target이 array에 없다고 보장할 수 없다.
        if start > end:
            return None


target = int(input("찾고자 하는 숫자를 입력하세요 : "))

result = BS_iter(array1, target,0,len(array1)-1)
# 여기 매개변수를 넣어줄 때 end의 위치에 len(array1) -1로 딱 마지막원소 index를 맞춰 넣어줘야함. 아니면, 배열의 모든 원소들보다 큰 target이 들어왔을 때 index out of range뜸.
if result == None:
    print("해당 target은 존재하지 않습니다!")

print(result, "번 째 인덱스에 위치해있음")


