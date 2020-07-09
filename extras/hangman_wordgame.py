# hangman
import getpass
word = getpass.getpass("Enter the Word for the Hang-Man Game: ")

# find out how many characters are in this word
# useful for separating the individual characters for the game
word_length = len(word)

# Put the input word into a list.
# This splits the word into individual characters
# it will look like ["h","e","l","l","o"]
char_list = list(word)
# set an empty list for processing the display
display_list = []

# for each character in the character list
# add it into the display_list
# it will change hello to ["_ ","_ ","_ ","_ ","_ ",]
for char in char_list:
    display_list.append("_ ")
# joins the list into string with .join function
display_string = "".join(display_list)

# initial display dashes
print(display_string)

# function to change the value in the list,
# and join it to a string
def show_char(player_input):
    global tries
    # for each char in character list
    for i, char in enumerate(char_list):
        # is the input character is identical to a char in the list
        if player_input == char:
            # change the display from "_" to the character
            display_list[i] = char_list[i]
    if player_input not in char_list:
        # add one try to the try variable after an nput
        tries += 1
    # join the list back into a string
    display_string = "".join(display_list)
    
    # return the value back to the function or part of the program
    # which called the show_char() function
    print(display_string)

def check_win(display_list,char_list):
    # call the done variable from outside of the function
    global done
    global tries
    global max_tries
    print("You have",max_tries - tries,"tries left")
    # if tries is less than or equal to max_tries,
    if tries <= max_tries and display_list == char_list:
        print("You win!")
        done = True

    # else if there are no more empty slots in display_list
    elif tries >= 5:
        print("You Lose!")
        done = True
    else:
        pass    
    
tries = 0
max_tries = 10 # set maximum number of tries

done = False

while done == False:
    player_input = input("Guess a character: ")
    # parse player_input value to show_char() function
    # sprints the return string from the function show_char()
    show_char(player_input)
    check_win(display_list, char_list)
    
while done == True:
    quit()

