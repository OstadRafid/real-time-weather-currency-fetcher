import json
import os

print("<================== Data Fetcher ==================>".center(110))

while True:
    print("\n1. Current Weather")
    print("2. Currency Exchange Rate")
    print("3. Save Result to JSON File")
    print("4. View Previous Saved Data")
    print("5. Exit")

    try:
        Choice = int(input("Enter Your Choice -> "))

        match Choice:
            case 1:
                from data_fetcher import Weather
                Weather()

            case 2:
                from currency_fetcher import Currency_Exchange
                Currency_Exchange()

            case 3:
                if os.path.exists("data.json"):
                    with open("data.json", "r") as File:
                        try:
                            Saved_Data = json.load(File)
                        except json.JSONDecodeError:
                            Saved_Data = []

                    if not isinstance(Saved_Data, list):
                        Saved_Data = []

                    with open("data.json", "w") as File:
                        json.dump(Saved_Data, File, indent=4)

                    print("Result saved successfully in data.json!")

                else:
                    print("No saved data found. Fetch weather or exchange currency first.")

            case 4:
                if os.path.exists("data.json"):
                    with open("data.json", "r") as File:
                        try:
                            Saved_Data = json.load(File)
                        except json.JSONDecodeError:
                            Saved_Data = []

                    if Saved_Data:
                        print("\n<================== Previous Saved Data ==================>\n")
                        print(json.dumps(Saved_Data, indent=4))
                    else:
                        print("No previous data available.")

                else:
                    print("data.json file not found.")

            case 5:
                print("Thank you for using Data Fetcher!")
                break

            case _:
                print("Invalid choice! Please select 1 to 5.")

    except ValueError:
        print("Please enter a valid number.")

"""
Developed By Md.Rafid Al Mahmud
Department of Software Engineering
Daffodil International Univarsity
"""