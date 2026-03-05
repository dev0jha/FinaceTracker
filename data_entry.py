from datetime import datetime
import os
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich.panel import Panel
from rich.columns import Columns

DATE_FORMAT = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

console = Console()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def colored_input(prompt):
    """Styled input prompt using rich."""
    return Prompt.ask(f"  [bold cyan]>[/bold cyan] {prompt}")


def success(msg):
    console.print(f"  [bold green]✓ {msg}[/bold green]")


def error(msg):
    console.print(f"  [bold red]✗ {msg}[/bold red]")


def warn(msg):
    console.print(f"  [bold yellow]⚠ {msg}[/bold yellow]")


def info(msg):
    console.print(f"  [cyan]ℹ {msg}[/cyan]")


def get_date(prompt, allow_default=False):
    date_str = colored_input(prompt)
    if allow_default and not date_str:
        today = datetime.today().strftime(DATE_FORMAT)
        info(f"Using today's date: [bold]{today}[/bold]")
        return today

    try:
        valid_date = datetime.strptime(date_str, DATE_FORMAT)
        return valid_date.strftime(DATE_FORMAT)
    except ValueError:
        error("Invalid date format. Please use dd-mm-yyyy")
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(colored_input("Amount: $"))
        if amount <= 0:
            raise ValueError("Amount must be a positive value.")
        return amount
    except ValueError as e:
        error(str(e))
        return get_amount()


def get_category():
    console.print()
    cat_panel = Panel(
        "[green][bold]I[/bold] → Income[/green]    [red][bold]E[/bold] → Expense[/red]",
        title="[dim]Categories[/dim]",
        border_style="dim",
        padding=(0, 2),
    )
    console.print(cat_panel)
    category = colored_input("Category").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    error("Invalid choice. Enter 'I' or 'E'.")
    return get_category()


def get_description():
    return colored_input("Description (optional)")