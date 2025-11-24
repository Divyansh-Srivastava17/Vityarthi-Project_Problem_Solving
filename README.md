# Simple Expense Splitter

This is a straightforward Python project designed to solve a common real-world problem: figuring out who owes money after a group event. Instead of doing complicated math manually, this tool calculates exactly who needs to pay whom to settle the bill.

## About The Project

We have all been in that situation where a group of friends goes on a trip or shares a dinner, and everyone pays for different things. One person buys the tickets, another pays for the food, and someone else covers the taxi. At the end, it is often confusing to figure out who paid more than their fair share and who paid less.

This program automates that entire process. It takes a list of people and their expenses, calculates the average cost per person, and produces a clear report showing the final settlement balances.

## Key Features

* **Flexible Group Sizes:** You are not limited to a specific number of people. You can add as many participants as you need (for example: Alice, Bob, Charlie, David).
* **Error Handling:** The program is built to handle mistakes gracefully. If you accidentally type text when the program is expecting a number for an expense, it will not crash. Instead, it will simply ask you to enter the amount again.
* **Unlimited Entries:** You can keep adding expenses one by one until you are finished recording everything.
* **Fair Calculation:** It uses precise floating-point math to ensure the total cost is split equally among all participants.

## How It Works

1.  **Group Setup:** The program starts by asking for the names of everyone involved in the group.
2.  **Recording:** It enters a loop where you record expenses. You simply state who paid and how much they paid.
3.  **Calculation:** Once you type "done," the system calculates the total expenses and divides it by the number of people to find the "fair share."
4.  **Results:** Finally, it displays a summary telling you the total cost, what the average cost was, and whether each person owes money or should receive a refund.

## How to Run

You do not need to install any external libraries to run this project. It works with standard Python.

1.  Download the expense_splitter.py file to your computer.
2.  Open your terminal or command prompt.
3.  Navigate to the folder where you saved the file.
4.  Run the following command:

python expense_splitter.py
