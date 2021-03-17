# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:03:47 2021

@author: azrasheikh
"""

#imports
import csv 
import math
import matplotlib.pyplot as plt
import time
#data structures for each column
price = []
open_price = []
high = []
low = []
change_per = []
switch = {'O': open_price, 'P': price, 'L': low, 'H': high, 'C': change_per}
#functions
def mean(column):
    sum = math.fsum(column)
    return sum/len(column)

def std(column):
    n = len(column)
    mu = mean(column)
    #calculate average variance
    square_variance = sum([(x - mu) ** 2 for x in column])/(n-1)
    return math.sqrt(square_variance)

def percentile(column, percentileVal):
    column.sort()
    return column[round(percentileVal * (len(column) - 1))]

def descriptive_stats(column):
    print('Descriptive Statistics for Variable')
    print(40*'-')
    print(f"{'Count:':<15} {len(column):>10,.2f}")
    print(f"{'Mean:':<15} {mean(column):>10,.2f}")
    print(f"{'std:':<15} {std(column):>10,.2f}")
    print(f"{'min:':<15} {min(column):>10,.2f}")
    print(f"{'25%:':<15} {percentile(column, .25):>10,.2f}")
    print(f"{'50%:':<15} {percentile(column, .50):>10,.2f}")
    print(f"{'75%:':<15} {percentile(column, .75):>10,.2f}")
    print(f"{'max:':<15} {max(column):>10,.2f}")

def generate_plot(column):
    plt.plot(column)
    plt.show()
    return True

def generate_histogram(column):
    plt.hist(column, bins = 20)
    plt.show()
    return True

def display_menu():
    print(
        """
        Get Descriptive Statistics For:
        (O)pen Price
        (P)rice
        (L)ow
        (H)igh
        (C)hange Percentage
        """
        )

def requested_column(val):
    switch = {'O': open_price, 'P': price, 'L': low, 'H': high, 'C': change_per}

    return switch.get(val.upper(), None)

def display_chart_menu():
    print(
        """
        Get Chart For:
        (O)pen Price
        (P)rice
        (L)ow
        (H)igh
        (C)hange Percentage
        """
        )



#File input 
file_input = str(input("Please enter file name: "))

#prompt user for valid csv file
while ".csv" not in file_input:
    print("File not found! PLease try again")
    file_input = str(input("Please enter file name: "))

#open csv file as read only
file = open(file_input, 'r')

#creating reader object which contains row lists
reader = csv.reader(file)

#skip header
next(reader, None)

#iterate over reader object and do something with row list data
for row in reader:
    price.append(round(float(row[1]), 2))
    open_price.append(round(float(row[2]), 2))
    high.append(round(float(row[3]), 2))
    low.append(round(float(row[4]), 2))
    change_per.append(round(float(row[6].strip('%')), 2))


program_continue = False
while not program_continue: 
    #Display menu
    display_menu()

    #Ask user for menu option
    menu_option = str(input("Which column would you like to select? "))

    #dictionary will return data structure if valid option, None returns if invalid. If invalid reprompt user
    while not requested_column(menu_option): 
        print("Not valid option")
        menu_option = str(input("Which column would you like to select? "))

    #use dictionary to print out stats for requested column
    descriptive_stats(requested_column(menu_option))

    #Ask user to display another column or view graph
    prompt = str(input("Would you like to select another column? (Y/N) ")).upper()

    #handle invlaid response
    while True: 
        if prompt == 'N':
             program_continue = True
             break
        elif prompt == 'Y':
             break
        else: 
            print("Not valid Option")
            prompt = str(input("Would you like to select another column or continue? (Y/N) ")).upper()

# plot requested chart

#Display menu
display_chart_menu()

#Ask user for menu option
menu_option = str(input("Which chart would you like to select? "))


#dictionary will return data structure if valid option, None returns if invalid. If invalid reprompt user
while not requested_column(menu_option): 
    print("Not valid option")
    menu_option = str(input("Which chart would you like to select? "))
   
#Output first plot and then wait a few seconds before ploting histogram
generate_plot(requested_column(menu_option))
time.sleep(2)


generate_histogram(change_per)

