prices = {
    "van_tor_price": 250,
    "van_ott_price": 280,
    "van_mon_price": 240,
    "van_edm_price": 150,
    "van_cal_price": 180,
    "ott_ber_price": 1350,
    "mon_lon_price": 1300,
    "edm_lon_price": 1290,
    "cal_lon_price": 1400,
    "tor_mun_price": 990,
}

times = {
    "van_tor_travel_time": 3.5,
    "van_ott_travel_time": 4,
    "van_mon_travel_time": 4,
    "van_edm_travel_time": 1.5,
    "van_cal_travel_time": 1,
    "ott_layover": 3.5,
    "mon_layover": 2,
    "edm_layover": 5,
    "cal_layover": 2.5,
    "tor_layover": 1.5,
    "ott_ber_travel_time": 9,
    "mon_lon_travel_time": 8,
    "edm_lon_travel_time": 10,
    "cal_lon_travel_time": 10,
    "tor_mun_travel_time": 9.5,
}

print("Hi! I'm in Lighthouse1.py")


def calculate_value(prices: list, times: list):
    return sum(prices) + sum(times)


def print_values(city2, city3):
    flight_prices = [prices[f"van_{city2}_price"], prices[f"{city2}_{city3}_price"]]
    travel_times = [
        times[f"van_{city2}_travel_time"],
        times[f"{city2}_{city3}_travel_time"],
        times[f"{city2}_layover"],
    ]
    print(f"VAN -> {city2.upper()} -> {city3.upper()}: {calculate_value(prices=flight_prices, times=travel_times)}")


print(f"File name: {__name__}")


if __name__ == "__main__":
    print("I'm the main file")
    print_values("mon", "lon")
    print_values("tor", "mun")
    print_values("edm", "lon")
    print_values("ott", "ber")
