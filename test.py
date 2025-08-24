class Washer:
	height = 800 
	def wash(self):
		print("洗衣服")
		print(self)
wa = Washer()
print(wa)
wa.wash()
#输出内存地址一致，说明self就是实例化对象本身