import os
import glob
from PIL import Image


def make_gif(frame_folder):
    print(f"Kullanılan Dizin: {frame_folder}")  # Klasörü Yazdır
    print("Bulunan Dosyalar:", glob.glob(f"{frame_folder}/*"))  # Dosyaları Listele

    # Sadece PNG dosyalarını al (Gerekirse *.jpg veya *.jpeg olarak değiştir)
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.jpg")]
    if not frames:
        print("Hata: Klasörde uygun resim bulunamadı!")
        return

    # GIF'in nereye kaydedileceğini açıkça yazdıralım
    save_path = os.path.join(frame_folder, "download.gif")
    print(f"GIF şu dizine kaydedilecek: {save_path}")

    frame_one = frames[0]
    frame_one.save(save_path, "GIF", append_images=frames[1:], save_all=True, duration=500, loop=0)

    print("✅ GIF başarıyla oluşturuldu!")


if __name__ == "__main__":
    print("inside main")
    frame_folder = input(r"Lütfen GIF'in oluşturulacağı klasörün yolunu girin: ")
    make_gif(frame_folder)
