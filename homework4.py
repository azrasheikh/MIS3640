#-------------------#
#   Azra Sheikh     #
#   MIS3640         #
#-------------------#

#imports
import os
import sys
import pandas_datareader as pdr
from time import time, sleep

#-------------------------------------------------------------------------------------------------------------
# MAIN ACTIONS
#-------------------------------------------------------------------------------------------------------------
# TRACK WATCHLISTS
def track(watchlists):

    #print watchlist
    for i, watchlist in enumerate(watchlists):
        print("\t" + str(i + 1) + " - " + watchlist)

    selection = input("Select watchlist:  ")
    while not selection.isnumeric():
        selection = input("Select watchlist:  ")

    #get watchlist from file
    f = open('./watchlists/' + watchlists[int(selection ) - 1] + ".txt", "r")

    #read lines from file
    symbols = f.readlines()
 
    symbols = [ symbol.strip() for symbol in symbols ]

    start_time = time()
    while True:
        for symbol in symbols:
            print(pdr.get_quote_yahoo(symbol)['price'])

        elapsed = time() - start_time
        if elapsed >= 10:
            prompt = input("Would you like to continue? y/n: ")
            if prompt == 'n':
                break
            start_time = time()
            elapsed = 0
        sleep(1)
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
# ADD WATCHLIST
def add_list(watchlists):
    symbols = []
    symbol = input("Enter a stock symbol: ")
    while symbol != '':
        if symbol.upper() not in symbols:
            symbols.append(symbol.upper())
        symbol = input("Enter another stock symbol: ")

    #get name for watchlist
    list_name = input("Enter a name for watchlist: ")
    while list_name == '':
         list_name = input("Enter a name for watchlist: ")

    #save watchlist
    f = open('./watchlists/' + str(list_name) + '.txt', 'w+')

    sorted(symbols)
    for symbol in symbols:
        f.write("%s\n" % symbol)
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
# DELETE WATCHLIST
def delete_list(watchlists):
    
    #print watchlist
    for i, watchlist in enumerate(watchlists):
        print("\t" + str(i + 1) + " - " + watchlist)
    
    #if no watchlist, exit
    if(len(watchlists) == 0):
        return

    selection = input("Select watchlist to delete:  ")
    while not selection.isnumeric():
        selection = input("Select watchlist to delete:  ")

    os.remove('./watchlists/' + watchlists[int(selection) - 1] + '.txt')
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
# EDIT WATCHLIST
def edit_list(watchlists):
    
    #print watchlist
    for i, watchlist in enumerate(watchlists):
        print("\t" + str(i + 1) + " - " + watchlist)
    
    #if no watchlist, exit
    if(len(watchlists) == 0):
        return

    selection = input("Select watchlist to edit:  ")
    while not selection.isnumeric():
        if selection == '':
            return
        selection = input("Select watchlist to edit:  ")

    watchlist = watchlists[int(selection) - 1]

    while True:
        selection = input("Do you want to add/delete:  ")
        while selection != "add" and selection !="delete":

            if selection == '':
                return
            selection = input("Do you want to add/delete:  ")

        #get watchlist from file
        f = open('./watchlists/' + watchlist + ".txt", "r")

        #read lines from file
        symbols = f.readlines()

        symbols = [ symbol.strip() for symbol in symbols ]

        if selection == "add":
            symbol = input("Enter a stock symbol: ")
            while symbol != '':
                if symbol.upper() not in symbols:
                    symbols.append(symbol.upper())
                symbol = input("Enter another stock symbol: ")
            
            #save watchlist
            f = open('./watchlists/' + watchlist + '.txt', 'w+')

            sorted(symbols)
            for symbol in symbols:
                f.write("%s\n" % symbol)
        
        if selection == "delete":

            #print watchlist
            for i, symbol in enumerate(symbols):
                print("\t" + str(i + 1) + " - " + symbol)

            #select ticker to remove
            selection = input("Select ticker to delete:  ")
            while not selection.isnumeric():
                if selection == '':
                    return
                selection = input("Select  ticker to delete:  ")

            #remove symbol from symbols list
            symbols.pop(int(selection) - 1)

            #save watchlist
            f = open('./watchlists/' + watchlist + '.txt', 'w+')

            sorted(symbols)
            for symbol in symbols:
                f.write("%s\n" % symbol)
 

        
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
# EXIT
def exit_program(watchlists):
    sys.exit()
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#   HELPERS
#-------------------------------------------------------------------------------------------------------------
#Lookup os directory for watchlist, If none exist create one :)
def getWatchListsFromDirectory():

    #Looks for watchlist directory, makes one if not exist
    if not os.path.exists('./watchlists'):
        os.makedirs('./watchlists')
    
    #For each file in watchlist, check if it is a file, and then add to watchlist without the file extension
    return [f.split(".")[0] for f in os.listdir('./watchlists') if f.endswith('.txt')]
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#menu from which user selects whether to track, add, delete, edit watchlist or exit the program 
def display_menu():
    print(
        """
    StockTracker Menu
    1. Track Watchlist
    2. Add Watchlist 
    3. Delete Watchlist
    4. Edit Watchlist
    5. Exit   
        """
    )
#-------------------------------------------------------------------------------------------------------------
#returns requested menu option
def requested_action(val):
    actions = {1: track, 2: add_list, 3: delete_list, 4: edit_list, 5: exit_program}

    return actions.get(int(val), None)
#-------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------- 
#prompts menu and asks for user selection
def promptAction():
    #Ask user for menu option
    menu_option = input("Enter your selection: ")

    #dictionary will return data structure if valid option, None returns if invalid. If invalid reprompt user
    while not requested_action(menu_option): 
        print("Not valid option")
        menu_option = input("Please select valid option?")

    return requested_action(menu_option)
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
def main():

    while True:
        #update list if new watchlist is created
        watchlists = getWatchListsFromDirectory()

        #render menu
        display_menu()

        #get user input
        action = promptAction()

        #call function
        action(watchlists)
#-------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
