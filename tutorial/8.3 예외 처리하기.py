import sys

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")


# class B(Exception):
#     pass


# class C(B):
#     pass


# class D(C):
#     pass


# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# try:
#     f = open("./tutorial/data/sam")
#     s = f.readline()
#     i = int(s.strip())
#     print("i =", i)
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as e:
#     print(f"Unexpected {e=},  {type(e)=}")

#     raise

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, "r")
#     except OSError:
#         print("cannot open", arg)
#     else:
#         print(arg, "has", len(f.readlines()), "lines")
#         f.close()

# def func():
#     raise ConnectionError

# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError("Failed to pen database") from exc


def bool_return():
    try:
        return True
    finally:
        return False


print(bool_return())
