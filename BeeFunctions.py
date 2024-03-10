# Author: Sunil gupta
# Date: 3/06/2024
# Description: Program to write all the functions that will support the Beeline.py file to run the Beeline game.

import os


def flower_list():
    '''
    :return: Dictionary containing flower letter as key and flower details as a tuple.
    '''

    # Dictionary to store flower details.
    flower = {}
    filename = input("Please enter the name of the file containing your flower to points mapping: ")

    # Looping till we get the available file name.
    while not os.path.exists(filename):
        filename = input(f"{filename} does not exist! Please enter "
                         f"the name of the file containing your flower to pollen mapping: ")

    # Opening the file.
    file = open(filename, 'r')
    for line in file:
        line = line.strip()
        line = line.split(",")

        # Storing in dictionary with key as flower letter and all flower details as a tuple to it.
        flower[line[0]] = tuple(line)
    file.close()

    # Returning the created Dictionary.
    return flower


def field(flower):
    '''
    :param flower: Dictionary containing the flower details.
    :type: Dictionary
    :return: 2 Dimensional list.
    '''

    # Creating a list to store the field.
    lis = []
    filename = input("Please enter the name of the file containing your field: ")

    # Looping till we get the available file name.
    while not os.path.exists(filename):
        filename = input(f"{filename} does not exist! Please enter the name of the file containing your field: ")
    file = open(filename, 'r')
    for line in file:

        # Splitting the line.
        k = line.split(",")

        # Getting the last element of the list which contains '\n' along with the last column value of the field.
        m = k[-1]

        # Taking the first character of the string. Leaving the '\n' part in the string.
        m = m[0]

        # Storing the last column value of field at the last position of the list.
        k[-1] = m

        # Loop to check if a unknown flower is present. If present then raise exception.
        for i in k:
            if i not in flower:
                if i not in ['H', 'P', ' ', '\n']:
                    raise TypeError(f"{i} is not a known flower type for this field!")

        # After checking, storing the field row details in the 2d list representing field.
        lis.append(k)
    file.close()

    # Returning 2D list representing the field.
    return lis


def copy_field(field_list):
    '''
    :param field_list: 2 Dimension list.
    :type: List
    :return: List
    '''

    # Creating new field to store the field.
    field_copy = []

    # Looping to create a field with same dimension as that of the passed one.
    for i in range(len(field_list)):
        m = []
        for j in range(len(field_list[0])):
            m.append(" ")
        field_copy.append(m)

    # Looping and storing the Hive at the correct location as that of
    # the passed field. Keep all other places as a space.
    for i in range(len(field_copy[0])):
        for j in range(len(field_copy)):
            if field_list[j][i] == 'H':
                field_copy[j][i] = 'H'
    return field_copy


def print_field(list):
    '''
    :param list: 2Dimension list
    :type: List
    '''

    l = len(list[0])

    # To check if the number of rows are greater then 10. If yes then the top row
    # will have 3 characters place to display each column number.
    if (l > 10):
        s = 3
    else:
        s = 1

    # Printing 3 spaces in the top row to align properly.
    print('   ', end='')

    # Printing the column numbers based on value of 's' using format function.
    for i in range(l):
        print(format(i, f'^{s}'), end=' ')
    print()

    # Printing each row after the first row as required.
    for i in range(len(list)):

        # To print the numbers on the left hand side of the grid for each row.
        print(format(i, '>2'), end='|')
        row = list[i]

        # Printing each value of the field based on the value of s.
        for j in row:
            print(format(j, f'^{s}'), end="|")
        print()


def intro(flowers, scout_bee, worker_bee, need_pollen):
    '''
    :param flowers: Dictionary containing flower details.
    :type: Dictionary
    :param scout_bee: Number of Scout bees.
    :type: Int
    :param worker_bee: Number of Worker bees.
    :type: Int
    :param need_pollen: Amount of the pollen needed.
    :type: Int
    '''

    # Printing the introduction message as per the output file.
    print('Welcome to Beeline!')
    print()
    print("You are the queen bee tasked with ensuring your hive produces enough honey.")
    print("Honey is created from pollen in flowers, which you will need to send bees out to find and harvest!")
    print("You have two kinds of bees: scout bees and worker bees.")
    print("Scout bees fly out to a location in the field and reveal 3x3 area around the specified location.")
    print(f"Worker bees fly out to a location, harvest flowers in a 3x3 area around the specified "
          f"location and also reveal the area they have harvested. ")
    print(f"However, you only have {scout_bee} scout bees and {worker_bee} worker"
          f"bees to obtain {need_pollen} units of pollen to produce enough honey.")
    print(f"Note, once a bee has been sent out it cannot be used again and a flower can only "
          f"be harvested once! Oh, and watch out for pitcher plants!")
    print("They'll trap your bees and prevent them from returning to the hive. Good luck!")
    print("The flowers contains the following units of pollen:")

    # Printing the flower details showing the flower letter, name and amount of pollen for it.
    for i in flowers:
        flow = flowers[i]
        print(f"{flow[0]}: {flow[1]}, {flow[2]} units of pollen")


def check_area(hidden_list, visible_list, x, y, st, flower):
    '''
    :param hidden_list: 2Dimension list containing the original field.
    :type: List
    :param visible_list: 2Dimension list containing the explored field.
    :type: List
    :param x: x coordinate.
    :type: Int
    :param y: y coordinate.
    :type: Int
    :param st: Representing a scout bee or a worker bee.
    :type: Int
    :param flower: Dictionary containing the flower details.
    :type: Dictionary
    :return: Harvested Pollen
    '''

    # Variable to keep track of the harvested pollen.
    pollen = 0

    # To check for the conditions in the which the bee may go out of bounds.
    if (x > (len(hidden_list[0])-1)) or (x < 0) or (y > (len(hidden_list)-1)) or (y < 0):
        print("Your bee has flown outside the field and gotten lost!")
        return pollen

    # Loop to check if the selected coordinate have any pitcher plant in 3x3 area.
    for i in range(x-1, x+2):

        # Continue the loop without doing anything in case the array goes out of
        # bound in case of coordinate near the edges of the grid.
        if (i > len(hidden_list[0])-1) or (i < 0):
            continue
        for j in range(y-1, y+2):

            # Continue the loop without doing anything in case the array goes out of
            # bound in case of coordinate near the edges of the grid.
            if (j > len(hidden_list)-1) or (j < 0):
                continue

            # Returning the pollen as 0 if the 3x3 area contains any pitcher plant.
            if hidden_list[j][i] == "P":
                print("Your bee must have fallen into a pitcher plant because it never returned!")
                return 0

    # This will execute if there are no pitcher plant in 3x3 area and sent bee is a Scout.
    if st == 'S':
        for i in range(x - 1, x + 2):

            # Continue the loop without doing anything in case the array goes out of
            # bound in case of coordinate near the edges of the grid.
            if (i > len(hidden_list[0]) - 1) or (i < 0):
                continue
            for j in range(y - 1, y + 2):

                # Continue the loop without doing anything in case the array goes out of
                # bound in case of coordinate near the edges of the grid.
                if (j > len(hidden_list) - 1) or (j < 0):
                    continue

                # Writing in the visible list based on the hidden list.
                if (hidden_list[j][i] in flower) or (hidden_list[j][i] == "U"):
                    visible_list[j][i] = hidden_list[j][i]

    # This will execute if the sent bee is a Worker.
    elif st == 'W':
        for i in range(x - 1, x + 2):

            # Continue the loop without doing anything in case the array goes out of
            # bound in case of coordinate near the edges of the grid.
            if (i > len(hidden_list[0]) - 1) or (i < 0):
                continue
            for j in range(y - 1, y + 2):

                # Continue the loop without doing anything in case the array goes out of
                # bound in case of coordinate near the edges of the grid.
                if (j > len(hidden_list) - 1) or (j < 0):
                    continue

                # If hidden list has U then writing in the Visible list.
                if hidden_list[j][i] == "U":
                    visible_list[j][i] = "U"

                # If there is any flower then write it as U in hidden and visible
                # list and increase pollen as per flower.
                if hidden_list[j][i] in flower:
                    tup = flower[hidden_list[j][i]]
                    pollen = pollen + int(tup[-1])
                    hidden_list[j][i] = "U"
                    visible_list[j][i] = "U"

    # Returning the added pollen value.
    return pollen
