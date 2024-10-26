import yfinance as yf

def get_stock_price(ticker_symbol):
    """
    Fetches the current stock price for the given ticker symbol.
    
    :param ticker_symbol: str, the stock ticker symbol (e.g., 'AAPL' for Apple)
    :return: float, the current stock price
    """
    stock = yf.Ticker(ticker_symbol)
    try:
        # Get the latest available stock price
        stock_price = stock.history(period="1d")['Close'][0]
        return stock_price
    except IndexError:
        print(f"Could not fetch data for {ticker_symbol}. Please check the ticker symbol.")
        return None

if __name__ == "__main__":
    # Example usage
    ticker_symbol = input("Enter the stock ticker symbol: ").upper()
    stock_price = get_stock_price(ticker_symbol)
    if stock_price is not None:
        print(f"The current stock price for {ticker_symbol} is ${stock_price:.2f}")