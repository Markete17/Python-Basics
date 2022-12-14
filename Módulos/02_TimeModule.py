import time as t
time_now = t.localtime()
print("Completed at: "+str(time_now.tm_hour) +"h" +str(time_now.tm_min)+"m")

time_now = t.time() # segundos desde 01-enero-1070 00:00h
deliveryTyme = time_now + (86400*7) # segundos en un día
print(t.localtime(deliveryTyme))

t.sleep(5)