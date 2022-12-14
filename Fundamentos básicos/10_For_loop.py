blog_posts = ["The 10 coolest math functions","", "ABCNDDADS", "A Tutorial Python"]

for index,post in enumerate(blog_posts):
    if(post == ""):
        continue
    else:
        print(index,post)

myString = "Python for beginners"

for char in myString:
    print(char)

for x in range(0,10):
    print(x)

person = {"name":"Marcos","age":23}
for key in person:
    print(key,person[key])

blog_posts = {"Python": ["The 10 coolest math functions","Python for beginners"], "JavaScript": ["ABCNDDADS JavaScript"],"Pascal":["A Tutorial Pascal"]}

for category in blog_posts:
    print("CATEGORY:",category)
    for index,name in enumerate(blog_posts[category]):
        print(index+1,"Name:",name)


