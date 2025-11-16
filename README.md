# Bilgisayarla Görü Ödevi 3: Nokta İşlemleri ve Histogram

Bu proje, "Bilgisayarla Görü" dersinin 3. ödevi kapsamında hazırlanmıştır. Proje, Python kullanarak temel görüntü işleme tekniklerini uygular.

Uygulanan teknikler şunlardır:
* **Soru 1:** Parlaklık, Kontrast, Negatif Alma ve Eşikleme gibi temel nokta işlemleri.
* **Soru 2:** Görüntünün histogramının manuel olarak (sıfırdan) hesaplanması ve istatistiklerinin (Ortalama, Standart Sapma, Entropi) çıkarılması.
* **Soru 3:** Manuel Kontrast Germe (Contrast Stretching) implementasyonu.
* **Soru 4:** Manuel Histogram Eşitleme (Histogram Equalization) implementasyonu.
* **Soru 5:** Gamma Düzeltmesi uygulaması ve analizi.

Proje, `cv2.calcHist()` veya `cv2.equalizeHist()` gibi hazır fonksiyonları kullanmadan, ödev gereksinimlerine uygun olarak NumPy kütüphanesi ile "sıfırdan implemente" edilmiştir.

## Gereksinimler

Projenin çalıştırılması için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

```bash
pip install numpy matplotlib opencv-python pillow