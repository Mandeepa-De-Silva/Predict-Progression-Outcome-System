# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1985618
# Date: 11/04/2023

# I referred by https://www.geeksforgeeks.org/python-time-module/ to attractive the programme with time delay
import time

# multiline printing
print("""
                        ~INSTRUCTIONS!

1. Enter correct credits to run this programme without any issue..
2. You can enter only integers..
3. Your credit range must be 0 or above and 120 or below..
4. Your credit must be one of these 0,20,40,60,80,100,120


                    Let's start the programme!!

""")

# count start for the inputs
progress_c = trailer_c = retriever_c = exclude_c = total_c = 0
Continue = "y"


# functions for validate user inputs
def check_validity(credit):
    while True:
        try:
            user_credit_input = int(input("Enter your " + credit + "credit: "))
            # only valid credit values are 0, 20, 40, 60, 80, 100, 120
            if user_credit_input not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range (-_-)\n")  # credits not in range repeat for user inputs
                continue
            else:
                break
        except ValueError:
            print("Integer required (-_-)\n")  # if user inputs are not integers
            continue
    return user_credit_input


# validation for run programme with correct path
options = [1, 2]
x = 0
while True:
    try:
        # Press 1 or 2 to select correct path
        x = int(input("If you are student press 1\nIf you are staff member press 2\n"))

        print("")
        if x not in options:
            # if user inputs are not 1 pr 2
            print("'1' or '2' required to continue the programme (-_-)\n")
            continue  # then continue the loop
        else:
            break
    except ValueError:
        print("Integer required (-_-)\n")
        continue

# if user input is 1 then run student version of the programme
# if user input is 2 then run staff version of the programme
if x == 1:
    print("Student version\n")
    while True:
        # user input credits goes to check_validity function and compare with validation
        Pass_credit, Defer_credit, Fail_credit = check_validity(
            "pass "), check_validity("defer "), check_validity("fail ")
        # total credit is addition with pass,defer,fail credits
        total_credit = Pass_credit + Defer_credit + Fail_credit
        # total credit must be equal to 120
        if total_credit == 120:
            break
        else:
            print("Total incorrect (-_-)\n")
            continue

    if Pass_credit == 120:
        progress_c += 1  # counting inputs
        print("Progress\n")
    elif Pass_credit == 100:
        trailer_c += 1
        print("Progress (module trailer)\n")
    elif Fail_credit >= 80:
        print("Exclude\n")
    else:
        print("Module retriever\n")
    total_c += 1  # user entered data storing and count one by one

else:
    print("Staff version with histogram\n")
    while Continue == "y":
        while True:
            # user input credits goes to check_validity function and compare with validation
            Pass_credit, Defer_credit, Fail_credit = check_validity(
                "pass "), check_validity("defer "), check_validity("fail ")
            # total credit is addition with pass,defer,fail credits
            total_credit = Pass_credit + Defer_credit + Fail_credit
            # total credit must be equal to 120
            if total_credit == 120:
                break
            else:
                print("Total incorrect (-_-)\n")
                continue
            
        if Pass_credit == 120:
            progress_c += 1  # count one by one
            print("Progress\n")
        elif Pass_credit == 100:
            trailer_c += 1
            print("Progress (module trailer)\n")
        elif Fail_credit >= 80:
            exclude_c += 1
            print("Exclude\n")
        else:
            retriever_c += 1
            print("Module retriever\n")
        total_c += 1  # user entered data storing and count one by one

        # if user wants to continue with another set of data press y and else q
        options = ["y", "q"]
        while True:
            Continue = str(input("Would you like to enter another set of data? \n"
                           "Enter 'y' for yes or 'q' for quit and view results with histogram\n")).lower()
            print("")
            if Continue not in options:
                print("'y' or 'q' required as an input (-_-)\n")  # to run the programme correctly
                continue
            else:
                break

        if Continue == "q":
            # if user press q then end the programme with histogram
            print("-"*50)
            print("Histogram")
            time.sleep(4)
            print("Progress", f'{progress_c:4}', ":", progress_c * "*")
            time.sleep(4)
            print("Trailer", f'{trailer_c:5}', ":", trailer_c * "*")
            time.sleep(3)
            print("Retriever", f'{retriever_c:3}', ":", retriever_c * "*")
            time.sleep(3)
            print("Excluded", f'{exclude_c:4}', ":", exclude_c * "*")
            time.sleep(3)
            print(total_c, "outcomes in total.")
            print("-"*50)
        else:
            # if user press y then loop will continue and ask to get another set of data
            continue
