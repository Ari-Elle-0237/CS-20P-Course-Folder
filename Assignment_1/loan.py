#! /usr/bin/python3
"""
Assignment #1: Loan Payment Calculator
loan.py
by Ariel Zepezauer (arielzepezauer@gmail.com
Pengo: 'azepezau'
Test Cases in loan_unittest.py
Repository at: https://github.com/Ari-Elle-0237/CS-20P-Course-Folder.git
"""

def main():
    print(f"Aríel Zepezauer, arielzepezauer@gmail.com\n"
          f"Due: Thu Sep 5, 2024 7:00pm, "
          f"Assignment #1: Program One (Loan Payment Calculator)\n"
          f"Exit Code: 0, Passes all test cases (see loan_unittest.py)")
    payment = calculate_payment(*prompt_user())
    print(f"each payment:${payment:0.2f}")


def calculate_payment(principal, annual_interest, annual_payments, years):
    r"""
    Function to calculate an individual loan payment from the given params
    Using the following formula (Written in LaTeX):
    payment = principal \: \div \: \frac{1-(1+interest)^{-numPayments}}{interest}
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
    print(f"Input Amount to be Borrowed (Input as a number, ie: for $10 input 10):")
    principal = float(input())
    print(f"Input Annual Interest Rate (Input as a number, ie: for 10% input 0.1):")
    annual_interest = float(input())
    print(f"Input Number of Payments per year:")
    annual_payments = float(input())
    print(f"Input Number of Years for loan to be paid:")
    years = float(input())
    return principal, annual_interest, annual_payments, years


if __name__ == "__main__":
    main()
