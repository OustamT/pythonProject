from sys import path
# path.append("packages")

# import extra.iota
# print(extra.iota.FunI())

# from extra.iota import FunI
# print(FunI())

# import extra.good.best.sigma
# from extra.good.best.tau import FunT
# print(extra.good.best.sigma.FunS())
# print(FunT())

# import extra.good.best.sigma as sig
# import extra.good.alpha as alp
# print(sig.FunS())
# print(alp.FunA())

path.append("packages\\Extrapack.zip")
import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB
print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())
