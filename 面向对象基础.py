class Washer:
    height = 1.0
    def wash(self):
        print("洗衣服")
        print(self)
print(Washer.height)
#1.0 
Washer.weight = 2000
 
print(Washer.weight)

wa = Washer() #实例化对象

print(wa)
wa = Washer()
print(wa)
wa.wash()

