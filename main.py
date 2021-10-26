import random
import time
import mouse

i = 0
while i < 1:
	rnd = random.randint(0, 1000)
	mouse.move(str(rnd), str(rnd))
	time.sleep(3)
