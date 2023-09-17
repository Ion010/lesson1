b = 3  #int
a = 3.14 #float
d =  'my text' #string/
boolean = True  # sau False = 0

#print(b)
#print(a)
#print(d)
#print(boolean)

#print(b + a) #1 + b
#print(b - a) #1 - b
#print(b / a) #1 * b
#print(b * a) #1 / b

#print(4/2)
#print(4/3)





#value_int = int(input("Enter a int")) #int
#value_float = float(input("Enter a float")) #float
#value_string = input("Enter a int") #string
#value_boolean = bool(input("Enter a boolean")) #boolean
#rint(value_int)
#print(value_float)
#print(value_string)
#print(value_boolean)





#str_var = "4"
#print(int(str_var))
#print(float(str_var))
#print(bool(str_var))








#major = 23
#var_input = int(input("Enter a number"))


#if major < var_input : #TRUE  #Condition 1
    #print( "<" ) ##True
#elif major == var_input: #Condition 2
    #print("=")
#else: #Else #Condition 3
    #print(">") #False




#var1 = "string"
#var2 = input("Enter a value")

#if var1 == var2:
    #print("Corect")
#else:
    #print("gresit")



#for count in range(1, 10):
    #print(count)


#var = 1
#while var < 100:
    #print(var)
    #var = var + 10












import random

var_check = random.randint(0, 25)
var_in = int(input("Enter a number"))
while var_in != var_check:

    if var_in < var_check:
        print("Less than need")
    else:
        print("More than need")
    var_in = int(input("Enter a number"))
else:
    print("Cong")












