# create a fun that will display how many items in the list have names more than 5 characters 
# names= ["atul","shubham","anurag","rahul","dev","roy"]


def a(name):
    n=0
    for i in name:
        l=len(i)
        if l>5:
            n+=1
    return n


name=["atul","shubham","anurag","rahul","dev","roy"]
c=a(name)
print(c)