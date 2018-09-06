#write the digits of a number in reverse order
def rev(number):
    if number < 10:
        print(number, end = "")
    else:
        print(number % 10, end="")
        rev(number // 10)
  
rev(375)
#prints 573
print()


#if i were to write the print statement after the recursive call to the function, then the digits would be printed
#from first to last. this happens because the print statement in the else block is evaluated only after the call stack
#starts being cleared
def rev2(number):
    if number < 10:
        print(number, end = "")
    else:
        rev2(number // 10)
        print(number % 10, end="")

rev2(375)