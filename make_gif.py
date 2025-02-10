import os  # Dosya ve dizin işlemleri için kullanılır(Dosya yolu oluşturmak için vb.)
import glob  # Klasörde ki JPG uzantılı dosyaları bulmak için kullanılıyor
from PIL import \
    Image  # Görüntü işlemek için kullanılan bir kütüphane, burada Image modülü kullanılarak resimler açılıyor ve GIF olarak kayıt ediliyor


# Bu fonksiyon belirttiğimiz klasörde ki JPG dosyalarından bir GIF oluşturur
def make_gif(frame_folder):
    print(f"Kullanılan Dizin: {frame_folder}")  # Klasörü Yazdır
    print("Bulunan Dosyalar:", glob.glob(f"{frame_folder}/*"))  # Dosyaları Listele

    # Sadece PNG dosyalarını al (Gerekirse *.jpg veya *.jpeg olarak değiştir)
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.jpg")]
    # glob.glob(f"{frame_folder}/*.jpg"): Klasördeki .jpg uzantılı dosyaları listeler.
    # [Image.open(image) for image in ...]: Bulunan tüm .jpg dosyaları açılır ve frames listesine eklenir.

    # eğer klasörde hiç .jpg uzantılı dosya yoksa, frames listesi boş kalır.
    if not frames:
        print("Hata: Klasörde uygun resim bulunamadı!")
        return

    # GIF'in nereye kaydedileceğini açıkça yazdıralım
    save_path = os.path.join(frame_folder, "download.gif")  # ifadesi, GIF'in kaydedileceği tam yolu oluşturur.
    print(f"GIF şu dizine kaydedilecek: {save_path}")

    frame_one = frames[0]  # İlk resmi alır.

    # frame_one.save İlk resmi kullanarak yeni bir GIF dosyası oluşturur
    # save_path: GIF'in kaydedileceği dosya yolu.
    # "GIF": Dosya formatı olarak GIF kullanılır.
    # append_images=frames[1:]: İlk resim dışındaki diğer resimler GIF'e eklenir.
    # duration ile her karenin 0,5 saniye ekranda kalmasını sağlar
    # loop ile GIF İN sonsuz döngüde oynatılması sağlanır
    frame_one.save(save_path, "GIF", append_images=frames[1:], save_all=True, duration=500, loop=0)

    print("✅ GIF başarıyla oluşturuldu!")


if __name__ == "__main__":
    print("inside main")
    frame_folder = input(r"Lütfen GIF'in oluşturulacağı klasörün yolunu girin: ")
    make_gif(frame_folder)
