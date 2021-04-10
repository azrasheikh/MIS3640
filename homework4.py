# """
# Application shell for menu driven app
# """
# import sys
# import pandas_datareader as pdr
# from time import time, sleep


# def display_menu():
#     print(
#         """
#     StockTracker Menu
#     1. Track Watchlist
#     2. Add Watchlist 
#     3. Delete Watchlistpi
#     4. Edit Watchlist
#     5. Exit   
#         """
#     )

# def track(watchlist):
#     start_time = time()
#     while True:
#         print(pdr.get_quote_yahoo(watchlist)['price'])
#         elapsed = time() - start_time
#         if elapsed >= 10:
#             prompt = input("Would you like to continue? y/n: ")
#             if prompt == 'n':
#                 break
#             start_time = time()
#             elapsed = 0
#         sleep(1)

# def add_list():
#     symbols = []
#     symbol = input("Enter a stock symbol: ")
#     while symbol != '':
#         if symbol not in symbols:
#             symbols.append(symbol.upper())
#         symbol = input("Enter a stock symbol: ")    
#     return sorted(symbols)

# def edit_list():
#     pass

# def delete_list():
#     pass            


# #actions = {'1' : track, '2' : add_list, '3' : delete_list, '4' : edit_list}

# def main():
#     while True:
#         display_menu()
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             track(watchlist)
#         elif choice == '2':
#             watchlist = add_list()   
#         elif choice == '5':
#             print("Thank you for using stonktracker!")
#             sys.exit(0)
#         else:
#             print("Please make a valid choice")        



# if __name__ == "__main__":
#     main()




import os

#Lookup os directory for watchlist, If none exist create one :)
def getWatchListsFromDirectory():

    #Looks for watchlist directory, makes one if not exist
    if not os.path.exists('./watchlists'):
        os.makedirs('./watchlists')
    
    #For each file in watchlist, check if it is a file, and then add to watchlist without the file extension
    return [f.split(".")[0] for f in os.listdir('./watchlists') if os.path.isfile('./watchlists/' + f)]
    

#Render menu, present user with the list of saved watchlists. If none exist, prompt user to add list and kick back to menu  :(

#Delete a list. User can select from the list which to delete. If none exist, kick back to menu :/

#Edit a list. User can select from the list which to update/edit. If none exist, kick back to menu :P


def main():
    print(getWatchListsFromDirectory())

if __name__ == "__main__":
    main()
