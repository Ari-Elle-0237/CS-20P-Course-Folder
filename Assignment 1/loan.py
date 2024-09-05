#! /usr/bin/python3
"""
Assignment #1: Loan Payment Calculator
loan.py
by Ariel Zepezauer
"""


def main():
    print(f"Aríel Zepezauer, arielzepezauer@gmail.com\n"
          f"Due: Thu Sep 5, 2024 7:00pm, "
          f"Assignment #1: Program One (Loan Payment Calculator)")
    payment = calculate_payment(*prompt_user())
    print(f"{payment:0.2f}")


def calculate_payment(principal, annual_interest, years, annual_payments):
    """
    Function to calculate an individual loan payment from the given params
    """
    num_payments = years * annual_payments
    interest = annual_interest / annual_payments
    return principal / ((1 - (1 + interest) ** (-num_payments)) / interest)


def prompt_user():
    """
    Prompt the user for the amount to be borrowed, the annual interest rate,
    the number of payments to be made each year, and the number of years the money
    is to be borrowed (in that order, one per line).
    """
    print(f"Input Amount to be Borrowed:")
    principal = float(input())
    print(f"Input Annual Interest Rate:")
    annual_interest = float(input())
    print(f"Input Number of Years for loan to be paid:")
    years = float(input())
    print(f"Input Number of Payments per year:")
    annual_payments = float(input())
    return principal, annual_interest, years, annual_payments


if __name__ == "__main__":
    main()
