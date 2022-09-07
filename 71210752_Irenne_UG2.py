'''
Irenne Dwita Natalia
71210752
Unguided 2.1
'''
import timeit

#rekursif
def deret_ajaib(n):
    if n<=5:
        return n
    else:
        return deret_ajaib(n-2)+deret_ajaib(n//2)

start = timeit.default_timer()
hasil = deret_ajaib(4)
stop = timeit.default_timer()
print("hasilnya adalah",hasil, "selama", stop-start, "detik")


#iteratif