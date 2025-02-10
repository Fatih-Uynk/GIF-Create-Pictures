# GIF Oluşturucu

Bu Python betiği, belirli bir klasörde bulunan JPEG resimlerini kullanarak bir GIF dosyası oluşturur.

## Nasıl Çalışır?

1. **Klasör Seçimi**: Kullanıcıdan GIF'in oluşturulacağı klasörün yolu istenir.
2. **Resimlerin Okunması**: Belirtilen klasördeki tüm JPEG resimleri okunur.
3. **GIF Oluşturma**: Okunan resimler birleştirilerek bir GIF dosyası oluşturulur.
4. **Kaydetme**: Oluşturulan GIF, aynı klasöre `download.gif` adıyla kaydedilir.

## Kod Açıklaması

- **`make_gif(frame_folder)`**: Bu fonksiyon, belirtilen klasördeki resimleri alır ve bir GIF oluşturur.
  - `glob.glob(f"{frame_folder}/*.jpg")`: Klasördeki tüm JPEG,PNG,JPG dosyalarını bulur.
  - `Image.open(image)`: Her bir resmi açar.
  - `frame_one.save(...)`: Resimleri birleştirerek GIF olarak kaydeder.

- **`if __name__ == "__main__":`**: Betik doğrudan çalıştırıldığında, kullanıcıdan klasör yolunu alır ve `make_gif` fonksiyonunu çağırır.

## Gereksinimler

- Python 3.x
- `Pillow` kütüphanesi (`pip install Pillow`)

## Kullanım

1. Betiği çalıştırın.
2. Klasör yolunu girin.
3. Oluşturulan GIF, belirtilen klasöre kaydedilecektir.

## Örnek

```bash
python make_gif.py
Lütfen GIF'in oluşturulacağı klasörün yolunu girin: /path/to/your/folder
