#Write a function that takes two parameters: a prompt message and an error message.
#The function will prompt the user with the passed in prompt to enter an integer
#If the text entered cannot be cast to an int, display the error message.
#The function will continue to prompt the user to enter an integer until a proper integer is entered.
#The most direct way of doing this would be using a try block, which has not been covered yet. You will need to research this.
#Write supporting code to call the function, and then display the number that was entered.



def check():
    Confirm = 0
    
    while Confirm == 0:
        try:
            Firstnumber = input("input an intiger: ")
            int(Firstnumber)
            print(f"The numebr that was entered is {Firstnumber}")
            Confirm =+ 1
        except:
            print("Error: Entered text could not be cast to an intiger")

check()