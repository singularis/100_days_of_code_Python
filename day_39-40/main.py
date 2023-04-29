import secret
import data_manager
import flight_data
import flight_search
import notification_manager
import datetime

time_now = datetime.datetime.now()
future_date = time_now + datetime.timedelta(days=30*6)
sheet = data_manager.DataManager(url=secret.sheety_endpoint, header=secret.sheety_bearer)
iata = flight_data.IATAmanager(url=secret.tequila_uri, header=secret.tequila_api_key)
flights = flight_search.Flights_manager(url=secret.tequila_uri, header=secret.tequila_api_key)
dante = notification_manager.NotificationManager(email=secret.email, password=secret.password)
sheet_payload = sheet.get_data()
new_user = data_manager.NewUser()
sheet.put_user(new_user.get_user())
users = sheet.get_users()
# Initial data check for new locations
for row in sheet_payload:
    iata = row["iataCode"]
    city = row["city"]
    if iata == '':
        iata_code = iata.get_codes(city)
        iata = iata_code
        sheet.put_iata(iata_code["code"], row["id"])
    lowest_price = flights.get_flights(iata, time_now.strftime('%d/%m/%Y'), future_date.strftime('%d/%m/%Y'))
    if lowest_price:
        if lowest_price < int(row["lowestPrice"]):
            sheet.put_price(lowest_price, row["id"])
            for user in users:
                print(user)
                dante.send_notification(receiver=user["email"], city=city, price=lowest_price)