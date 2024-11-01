from notifier_botty import login_to_chegg, refresh_chegg, telegram_bot_sendtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta
import pytz
import requests
import multiprocessing


# Account credentials (you can add more accounts here)
accounts = [
    #{"username": "nageshoperation@gmail.com", "password": "Nagesh@143", "user_bot_chatID": '748228452', "account_name": "Anandkumar", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    #{"username": "nageshoperation@gmail.com", "password": "Nagesh@143", "user_bot_chatID": '748228452', "account_name": "Anandkumar", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    # Add more accounts if necessary
]


accept_option = True
start_time = 0  # Starting time. Default 0. In 24-hour format
end_time = 25  # Ending time. Default 25. In 24-hour format


def refresh_account(account):
    username = account["username"]
    password = account["password"]
    user_bot_chatID = account["user_bot_chatID"]
    account_name = account["account_name"]
    user_bot_token = account["user_bot_token"]  # Same token for all accounts

    # Set up Chrome WebDriver for this account
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Each account gets its own Chrome instance
    driver = webdriver.Chrome(options=options)

    # Attempt to log in
    flag_login = True
    while flag_login:
        flag_login = login_to_chegg(username, password, driver)


    # Start refreshing for the account
    refresh_chegg(driver, accept_option, start_time, end_time, user_bot_token, user_bot_chatID, account_name)  
    


if __name__ == "__main__":
    # Create a process for each account
    processes = []
    for account in accounts:
        process = multiprocessing.Process(target=refresh_account, args=(account,))
        processes.append(process)
        process.start()

    # Optionally join the processes to ensure the script waits for all to finish (though in infinite loops, this won't happen)
    for process in processes:
        process.join()
