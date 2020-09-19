import os, shutil, os.path


##old_location = "/Volumes/SAMSUNG T5/Chrome Download/untitled folder/old"
##new_location = "/Volumes/SAMSUNG T5/Chrome Download/untitled folder/new"

old_location = ""
new_location = ""

old_location_name = ""
new_location_name = ""

## Boolean if the program is all set up and ready to use
ready_to_go = False

## Function to print a line of strokes
def print_stroke():
    for i in range(100):
        print("=", end = "")
    print()

def read_location():
    ## Declare global variable
    global old_location
    global new_location
    global old_location_name
    global new_location_name
    global ready_to_go

    ## Boolean to check if the old and new path is ready
    old_ready = False
    new_ready = False

    ## Try reading for old location
    ## If it does not exist, we create one for them
    try:
        f = open("oldpath.txt")
        old_location = f.readline()
        if(old_location == ""):
            print_stroke()
            print()
            print("Initial path is empty")
            print("Please save your initial directory path in the text file")
        else:
            print_stroke()
            print()
            old_location_name = os.path.basename(old_location)
            directory_exist = os.path.isdir(old_location)
            ## Check if the initial directory exist
            ## If it exist, we set the new path to be ready
            ## Otherwise, we inform the user
            if directory_exist:
                old_ready = True
                print("Initial Location: " + old_location)
            else:
                print("Initial Location does not exist")
                print("Make sure the path you saved is correct")
        f.close
    except FileNotFoundError:
        f = open("oldpath.txt", "w") 
        print_stroke()
        print()
        print("oldpath.txt created")
        print("Please save your initial directory path in the text file")
        f.close

    ## Try reading for new location
    ## If it does not exist, we create one for them
    try:
        f = open("newpath.txt")
        new_location = f.readline()
        if(new_location == ""):
            print()
            print("End path is empty")
            print("Please save your end directory path in the text file")
        else:
            print()
            new_location_name = os.path.basename(new_location)
            ## Check if the new directory exist
            ## If it exist, we set the new path to be ready
            ## Otherwise, we inform the user
            directory_exist = os.path.isdir(new_location)
            if directory_exist:
                new_ready = True
                print("New Location: " + new_location)
            else:
                print("New Location does not exist")
                print("Make sure the path you saved is correct")
        f.close
    except FileNotFoundError:
        f = open("newpath.txt", "w") 
        print()
        print("newpath.txt created")
        print("Please save your end directory path in the text file")
        f.close

    ## Update the boolean to true if both inital path and new path exist
    ready_to_go = old_ready and new_ready

    ## Inform the user by printing a message
    if not ready_to_go:
        print()
        print("Please re-run the program after making new changes to the .txt file")
        print_stroke()


def move_things_to_new_directory():
    ## Declare global variable
    global old_location
    global new_location
    global old_location_name
    global new_location_name

    ## Read every folder and files in initial location
    for folder in os.listdir(old_location):
        ## Update folder path for later use
        folder_path = old_location + "/" + folder
        ## Save current and final directory location
        current_location = folder_path
        final_location = current_location
        ## Check if the current path is a directory
        isDirectory = os.path.isdir(folder_path)
        ## Keep looping through the folders until it is the final directory
        while isDirectory == True:
            allFiles = os.scandir(current_location)
            ## Check if all the files scanned is a directory or not
            ## If true, we keep looping
            ## Otherwise, we stop and save the final directory path
            for file in allFiles:
                if file.is_dir():
                    ## Update the current directory path
                    current_location = current_location + "/" + file.name
                else :
                    ## finalise the final directory path
                    final_location = current_location
                    isDirectory = False

            if isDirectory == False:
                ## Save data for outputing on terminal
                list = os.listdir(final_location)
                number_of_files = len(list)
                folder_name = os.path.basename(final_location)
                ## Move the foler to the new directory
                shutil.move(final_location, new_location)
                print_stroke()
                ## Output message for the terminal
                print("Moved 「" + folder_name + "」 with " + str(number_of_files) + 
                " files from " + old_location_name + " to " + new_location_name)

                ## Final the length of the current folder name
                file_name_length = len(folder_name)
                ## Remove text from current directory to find its parent directory path
                parent_location = current_location[:-(file_name_length + 1)]
                ## Delete parent directory
                shutil.rmtree(parent_location)


if __name__ == "__main__": 
    read_location()
    while(ready_to_go):
        move_things_to_new_directory()
        ## Program halts when there is no more folders left
        if len(os.listdir(old_location)) == 0:
            print("Directory is empty")
            print("Program terminates")
            break
