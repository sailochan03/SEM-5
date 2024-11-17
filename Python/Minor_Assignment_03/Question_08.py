def days_in_month(month):
    month_days = {
        "january": "31",
        "february": "28/29", 
        "march": "31",
        "april": "30",
        "may": "31",
        "june": "30",
        "july": "31",
        "august": "31",
        "september": "30",
        "october": "31",
        "november": "30",
        "december": "31"
    }
    month = month.lower()
    return month_days.get(month, "Invalid month name")

month = input("Enter the name of the month: ")
print(f"Number of days in {month}: {days_in_month(month)} days")
