class MyEmptyClass:
    pass


def initlog(*args):
    pass  # Remember to implement this!


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"


print(http_error(400))


def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)


ask_ok("파일을 덮어써도 좋습니까?", 2, "Yes or no, please!")
