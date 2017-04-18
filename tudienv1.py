

database1={'home':'ngoi nha','library':'thu vien','flat':'chung cu',
    'restaurant':'nha hang','supermarket':'sieu thi','village':'lang que',
    'museum':'bao tang','hotel':'khach san'}
    
database2={'ngoi nha':'home','thu vien':'library','chung cu':'flat','nha hang':'restaurant','sieu thi':'supermarket',
           'lang que':'village','bao tang':'museum','khach san':'hotel','benh vien':'hospital','san bay':'airport',
           'cong so':'office','qua mit':'jackfruit','qua tao':'apple','qua chuoi':'bananas','con cho':'dog','con meo':'cat','hoa':'flower',
           'cay':'trees','bac si':'doctor','y ta':'nurse','may vi tinh':'computer'}

def show_menu():
    print("="*79)                                                 
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                      WELCOME TO THE DICTIONARY PROGRAM                      |")                                         
    print("|                                                                             |")
    print("|                                                                             |")
    print("="*79)
    print("|                                      |                                      |")
    print("|              1.English-Vietnamese    |     2.Vietnamese-English             |")                                    
    print("|                                      |                                      |")
    print("="*79)
    print("|                                                                             |")
    print("|                      press '0' to exit the program                          |")
    print("|                                                                             |")
    print("="*79)
def find_av():
    word = raw_input(">>> Word to enter: ")
    if word in database1:
        print(">>>  %s  : %s "%(word, database1[word]))
    else:
        print(">>> Word '%s' is not in the dictionary ! " % word)
def find_va():
    word = raw_input(">>> Word to enter: ")
    if word in database2:
        print(">>>  %s  : %s "%(word, database2[word]))
    else:
        print(">>> Word '%s' is not in the dictionary ! " % word)
show_menu()

choice = int(raw_input("\nYour choice   : "))
while choice != 0:
    if choice == 0:
        break
    elif choice == 1:
        find_av()
    elif choice == 2:
        find_va()
    else:
        print("This opption does not have !")
    choice = int(raw_input("\nYour choice   : "))
print("\nGood bye !")

