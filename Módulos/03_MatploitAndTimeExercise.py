import matplotlib.pyplot as plt
import time as t

word = "caca"
mistakes = 0
results = []
for x in range(0,5):
    start_time = t.time()
    user_word = input("Type the word "+word+": ")
    end_time = t.time()
    if(user_word.lower()!=word):
        mistakes+=1
    results.append(round(end_time-start_time,2))
print("Number of mistakes:",mistakes)

x = [1,2,3,4,5]
y = results
plt.xlabel("Attemps")
plt.xticks(x,x)
plt.ylabel("Seconds")
plt.plot(x,y)
plt.show()