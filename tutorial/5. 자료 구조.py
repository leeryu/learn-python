fruits = ["apple", "banana", "cherry", "durian", "elderberry", "apple"]  # 리스트
# print(fruits.count("apple"))  # 리스트에 apple이 몇 개 있는지 세기
# print(fruits.index("banana"))  # banana의 인덱스 찾기
fruits.append("fig")  # 리스트에 fig 추가

fruits_copy = fruits.copy()  # 리스트 복사

fruits_copy.append("grape")  # 리스트에 grape 추가
# print(fruits)
from collections import deque

queue = deque(["apple", "banana", "cherry"])  # 큐

# print(queue.popleft())  # apple 출력
# print(queue)
# queue.append("durian")  # 큐에 durian 추가
# print(queue)

squares = list(map(lambda x: x**2, range(10)))
# print(squares)
# print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
# print(combs)
# 튜플은 '불변'이고, 보통 이질적인 요소들의 시퀀스를 포함한다.
# 요소들은 언 패킹(unpacking)이 가능하다. 튜플은 리스트와 비슷하지만,
# 리스트는 변경 가능하고, 튜플은 변경 불가능하다.
t = 12345, 54321, "hello!"
u = t, (1, 2, 3, 4, 5)
# print(u)
# for i in u:
#     print(type(i))
# empty = ()
# singleton = ("hello",)  # <-- note trailing comma

# x, y, z = t
# print("x: ", x, "y: ", y, "z: ", z)
# basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
# print("computer" in basket)  # False
knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)
for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)
