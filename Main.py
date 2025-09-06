import Exercise_1 as ex1
import Exercise_2 as ex2
import Exercise_3 as ex3
import Exercise_4 as ex4
import Exercise_5 as ex5
import Exercise_6 as ex6
import matplotlib.pyplot as plt

# Main
# Exercise 1
print ("Câu 1a: ", ex1.f_1a(10))
print ("Câu 1b: ", ex1.f_1b(10))
print ("Câu 1c: ", ex1.f_1c(10))
print ("Câu 1d: ", ex1.f_1d(10))
print ("Câu 1e: ", ex1.f_1e(10))
print ("Câu 1f: ", ex1.f_1f(10))
print ("Câu 1g: ", ex1.f_1g(10))
print ("Câu 1h: ", ex1.f_1h(10))
print ("Câu 1i: ", ex1.f_1i(10))
print ("Câu 1j: ", ex1.f_1j(10))
print ("Câu 1k: ", ex1.f_1k(10))
print ("Câu 1l: ", ex1.f_1l(10))
print ("Câu 1m: ", ex1.f_1m(10))
print ("Câu 1n: ", ex1.f_1n(10))

# Exercise 2
print ("Max 2a: ", ex2.Find_fmax(ex2.f_2a, -2, 2))
print ("Min 2a: ", ex2.Find_fmin(ex2.f_2a, -2, 2))
print ("Max 2b: ", ex2.Find_fmax(ex2.f_2b, 0, 5))
print ("Min 2b: ", ex2.Find_fmin(ex2.f_2b, 0, 5))
print ("Max 2c: ", ex2.Find_fmax(ex2.f_2c, 5, 10))
print ("Min 2c: ", ex2.Find_fmin(ex2.f_2c, 5, 10))
print ("Max 2d: ", ex2.Find_fmax(ex2.f_2d, -3, 3))
print ("Min 2d: ", ex2.Find_fmin(ex2.f_2d, -3, 3))
print ("Max 2e: ", ex2.Find_fmax(ex2.f_2e, -3, 3))
print ("Min 2e: ", ex2.Find_fmin(ex2.f_2e, -3, 3))

# Exercise 3
print ("Câu 3a: ", ex3.f_3a)
print ("Câu 3b: ", ex3.f_3b)
print ("Câu 3c: ", ex3.f_3c)
print ("Câu 3d: ", ex3.f_3d)

# Exercise 4
ex4.draw(ex4.fx_4i, -5, 5, 0.01, "red", "4i")
ex4.draw(ex4.fx_4j, -5, 5, 0.01, "blue", "4j")
ex4.draw(ex4.fx_4k, -5, 5, 0.01, "green", "4k")
ex4.draw(ex4.fx_4l, -5, 5, 0.01, "black", "4l")
ex4.draw(ex4.fx_4m, -5, 5, 0.01, "orange", "4m")
ex4.draw(ex4.fx_4n, -5, 5, 0.01, "gray", "4n")

# Exercise 5
ex5.draw(ex5.fx_1, -2, 2, 0.000001, "red", "5_f1")
ex5.draw(ex5.fx_2, -2, 2, 0.000001, "pink", "5_f2")
plt.grid()
plt.show()

# Exercies 6
for ki in range(2, 13, 2):
    ex6.draw(ex6.fx_6a, ki, -10, 10, 0.1, "red")
    ex6.draw(ex6.fx_6b, ki, -10, 10, 0.1, "blue")