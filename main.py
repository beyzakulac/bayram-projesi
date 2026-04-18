import time
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import openrouteservice

client = openrouteservice.Client(key="eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjBlNTk1ZGQwMzM2ZDQzYjFhMjMyMmIyMDdiNDkzOTcwIiwiaCI6Im11cm11cjY0In0=")
#Geolocator oluştur
geolocator = Nominatim(user_agent="bayram_app")

# Konumum
my_location_address = "adresim"#kendi adresini yazabilirsin, örneğin: "Ankara, Çankaya" 
# Akraba listesi (isim ve adres)
relatives = [
    {"name": "Teyze", "address": ""},
    {"name": "Amca", "address": ""},
    {"name": "Hala", "address": "Ankara, Akşemsettin"},
    {"name": "Annane", "address": "Ankara, Boğaziçi"},
    {"name": "teyze rukiye", "address": "Ankara, Araplar"},
    {"name": "Amca mustafa", "address": "Ankara, Etimesgut"},
    {"name": "recep amca", "address": "Ankara, Eryaman"},
    {"name": "babane", "address": "Ankara, Akşemsettin"},
    {"name": "hasan", "address": "Ankara, Pursaklar"},   
 {"name": "hala metiye", "address": "İzmir, Çandarlı"}, 
 {"name": "amca mikail", "address": "Yozgat, Sorgun"},
]


def get_coords(address):
    try:
        location = geolocator.geocode(address)
        time.sleep(1) # Hata almamak için kısa bekleme
        return (location.latitude, location.longitude) if location else None
    except:
        return None

# Önce senin konumunun koordinatlarını alalım
my_coords = get_coords(my_location_address)
my_home = {"name": "EVİM (BAŞLANGIÇ)", "address": my_location_address, "coords": my_coords}

# Akrabaların koordinatlarını alalım
for r in relatives:
    r["coords"] = get_coords(r["address"])

# Mesafe fonksiyonu
def travel_time(a, b):
    try:
        coords = [(a[1], a[0]), (b[1], b[0])]  

        route = client.directions(
            coordinates=coords,
            profile='driving-car'
        )

        duration = route['routes'][0]['summary']['duration']
        return duration 

    except:
        return float('inf')

# komundan başlayan en yakın komşu algoritması
def nearest_neighbor_from_me(start_point, relatives):
    route = []
    remaining = [r for r in relatives if r["coords"] is not None]
    
    current = start_point
    route.append(current)

    while remaining:
    # Şu an bulunduğun noktaya en hızlı gidileni bul
    next_one = min(
        remaining,
        key=lambda x: travel_time(current["coords"], x["coords"])
    )

    route.append(next_one)
    remaining.remove(next_one)
    current = next_one  # yeni konum
    return route
time_sec = travel_time(current["coords"], next_one["coords"])
print(f"{current['name']} → {next_one['name']} : {time_sec/60:.1f} dk")

if my_coords:
    final_route = nearest_neighbor_from_me(my_home, relatives)
    
    print("\n Senin konumundan başlayan en verimli bayram rotası:\n")
    for i, r in enumerate(final_route):
        prefix = "🏠" if i == 0 else f"{i}."
        print(f"{prefix} {r['name']} -> {r['address']}")
else:
    print("Kendi konumun bulunamadığı için rota oluşturulamadı!")