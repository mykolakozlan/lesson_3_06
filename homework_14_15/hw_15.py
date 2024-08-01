# import numbers
# import math
#
#
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         # return math.ceil(self.width * self.height)
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return NotImplemented
#
#     # def __add__(self, other):
#     #     if isinstance(other, Rectangle):
#     #         square = self.get_square() + other.get_square()
#     #         x = square ** 0.5
#     #         return Rectangle(x, x)
#     #     return NotImplemented
#
#     # def __add__(self, other):
#     #     return Rectangle(1, self.get_square() + other.get_square())
#
#     # def __add__(self, other):
#     #     combined_area = self.get_square + other.get_square
#     #     return Rectangle(combined_area ** 0.5, combined_area / (combined_area ** 0.5))
#
#     # def __add__(self, other):
#     #     r1_r2_square = self.get_square() + other.get_square()
#     #     another_width = 2
#     #     another_height = r1_r2_square // 2
#     #     return Rectangle(another_width, another_height)
#
#     # def __add__(self, other):
#     #     total_square = self.get_square() + other.get_square()
#     #     return Rectangle(self.width, total_square / self.width)
#
#     # def __mul__(self, n):
#     #     if isinstance(n, numbers.Real):
#     #         return Rectangle(self.width, self.height * n)
#     #     return NotImplemented
#
#     # def __mul__(self, n):
#     #     new_width = self.width * (n ** 0.5)
#     #     new_height = self.height * (n ** 0.5)
#     #     return Rectangle(new_width, new_height)
#
#     def __str__(self):
#         return "Rectangle [width = {}, height = {}, square = {}]".format(self.width, self.height, self.get_square())
# #
# #
# # r1 = Rectangle(2, 4)
# # r2 = Rectangle(3, 6)
# #
# # assert r1.get_square() == 8, 'Test1'
# # assert r2.get_square() == 18, 'Test2'
# #
# # r3 = r1 + r2
# # assert r3.get_square() == 26, 'Test3'
# #
# # r4 = r1 * 4
# # assert r4.get_square() == 32, 'Test4'
#
#
#
#
#
#
#
#
# class Fraction:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __mul__(self, other):
#         """a/b * c/d = a*c / b*d"""
#         if isinstance(other, Fraction):
#             numerator = self.a * other.a
#             denominator = self.b * other.b
#             return Fraction(numerator, denominator)
#         return NotImplemented
#
#     def __add__(self, other):
#         """a/b + c/d = a*d + c*b / b*d"""
#         if isinstance(other, Fraction):
#             numerator = self.a * other.b + other.a * self.b
#             denominator = self.b * other.b
#             return Fraction(numerator, denominator)
#         return NotImplemented
#
#     def __sub__(self, other):
#         """a/b - c/d = a*d - c*b / b*d"""
#
#         if isinstance(other, Fraction):
#             numerator = self.a * other.b - other.a * self.b
#             denominator = self.b * other.b
#             return Fraction(numerator, denominator)
#         return NotImplemented
#
#     def __eq__(self, other):
#         if isinstance(other, Fraction):
#             return self.a / self.b == other.a / other.b
#         return NotImplemented
#
#     def __gt__(self, other):
#         """a/b > c/d = a*d > c*b"""
#
#         if isinstance(other, Fraction):
#             return self.a * other.b > other.a * self.b
#         return NotImplemented
#
#     def __lt__(self, other):
#         """a/b < c/d = a*d < c*b"""
#
#         if isinstance(other, Fraction):
#             return self.a * other.b < other.a * self.b
#         return NotImplemented
#
#     def __str__(self):
#         return f"Fraction: {self.a}, {self.b}"
#
#
# f_a = Fraction(2, 3)
# f_b = Fraction(3, 6)
# f_c = f_b + f_a
# assert str(f_c) == 'Fraction: 21, 18'
# f_d = f_b * f_a
# assert str(f_d) == 'Fraction: 6, 18'
# f_e = f_a - f_b
# assert str(f_e) == 'Fraction: 3, 18'
#
# assert f_d < f_c  # True
# assert f_d > f_e  # True
# assert f_a != f_b  # True
# f_1 = Fraction(2, 4)
# f_2 = Fraction(3, 6)
# assert f_1 == f_2  # True
# print('OK')
