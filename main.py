import sender
import yfinance
import time

# Dictionary containing stock tickers and price targets
TRACKED_STOCKS = {"AAPL": 320, "MSFT": 167, "TSLA": 587}
# Replace with list of emails to be alerted of price changes
ALERTED_EMAILS = ["email1@email.com", "email2@email.com"]
# Replace with sender email username
SENDER_USERNAME = ""
# Replace with sender email password
SENDER_PASSWORD = ""

# Initialize sender email instance for sending alerts
sender_email = sender.Email(SENDER_USERNAME, SENDER_PASSWORD)

while True:

    for stock in TRACKED_STOCKS:
        # View price information for stock using yfinance API
        print("Viewing price info for " + stock + "...")
        yahoo_finance_stock = yfinance.Ticker(stock)
        price = yahoo_finance_stock.info["regularMarketPrice"]
        
        # Evaluate if the price is above the set threshold
        if price > TRACKED_STOCKS[stock]:
            
            # If the price is above threshold, send alert to every email in ALERTED_EMAILS
            print("ALERT!!!! " + stock + " price is $" + str(price) + ". Sending emails...")
            for email in ALERTED_EMAILS:
                sender_email.send_email(email, stock, "$" + str(price))
            
            # Then, increase the new price threshold by 5%
            TRACKED_STOCKS[stock] *= 1.05
            print("New price alert for " + stock + " is $" + str(TRACKED_STOCKS[stock]))
        
        else:
            # Otherwise print the current price
            print("Price under alert, $" + str(price))
    
    # After checking all stocks in the dictionary, sleep for 30 seconds.
    time.sleep(30)
