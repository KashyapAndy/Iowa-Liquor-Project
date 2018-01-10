#Trying to understand profits/bottle across the state. Practice information

profit_bottle = liq_data[["Category Name", "Bottles Sold", "Profit_Dollars"]].groupby("Category Name", as_index = False).sum()
profit_bottle["Profit_Bottle"] = profit_bottle["Profit_Dollars"]/profit_bottle["Bottles Sold"]

profit_bottle = profit_bottle.sort_values("Bottles Sold", ascending=False)
profit_bottle.head(5)

# Trying to understand the sales by year/month/date for 2015 & 2016

sales_year = liq_data[liq_data["Year"] == 2015].groupby(["Year", "CityName", "County Number", "Zip Code", "Store Number", "Category Name", "Bottle Cost_Dollars", "CountyName"], as_index = False)["Sale_Dollars", "Profit_Dollars", "Bottles Sold"].sum().sort_values(["CityName"])

#Trying to understand a specific Category search!

sales_year[(sales_year["Category Name"]=="VODKA 80 PROOF") & (sales_year["CityName"]=="SUMNER")]

