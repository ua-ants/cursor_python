# Task 2: Указать в каком порядке будет происходить поиск атрибутов
#         и методов в классе E если существует такая иерархия классов
#         (Все классы нового стиля!!!):

class A:
        pass

class B:
        pass

class C(B, A):
        pass

class D(C, A):
        pass

class E(D, B):
        pass

e = E
print(e.mro())

# Manua calculation:
# L(A) = [A, Obj]
# L(B) = [B, Obj]
# L(C) = [C] + merge(L(B),L(A),[B,A]) = [C] + merge([B,Obj],[A,Obj],[B,A]) = [C,B,A,Obj]
# L(D) = [D] + merge(L(C),L(A),[C,A]) = [D] + merge([C,B,A,Obj],[A,Obj],[C,A]) = [D,C,B,A,Obj]
# L(E) = [E] + merge(L(D),L(B),[D,B]) = [E] + merge([D,C,B,A,Obj],[B, Obj],[D,B]) = [E,D,C,B,A,Obj]
#
# sources[1]: https://habr.com/post/62203/
# sources[2]: https://ru.wikipedia.org/wiki/C3-%D0%BB%D0%B8%D0%BD%D0%B5%D0%B0%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F
