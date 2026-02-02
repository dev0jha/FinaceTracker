# Finance Transaction Tracker

A Python-based personal finance management application that helps you track income and expenses, view transaction summaries, and visualize financial data over time.

## Features

- **Add Transactions**: Record income and expense transactions with date, amount, category, and description
- **View Transactions**: Filter and view transactions within a specific date range
- **Financial Summary**: Automatically calculates total income, total expenses, and net savings
- **Data Visualization**: Generate plots to visualize income and expenses over time
- **CSV Storage**: All transactions are stored in a CSV file for easy access and portability

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

### Menu Options

1. **Add a new transaction**: Enter details for a new income or expense transaction
   - Date (dd-mm-yyyy format or press Enter for today's date)
   - Amount (must be a positive number)
   - Category (I for Income, E for Expense)
   - Description (optional)

2. **View transactions and summary**: View all transactions within a date range
   - Enter start date (dd-mm-yyyy)
   - Enter end date (dd-mm-yyyy)
   - Optionally view a graphical plot of income vs expenses

3. **Exit**: Close the application

## File Structure

- `main.py`: Main application file with CSV handling and plotting functionality
- `data_entry.py`: User input validation and data entry functions
- `finance_data.csv`: CSV file storing all transaction data
- `requirements.txt`: Python package dependencies

## Data Format

Transactions are stored in CSV format with the following columns:

- **date**: Transaction date (dd-mm-yyyy)
- **amount**: Transaction amount (numeric)
- **category**: Income or Expense
- **description**: Optional description of the transaction

## Requirements

- Python 3.6+
- pandas
- matplotlib

## Example

```
1. Add a new transaction
2. View transactions and summary within a date range
3. Exit
Enter your choice (1-3): 1
Enter the date of the transaction (dd-mm-yyyy) or enter for today's date:
Enter the amount: 1000
Enter the category ('I' for Income or 'E' for Expense): I
Enter a description (optional): Monthly salary
Entry added successfully
```

## License

This project is open source and available for personal use.
