import niquests
from datetime import datetime
import json

def Currency_Exchange():
    print()
    print("<=============== Currency Exchange Rate ===============>".center(110))

    Base_Currency = input("From Currency -> ").upper()
    Target_Currency = input("To Currency -> ").upper()
    Amount = float(input("Enter Amount -> "))

    URL = f"https://open.er-api.com/v6/latest/{Base_Currency}"

    Response = niquests.get(URL)
    Data = Response.json()

    if Data["result"] == "success" and Target_Currency in Data["rates"]:
        Rate = Data["rates"][Target_Currency]
        Result = Amount * Rate

        print("\n<==================== Currency Report ====================>\n")
        print("Exchange Rate ->", Rate)
        print("Converted Amount ->", round(Result, 2), Target_Currency)
        print("Date & Time ->", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("\n===========================================================")

        Result_Data = {
            "type": "currency",
            "base": Base_Currency,
            "target": Target_Currency,
            "amount": Amount,
            "rate": Rate,
            "converted_amount": round(Result, 2),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        try:
            with open("data.json", "r") as File:
                Saved_Data = json.load(File)
        except (FileNotFoundError, json.JSONDecodeError):
            Saved_Data = []

        if not isinstance(Saved_Data, list):
            Saved_Data = []

        Saved_Data.append(Result_Data)

        with open("data.json", "w") as File:
            json.dump(Saved_Data, File, indent=4)

        print("Data saved successfully!")

    else:
        print("Invalid Currency.\n")

Currency_Exchange()