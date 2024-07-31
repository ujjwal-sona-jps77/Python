ram = int(input(" Ram Enter your age :- "))
shyam = int(input(" Shyam Enter your age :- "))
ujjwal = int(input("Ujjwal Enter your age :- "))

if ram > shyam and ram > ujjwal :
    print("Ram is gretaer than Syam and Ujjwal.")
elif shyam > ram and shyam > ujjwal :
    print("Shyam is greater than Ram and Ujjwal .")
elif ujjwal > ram and ujjwal > shyam :
    print("Ujjwal is greater than Ram and Shyam.")
elif ram == shyam and ram > ujjwal :
    print("Ram is greater than Ujjwal and equal to Shyam.")
elif shyam == ram and shyam > ujjwal :
    print("Shyam is greater than Ujjwal and equal to Ram.")
elif ujjwal == ram and ujjwal > shyam :
    print("Ujjwal is grater than Shyam and equal to Ram . ")
elif ram == ujjwal and ram > shyam :
    print("Ram is greater than Shyam and equal to Ujjwal.")
elif shyam == ujjwal and shyam > ram :
    print("Shyam is greater than Ram and equal to Ujjwal.")
elif ujjwal == shyam and ujjwal > ram :
    print("Ujjwal is grater than Ram and equal to Shyam . ")
else: 
    print("Error")
    
# Complete

num = int(input("Enter the number :- "))
if (num % 2 == 0) :
    print("The number is Even")
else:
    print("The number is Odd.")

year = int(input("Enter the year :- "))
if (year % 4 == 0):
    print("Year is a leap year")
else :
    print("Year is not a leap year.")


    

    


