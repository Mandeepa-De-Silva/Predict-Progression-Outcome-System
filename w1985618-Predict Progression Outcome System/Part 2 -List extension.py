# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1985618
# Date: 13/04/2023

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

progress_d, trailer_d, retriever_d, exclude_d = [], [], [], []


# functions for validate user inputs
def check_validity(credit):
    while True:
        try:
            user_credit_input = int(input("Enter your " + credit + "credit: "))
            # only valid credit values are 0, 20, 40, 60, 80, 100, 120
            if user_credit_input not in [0, 20, 40, 60, 80, 100, 120]:
                # credits not in range repeat for user inputs
                print("Out of range (-_-)\n")
                continue
            else:
                break
        except ValueError:
            print("Integer required (-_-)\n")  # if user inputs are not integers
            continue
    return user_credit_input


print("Staff version and histogram with list\n")
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

    # tuple for validate user inputs credits
    credit_tuple = (Pass_credit, Defer_credit, Fail_credit)
    # store progression outcomes and sort user input data sets
    if Pass_credit == 120:
        print("Progress\n")
        progress_c += 1
        progress_d.append(credit_tuple)  # add credits to credit tuple
    elif Pass_credit == 100:
        print("Progress (module trailer)\n")
        trailer_c += 1
        trailer_d.append(credit_tuple)
    elif Fail_credit >= 80:
        print("Exclude\n")
        exclude_c += 1
        exclude_d.append(credit_tuple)
    else:
        print("Module retriever\n")
        retriever_c += 1
        retriever_d.append(credit_tuple)
    total_c += 1  # user entered data storing and count one by one

    # if user wants to continue with another set of data press y and else q
    options = ["y", "q"]
    while True:
        Continue = str(input("Would you like to enter another set of data? \n"
                             "Enter 'y' for yes or 'q' for quit and view results with histogram\n")).lower()
        print("")
        if Continue not in options:
            # to run the programme correctly
            print("'y' or 'q' required as an input (-_-)\n")
            continue
        else:
            break

    if Continue == "q":
        # if user press q then end the programme with histogram
        print("-" * 50)
        print("Histogram")
        time.sleep(4)
        print("Progress", f'{progress_c:4}', ":", progress_c * "*")
        time.sleep(2)
        print("Trailer", f'{trailer_c:5}', ":", trailer_c * "*")
        time.sleep(2)
        print("Retriever", f'{retriever_c:3}', ":", retriever_c * "*")
        time.sleep(2)
        print("Excluded", f'{exclude_c:4}', ":", exclude_c * "*")
        time.sleep(2)
        print(total_c, "outcomes in total.")
        print("-" * 50)
    else:
        # if user press y then loop will continue and ask to get another set of data
        continue


# function for unpack progression data list
def unpack_list(p_outcome, p_out_cat):
    # print the list with loop
    for i in range(len(p_outcome)):
        print(p_out_cat, end=" ")
        time.sleep(2)
        # I referred this website https://flexiple.com/python/python-print-list/ how to remove parentheses from tuple
        print(*p_outcome[i], sep=", ")
        # remove all parentheses form tuple and separate by comma
        time.sleep(2)


unpack_list(progress_d, "progress -")
unpack_list(trailer_d, "progress (module trailer) -")
unpack_list(retriever_d, "Module retriever -")
unpack_list(exclude_d, "Exclude -")
