# with open("./tutorial/data/sam", "w", encoding="utf-8") as f:  #
#     data = ""
#     for i in range(1, 11):
#         data += f"{i}번째 줄입니다.\n"

#     f.write(data)

with open("./tutorial/data/sam", "r", encoding="utf-8") as f:
    while True:
        str = f.readline()
        if not str:
            break
        i = 1
        regno = ""
        for s in str:
            if i >= 12 and s != "":
                regno += s
            i += 1

        print(str, end="")
        print(f"주민번호: {regno}")

g, c, d = (
    11,
    (2),
    (8401301918719),
)
# print(g == 11)

users = {
    "lee": 5678,
    "park": 9012,
    "kim": 1234,
}
import json

j = json.dumps(users, indent=4, sort_keys=True)

o = json.loads(j)
# print(o)
apple = 2
banana = 3
cranberry = 1
detox = (banana**2 - 4 * apple * cranberry) // apple
print(detox)
