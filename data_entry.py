from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {'I':"Income", 'E':"Expense"}


def get_date(prompt,allow_default=False): 
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        date_obj = datetime.strptime(date_str, date_format)
        return date_obj.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return get_date(prompt, allow_default)

def get_description(prompt):
    return input ("Enter description: (optional)")


def get_amount(prompt):
    try:
        amount_str = float(input(prompt))
        if amount_str <= 0:
            raise ValueError("Amount must be positive.")
        return amount_str
    except ValueError as e:
        print(e)
        return get_amount()


def get_category(prompt, categories):
    category = input("Enter the category('I' for income or 'E' for expense): ").strip().upper()
    if category in categories:
        return categories[category]
    else:
        print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
        return get_category(prompt, categories)
    


