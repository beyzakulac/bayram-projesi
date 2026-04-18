
# Bayram Rota Planlayıcı 

Bu proje, bayram ziyaretleri veya çoklu durak gerektiren seyahatler için en verimli rotayı hesaplayan bir Python betiğidir. Kullanıcının başlangıç konumunu baz alarak, girilen adresler (akrabalar/duraklar) arasındaki sürüş sürelerini hesaplar ve **En Yakın Komşu (Nearest Neighbor)** algoritmasını kullanarak zaman açısından en uygun rotayı oluşturur.

##  Özellikler

* **Otomatik Koordinat Çevirimi:** Geopy (Nominatim) kullanılarak girilen metin tabanlı adresler (Örn: "Ankara, Akşemsettin") enlem ve boylam koordinatlarına dönüştürülür.
* **Gerçek Zamanlı Mesafe Hesaplama:** OpenRouteService API kullanılarak iki nokta arasındaki kuş uçuşu mesafe değil, gerçek **sürüş süresi (driving-car)** baz alınır.
* **Akıllı Rota Optimizasyonu:** Başlangıç noktasından itibaren her adımda, bulunulan konuma zaman açısından en yakın olan bir sonraki durak seçilerek rota optimize edilir.

##  Kullanılan Teknolojiler

* **Python 3.x**
* **Geopy:** Açık kaynaklı Nominatim API'si ile adres-koordinat dönüşümü (Geocoding) için.
* **OpenRouteService:** Koordinatlar arası rota ve sürüş süresi (duration) hesaplamaları için.

##  Kurulum

Projenin çalışması için bilgisayarınızda Python yüklü olmalıdır. Gerekli kütüphaneleri kurmak için terminalinizde şu komutu çalıştırın:

```bash
pip install geopy openrouteservice
 Kullanım
API Anahtarı: Kodu çalıştırmadan önce openrouteservice.Client(key="...") kısmına kendi OpenRouteService API anahtarınızı girmelisiniz.

Başlangıç Konumu: Kod içerisindeki my_location_address değişkenine kendi başlangıç adresinizi yazın (Örn: "Ankara, Çankaya").

Duraklar (Akrabalar): Ziyaret edilecek kişileri ve adreslerini relatives listesine ekleyin.

Python
relatives = [
    {"name": "Hala", "address": "Ankara, Akşemsettin"},
    {"name": "Recep Amca", "address": "Ankara, Eryaman"}
]
Çalıştırma: Betiği çalıştırdığınızda terminalde adım adım en verimli rota listelenecektir.

⚠️ Önemli Notlar
Geopy İstek Sınırı: Nominatim ücretsiz bir servis olduğu için saniyede 1 istek limiti vardır. Kod içerisindeki time.sleep(1) bu limiti aşmamak ve banlanmamak için konulmuştur, lütfen kaldırmayın.

API Güvenliği: GitHub'a yükleme yaparken API anahtarınızın (key) kodun içinde açıkça görünmemesine dikkat edin. Güvenlik için .env dosyası veya ortam değişkenleri kullanılması tavsiye edilir
