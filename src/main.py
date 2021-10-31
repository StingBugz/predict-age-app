# Aplikasi untuk memperikirakan Umur
import datetime as dt

class UmurApp:
    def Main():
    # title
        today = dt.date.today()

        print(5*"="+"How Old are U?"+"="*5)
        print(f"Today is = {today:%A}, {today}")

    # birthday data
        print("Birthday Data")
        date = int(input("Date   : "))
        month = int(input("Month  : "))
        year = int(input("Year   : "))

    #formulas
        birthdate = dt.date(year,month,date)
        birthday = today - birthdate
        yearsold = birthday.days // 365
        birthmonth = (birthday.days % 365) // 30
        print(f"You are Birth at {birthdate:%A}, {birthdate}")
        print(f"Now you are "+str(yearsold)+" yo " + str(f"{birthmonth:.0f}") +" month")

        return 1
if UmurApp.Main() == 1 :
    ans = input("Another Birthday ?\n(y/n)").lower()
    
    if ans == "y":
        UmurApp.Main()
    elif ans == "n":
        exit()

if __name__ == "__main__":
    UmurApp.Main()