import requests
import geojson

api_key = open('apikeys.txt', 'r')
api_key = api_key.read()
api_key = api_key.split(",")

def api_get_waypoints(lat_1, long_1, lat_2, long_2):
    to_api = (str(lat_1) + "," + str(long_1) + "&end=" + str(lat_2) + "," + str(long_2))
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    call = requests.get(
        "https://api.openrouteservice.org/v2/directions/foot-walking?api_key=" + str(api_key[0]) + '&start=' + str(
            to_api), headers=headers)

    # print(call.status_code, call.reason)

    gj = geojson.loads(call.text)

    for feature in gj['features']:
        # print(feature['geometry']['coordinates'])
        l = feature['geometry']['coordinates']
    return l

def api_holidays():

    holidays = []
    date_to_api = datetime.datetime.today()

    for i in range(2):
        day = date_to_api.day + i
        month = date_to_api.month
        year = date_to_api.year

        response = requests.get(
            "https://holidays.abstractapi.com/v1/?api_key=" + str(api_key[1]) + "&country=PL&year=" + str(
                year) + "&month=" + str(month) + "&day=" + str(day))

        time.sleep(2)
        # print(response.status_code)
        # print(response.content)

        if len(response.content) == 2:
            holidays.append("false")
        else:
            holidays.append("true")



