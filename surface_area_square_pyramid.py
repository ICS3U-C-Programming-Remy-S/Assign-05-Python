#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Dec 11, 2023
# This program will ask for the base edge
# and height of a square based pyramid
# then it will calculate the surface area

import math


def calc_surface_area_pir(base_edge, height):
    # Calculate the surface area of the square pyramid
    calc_surface_area = base_edge**2 + base_edge * 2 * math.sqrt(
        base_edge**2 / 4 + height**2
    )
    return calc_surface_area


def main():
    # to continue to loop if user wants
    while True:
        # Nested loop to get valid input
        while True:
            # get decimal and places and display message to user
            print("This program will ask for the base edge")
            print("and height of a square based pyramid")
            print("then it will calculate the surface area")
            user_base_edge_str = input("Enter the base edge of the square pyramid: ")
            user_height_str = input("Enter the height of the square pyramid: ")

            # check if input is correct
            try:
                user_base_edge_float = float(user_base_edge_str)
                user_height_float = float(user_height_str)
                # Exit the loop if input is valid
                break
            except Exception:
                print(
                    f"{user_base_edge_str} and {user_height_str} are invalid base edge and height"
                )

        # call the function
        surface_area = calc_surface_area_pir(user_base_edge_float, user_height_float)

        # Display the surface area
        print(f"\nThe surface area of the square pyramid is: {surface_area:.2f}")

        # Ask if the user wants to continue
        user_input = input(
            "\nDo you want to calculate for another square based pyramid? (y/n): "
        )

        # Check if the user wants to exit the loop
        if user_input.lower() != "y":
            break


if __name__ == "__main__":
    main()
