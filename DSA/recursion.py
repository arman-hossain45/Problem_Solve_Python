# def greet():
#     print("arman")
#     greet()

# greet()#it show stack overflow error this fun is called again again 
#we want to reduce the space for this reason we want to give a stop condition 

def fun(count=0):
    if count == 4:
        return
    count += 1
    fun(count)
    print("Arman")

fun()





