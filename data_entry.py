from datetime import datetime

def get_date(prompt,allow_default=False): 
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime("%d-%m-%Y")
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return get_date(prompt, allow_default)
def get_description(prompt):
    pass


def get_amount(prompt):
    pass
def get_category(prompt, categories):
    pass

