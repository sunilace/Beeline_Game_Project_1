# Author: Sunil gupta
# Date: 3/06/2024
# Description: Program to run the Beeline game with the help of BeeFunctions.py .

# Importing functions from BeeFunctions.py
import BeeFunctions as bee


def main():
    # Getting the flower Dictionary.
    flowers = bee.flower_list()
    try:

        # Loading the field.
        hidden_field = bee.field(flowers)
    except TypeError as e:

        # Printing the exception showing the flower label not available in the flower dictionary.
        print(e)
        exit(-1)

    # Creating a visible list based on the hidden list.
    visible_field = bee.copy_field(hidden_field)
    NEEDED_POLLEN = 20
    harvested_pollen = 0
    scouts = 5
    worker = 5

    # To print intro details.
    bee.intro(flowers, scouts, worker, NEEDED_POLLEN)

    # Loop to continue till either worker is 0 or harvested pollen is greater then 20.
    while (worker > 0) and (harvested_pollen < 20):
        print(f"\nYou have {scouts} scout bees left, {worker} worker bees left, and have "
              f"harvested {harvested_pollen} units of pollen.")
        print("H is the hive, U is a used flower")

        # Printing the visible field.
        bee.print_field(visible_field)

        # Getting if the bee is scout or a worker bee.
        st = input("What type of bee would you like to send out (S for scout or W for worker): ")
        st = st.upper()

        # If the bee is scout then this will execute.
        if st == 'S':
            if scouts < 1:

                # Showing message if no scout bees are left.
                print("You do not have any more scout bees!")
            else:

                # Getting coordinates to scout.
                print("Where would you like to send the bee")
                x = int(input(f"0 <= x < {len(visible_field[0])}: "))
                y = int(input(f"0 <= y < {len(visible_field)}: "))
                scouts -= 1
                print("Sending out the scout")

                # Checking the area around the given coordinates using check_area function.
                bee.check_area(hidden_field, visible_field, x, y, 'S', flowers)

        # If bee is a Worker bee then the following will get executed.
        elif st == 'W':
            if worker < 1:

                # Showing message if no worker bees are left.
                print("You do not have any more worker bees!")
            else:

                # Getting coordinates to scout.
                print("Where would you like to send the bee")
                x = int(input(f"0 <= x < {len(visible_field[0])}: "))
                y = int(input(f"0 <= y < {len(visible_field)}: "))
                worker -= 1
                print("Sending out the worker")

                # Checking the area around the given coordinates using check_area function.
                # If pollen harvested then adding it in the harvested pollen.
                harvested_pollen = harvested_pollen + bee.check_area(hidden_field, visible_field, x, y, 'W', flowers)
        else:

            # If anything other then S or W are entered then showing appropriate message.
            print("That is not a valid bee type!")

    # Showing message if enough pollen has been harvested.
    if harvested_pollen > 19:
        print(f"Good work! You made {harvested_pollen} honey for the hive. Just in time for winter!")

    # Showing message if worker are 0 and enough pollen was not harvested.
    elif worker == 0:
        print(f"Oh no! You have made only {harvested_pollen} honey which is not enough."
              f" You have been deposed as queen.")


main()
