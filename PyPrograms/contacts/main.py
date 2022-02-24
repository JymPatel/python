# code by @JymPatel
# edited by @bupboi1337, (editors can put their name here && thanks for contribution :)

# this code uses GPL V3 LICENSE
print("this code uses GPL V3 LICENSE")
print("")

# start of code
# import library
import pickle
import os
# imports from our py files
import functions as fuN

# get array from pickle data
infile = open('data/pickle-main', 'rb')
# defining array
array = pickle.load(infile)
infile.close()

# get key if path exists
keyacess = False
path = 'data/pickle-key'
if os.path.isfile('data/pickle-key'):
    pklekey = open('data/pickle-key', 'rb')
    key = pickle.load(pklekey)
    pklekey.close()
    if key == 'SKD0DW99SAMXI19#DJI9':
        keyacess = True
        print("key found & is correct")
        print("ALL FEATURES ENABLED")
    else:
        print("key is WRONG\nSOME FEATURES ARE DISABLED")
        print("check https://github.com/JymPatel/Python-FirstEdition/tree/Main/PyPrograms/contacts for key, it's free")
else:
    print("key not found\nSOME FEATURES ARE DISABLED")
    print("check https://github.com/JymPatel/Python-FirstEdition/tree/Main/PyPrograms/contacts for key, it's free")

print("")
print("update-22.02 ADDS SAVING YOUR DATA WHEN CLOSED BY SAVING USING OPTION 0\n##")

# for ease in reading
fname = 0
lname = 1
number = 2
email = 3
# getting some variables
promptvar = 0 # variable for prompt
loopvar = 0 # variable for main loop
# making loop to run
while loopvar < 1:
    # ask user what to do
    print("")  # putting blank line before running new loop
    if promptvar == 0:
        print("0.  exit program")
        print("1.  get all contacts")
        print("2.  add new contact")
        print("3.  remove any contact")
        print("4.  sort contacts by first name")
        print("9.  stop getting this prompt")

    a = input("WHAT WOULD YOU LIKE TO DO?  ")

    # check for integer & calculate length of array
    try:
        a = int(a)
    except ValueError:
        print("!! PLEASE ENTER AN INTEGRAL VALUE")
    # get length of array
    print(array)
    arraylen = len(array[fname])

    # if option 1 is selected
    if a == 1:
        fuN.printallcontacts(arraylen, array)

    # option 2 is selected
    elif a == 2:
        array = fuN.addnewcontact(arraylen, array)
        arraylen += 1

    # option 3
    elif a == 3:
        array = fuN.deleteOldContact(arraylen, array)
        arraylen -= 1

    # if option 4 is selected
    elif a == 4:
        if keyacess == True:
            sortcounter = 1
            while sortcounter != 0:
                # reset counter
                sortcounter = 0
                arraylen = len(array[fname])
                for i in range(arraylen - 1):
                    if array[fname][i].upper() > array[fname][i + 1].upper():
                        for j in range(4):
                            temp = array[j][i]
                            array[j][i] = array[j][i + 1]
                            array[j][i + 1] = temp
                        # add one for changing values
                        sortcounter += 1
                    if array[fname][i].upper() == array[fname][i + 1].upper():
                        # if first name are same, compare last
                        if array[lname][i].upper() > array[lname][i + 1].upper():
                            for j in range(4):
                                temp = array[j][i]
                                array[j][i] = array[j][i + 1]
                                array[j][i + 1] = temp
                            # add one for changing values
                            sortcounter += 1
            # if no values are swapped, sortcounter = 0; no next loop
            print("CONTACTS ARE NOW SORTED")
        else:
            print("NEED CORRECT KEY TO ENABLE THIS FEATURE")

    # option 9
    elif a == 9:
        if keyacess:
            # change prompt settings
            if promptvar == 0: 
                promptvar += 1
                print("you won't get prompt now!")
                print("ENTER 9 AGAIN TO START GETTING PROMPT AGAIN!!")
            else:
                promptvar -= 1
        else:
            print("NEED CORRECT KEY TO ENABLE THIS FEATURE")


    # if option 0 is selected
    elif a == 0:
        print("Saving your Data ...")
        outfile = open('data/pickle-main', 'wb')
        pickle.dump(array, outfile)
        outfile.close()
        print("YOUR DATA HAS BEEN SAVED SUCESSFULLY!")
        loopvar += 1

    # if no true option is selected
    else:
        print("!! PLEASE ENTER VALUE FROM GIVEN INTEGER")

# end of code
print("")
print("get this code at https://github.com/JymPatel/Python-FirstEdition")