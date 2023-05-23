# import module
# print(module.__counter)

# import sys
# for p in sys.path:
#    print(p)

# #7
# print("\n7.")
# from module import suml, prodl
# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(suml(zeroes))
# print(prodl(ones))

# #9
# print("\n9.")
from sys import path
path.append("moduls")

import module

# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(module.suml(zeroes))
# print(module.prodl(ones))

# 9+
print("\n9+.")
zeroes = [i for i in range(5)]
ones = [i for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))