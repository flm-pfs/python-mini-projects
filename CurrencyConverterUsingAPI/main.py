import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "your_exchangeratesapi_api_key"  # Your API key for exchange rates API
# Base URL for exchange rates API
BASE_URL = "http://api.exchangeratesapi.io/v1/latest"


def get_exchange_rates():
    """
    Fetches the latest exchange rates from the API.
    Returns a dictionary containing the rates.
    """
    params = {
        'access_key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['rates']
    else:
        messagebox.showerror("Error", "Failed to fetch exchange rates.")
        return None


def convert_currency():
    """
    Converts the entered amount from one currency to another.
    Displays the converted amount in the result label.
    """
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

    rates = get_exchange_rates()
    if rates:
        if from_currency in rates and to_currency in rates:
            converted_amount = amount * \
                (rates[to_currency] / rates[from_currency])
            result_label.config(text=f"{amount} {from_currency} = {
                                converted_amount:.2f} {to_currency}")
        else:
            messagebox.showerror(
                "Error", "Selected currencies are not available.")


def main():
    """
    Main function that sets up the GUI and runs the application.
    """
    global amount_entry, from_currency_var, to_currency_var, result_label
    root = tk.Tk()
    root.title("Currency Converter")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    amount_label = tk.Label(frame, text="Amount:", font=('Arial', 14))
    amount_label.grid(row=0, column=0, padx=10)

    amount_entry = tk.Entry(frame, width=20, font=('Arial', 14))
    amount_entry.grid(row=0, column=1, padx=10)

    from_currency_var = tk.StringVar(root)
    from_currency_var.set("EUR")  # default value
    from_currency_menu = tk.OptionMenu(
        frame, from_currency_var, "EUR", "USD", "GBP", "JPY", "AUD", "CAD")
    from_currency_menu.config(font=('Arial', 14))
    from_currency_menu.grid(row=1, column=0, padx=10)

    to_currency_var = tk.StringVar(root)
    to_currency_var.set("USD")  # default value
    to_currency_menu = tk.OptionMenu(
        frame, to_currency_var, "EUR", "USD", "GBP", "JPY", "AUD", "CAD")
    to_currency_menu.config(font=('Arial', 14))
    to_currency_menu.grid(row=1, column=1, padx=10)

    convert_button = tk.Button(frame, text="Convert", font=(
        'Arial', 14), command=convert_currency)
    convert_button.grid(row=2, column=0, columnspan=2, pady=20)

    result_label = tk.Label(root, text="", font=('Arial', 14))
    result_label.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
