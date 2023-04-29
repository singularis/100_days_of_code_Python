import requests
import time



class Flights_manager:
    def __init__(self, url, header):
        self.header = header
        self.url = url

    def get_flights(self, city, date_from, date_to):
        params = {
            "fly_from": "city:KRK",
            "fly_to": city,
            "date_from": date_from, #"01/06/2023",
            "date_to": date_to,
            "return_from": date_to,
            "return_to": date_to,
            "nights_in_dst_from": "2",
            "nights_in_dst_to": "3",
            "max_fly_duration": "20",
            "flight_type": "round",
            "ret_from_diff_city": "true",
            "ret_to_diff_city": "true",
            "one_for_city": "0",
            "one_per_date": "0",
            "adults": "2",
            "children": "2",
            "selected_cabins": "C",
            "mix_with_cabins": "M",
            "adult_hold_bag": "1,0",
            "adult_hand_bag": "1,1",
            "child_hold_bag": "2,1",
            "child_hand_bag": "1,1",
            "only_working_days": "false",
            "only_weekends": "false",
            "partner_market": "us",
            "max_stopovers": "2",
            "max_sector_stopovers": "2",
            "vehicle_type": "aircraft",
            "limit": "10"
        }

        header = {
            "apikey": self.header,
            "accept": "application/json"
        }
        url = self.url +"v2/search"
        response = requests.get(url, params=params, headers=header)
        response.raise_for_status()
        data = response.json()["data"]
        if not data:
            return None
        lower_price = data[0]["conversion"]["EUR"]
        for flight in data:
            price = flight["conversion"]["EUR"]
            if price < lower_price:
                lower_price = price
        return lower_price

