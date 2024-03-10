# Author: Sunil gupta
# Date: 3/06/2024
# Description: Program to create a field based on the given input and store it in a csv file.

import os
import random
import csv


# Function to generate random x and y co-ordinates.
def coordinate_generator(rows, cols):
    '''
    :param rows: Representing the Rows in the field.
    :type: Int
    :param cols: Representing the Columns in the field
    type: Int
    :return: Generated x and y coordinate.
    '''
    no1 = random.randint(0, rows - 1)
    no2 = random.randint(0, cols - 1)
    return no1, no2


# Function to get all the flower code and return a list containing these code to add it in field.
def flower_list(filename):
    '''
    :param filename: Name of the file that contains the flower details.
    :type: String
    :return: List containing the letters of all the flower type.
    '''
    flower = []
    file = open(filename, 'r')
    for line in file:
        line = line.strip()
        line = line.split(",")
        flower.append(line[0])
    file.close()
    return flower


def main():
    file_name = input("Enter what the name of the file should be:")
    file_name = file_name + '.csv'

    # To check if a file with same name already exists. If exists then ask again for file name.
    while os.path.exists(file_name):
        file_name = input(f"{file_name} already exists. Enter what the name of the file should be:")
        file_name = file_name + '.csv'

    # Enter the dimension to make corresponding rows and columns of the field.
    print("Enter the dimensions of the field:")
    rows = int(input("Rows = "))
    cols = int(input("Columns = "))

    # To enter the number of the flowers to be in the field.
    flower_no = int(input("Enter the number of the flowers to be in the field: "))

    # To enter the number of pitcher plants to be in the field.
    pitcher_no = int(input("Enter the number of the pitcher plants to be in the field: "))

    # Getting the file name of the flower details file.
    flow_file = input("Please enter the name of the file containing your flower to points mapping: ")
    while not os.path.exists(flow_file):
        flow_file = input(f"{flow_file} does not exists. Please enter the name of "
                          f"the file containing your flower to points mapping: ")

    # Printing the message if the number of Flowers and Pitcher plants
    # along with hive is greater then the overall dimension of the field.
    if (flower_no + pitcher_no + 1) > (rows * cols):
        print("The entered number of the flower and pitcher plant along with a hive cannot "
              "exists in a field of the entered dimension.")
        exit(-1)
    else:
        field = []

        # Creating 2 dimension field based on received rows and columns number.
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(' ')
            field.append(row)

        # Generating random co-ordinates.
        x, y = coordinate_generator(rows, cols)

        # Placing the Hive.
        field[x][y] = "H"

        # Getting the letter of the flower in the given flower details file.
        flower = flower_list(flow_file)

        # Adding flowers in the field with random co-ordinates.
        for i in range(flower_no):
            x, y = coordinate_generator(rows, cols)
            random_flower = random.choice(flower)
            while field[x][y] != " ":
                x, y = coordinate_generator(rows, cols)
            field[x][y] = random_flower

        # Adding pitcher plants in the field with random co-ordinates.
        for i in range(pitcher_no):
            x, y = coordinate_generator(rows, cols)
            while field[x][y] != " ":
                x, y = coordinate_generator(rows, cols)
            field[x][y] = "P"

        # Creating a csv file with given name and write the field values in the csv file.
        with open(file_name, 'x', newline='') as csv_file:
            csv_write = csv.writer(csv_file)
            csv_write.writerows(field)

        print(f"Field created in the file with name {file_name}")


main()
