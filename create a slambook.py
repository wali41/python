import sys

def initial_slambook():
    rows,cols = int(input("please enter number of yours:")),5
    slam_book = []
    print(slam_book)
    for i in range (rows):
        print("/n enter your %d details in the following order(ONLY):"%(i+1))
        print("note: * indicates mandatory fields")
        print
        ("......................................................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
            if j == 1:
                temp.append(int(input("Enter  number*: ")))

            if j == 2:            
                temp.append(str(input("Enter  something about your friend*: ")))

            if temp[j]  == '' or temp[j] == ' ':
                temp[j] = None
            if j == 3:
                temp.append(str(input("enter date of birth (dd/mm/yy): ")))


            if temp[j] == '' or temp[j] == ' ':
    # Even if this field is left as blank, None will take the blank's place
                temp[j] = None

    if j == 4:
        temp.append(
        str(input("Enter category (Family/Friends/Work/Others): "))
    )
    # Even if this field is left as blank, None will take the blank's place
    if temp[j] == "" or temp[j] == ' ':
        temp[j] = None

    slam_book.append(temp)
# By this step we are appending a list temp into a list slam_book
# That means slam_book is a 2-D array and temp is a 1-D array

    print(slam_book)
    return slam_book


def menu():
    # We created this simple menu function for
    # code reusability & also for an interactive console
    # Menu func will only execute when called
    print("********************************************")    
                    
                          
                             
        
            