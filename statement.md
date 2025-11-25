# Problem Statement

When groups of people travel together, share an apartment, or simply go out for dinner, managing shared finances becomes a significant challenge. One person might pay for the hotel, another for the groceries, and someone else for the taxi. At the end of the event, calculating exactly who owes money to whom is a tedious and error-prone process. Manual math often leads to confusion, awkwardness, and unfair settlements. There is a need for a simple, automated tool that can take these various expenses and calculate a mathematically fair distribution of costs.

## Scope of the Project

The scope of this project is to develop a Command Line Interface (CLI) application using Python. The system is designed to handle the core logic of expense splitting without the need for complex graphical interfaces or external databases.

The project encompasses:

Accepting a dynamic list of participant names.

Recording multiple, individual expense entries associated with specific users.

performing mathematical calculations to determine the total group spend and the "fair share" per person.

Generating a final text-based report that categorizes users as either "owing money" or "receiving money" to settle the balance.

Handling basic input errors (such as invalid numbers) to prevent program crashes.

## Target Users

This tool is intended for anyone who needs to manage shared costs, including:

Roommates: For splitting rent, utilities, and grocery bills.

Travelers: For groups of friends managing expenses during a vacation or road trip.

Students: For splitting costs of group projects or shared meals.

Event Organizers: For managing small-scale event budgets where multiple people contribute to the costs.

## High-Level Features

**Dynamic Group Management:** Allows the user to input any number of participants at the start of the session.

**Expense Logging:** detailed recording of expenses, linking a specific amount to a specific payer.

**Input Validation:** Robust error handling that detects if a user enters text instead of a number or tries to assign an expense to a person who is not in the group.

**Settlement Calculation:** An automated algorithm that sums all costs, divides them equally, and determines the net balance for each individual.

**Summary Report:** A clear, readable output displaying the total money spent and a breakdown of the final financial obligations for each member.
