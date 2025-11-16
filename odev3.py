"""
Bilgisayarla Görü Ödevi 3: Nokta İşlemleri ve Histogram İşleme
NumPy kullanilarak yazilmiştir.
Hazir cv2 fonksiyonlari (calcHist, equalizeHist) kullanilmamiştir.
*** çiktiler pencere yerine dosyaya kaydedilmiştir. ***
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

print("Kütüphaneler yüklendi. İşlemler başliyor...")

#################################################
# YARDIMCI FONKSİYONLAR
#################################################

def gorsel_goster(baslik, goruntu, cmap='gray'):
    plt.figure()
    plt.title(baslik)
    plt.imshow(goruntu, cmap=cmap)
    plt.axis('off')
    print(f"-> '{baslik}' gösterim için hazirlaniyor...")

def histogram_ciz(baslik, hist):
    plt.figure()
    plt.title(baslik)
    plt.xlabel("Piksel Değeri (0-255)")
    plt.ylabel("Piksel Sayisi")
    plt.bar(range(256), hist, width=1.0, color='b')
    plt.xlim([0, 255])
    print(f"-> '{baslik}' çizim için hazirlaniyor...")

#################################################
# SORU 1: TEMEL NOKTA İŞLEMLERİ
#################################################

def parlaklik_ayarla(goruntu, c):
    yeni_goruntu = np.clip(goruntu.astype(np.int16) + c, 0, 255)
    return yeni_goruntu.astype(np.uint8)

def kontrast_ayarla(goruntu, factor):
    yeni_goruntu = factor * (goruntu.astype(np.float32) - 128) + 128
    yeni_goruntu = np.clip(yeni_goruntu, 0, 255)
    return yeni_goruntu.astype(np.uint8)

def negatif_al(goruntu):
    yeni_goruntu = 255 - goruntu
    return yeni_goruntu

def esikleme(goruntu, esik_degeri):
    yeni_goruntu = np.where(goruntu > esik_degeri, 255, 0)
    return yeni_goruntu.astype(np.uint8)

#################################################
# SORU 2: HİSTOGRAM ANALİZİ VE İSTATİSTİKLER
#################################################

def manuel_histogram_hesapla(goruntu):
    duz_goruntu = goruntu.ravel()
    hist = np.bincount(duz_goruntu, minlength=256)
    return hist

def goruntu_istatistikleri(goruntu, hist):
    M, N = goruntu.shape
    toplam_piksel = M * N
    
    ortalama = np.mean(goruntu)
    std_sapma = np.std(goruntu)
    min_deger = np.min(goruntu)
    max_deger = np.max(goruntu)
    
    prob = hist / toplam_piksel
    prob_pozitif = prob[prob > 0]
    entropi = -np.sum(prob_pozitif * np.log2(prob_pozitif))
    
    print("\n--- Soru 2: Görüntü İstatistikleri ---")
    print(f"  Boyutlar (M x N): {M} x {N}")
    print(f"  Toplam Piksel: {toplam_piksel}")
    print(f"  Min Piksel Değeri: {min_deger}")
    print(f"  Max Piksel Değeri: {max_deger}")
    print(f"  Ortalama (Mean): {ortalama:.2f}")
    print(f"  Standart Sapma: {std_sapma:.2f}")
    print(f"  Entropi: {entropi:.2f}")
    print("--------------------------------------")
    
    return ortalama, std_sapma, entropi, min_deger, max_deger

#################################################
# SORU 3: KONTRAST GERME (CONTRAST STRETCHING)
#################################################

def kontrast_germe(goruntu):
    min_val = np.min(goruntu)
    max_val = np.max(goruntu)
    
    if min_val == max_val:
        return goruntu
        
    goruntu_float = goruntu.astype(np.float32)
    yeni_goruntu = ((goruntu_float - min_val) / (max_val - min_val)) * 255
    
    return yeni_goruntu.astype(np.uint8)

#################################################
# SORU 4: HİSTOGRAM EŞİTLEME (MANUEL)
#################################################

"""
Bilgisayarla Görü Ödevi 3: Nokta İşlemleri ve Histogram İşleme
Tüm fonksiyonlar ödev isterlerine göre NumPy kullanılarak yazılmıştır.
Hazır cv2 fonksiyonları (calcHist, equalizeHist) kullanılmamıştır.
*** ÇIKTILARI PENCERE YERİNE DOSYAYA KAYDEDEN VERSİYON (SORU 4 DÜZELTİLDİ) ***
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

print("Kütüphaneler yüklendi. İşlemler başlıyor...")

#################################################
# YARDIMCI FONKSİYONLAR
#################################################

def gorsel_goster(baslik, goruntu, cmap='gray'):
    plt.figure()
    plt.title(baslik)
    plt.imshow(goruntu, cmap=cmap)
    plt.axis('off')
    print(f"-> '{baslik}' gösterim için hazırlanıyor...")

def histogram_ciz(baslik, hist):
    plt.figure()
    plt.title(baslik)
    plt.xlabel("Piksel Değeri (0-255)")
    plt.ylabel("Piksel Sayısı")
    plt.bar(range(256), hist, width=1.0, color='b')
    plt.xlim([0, 255])
    print(f"-> '{baslik}' çizim için hazırlanıyor...")

#################################################
# SORU 1: TEMEL NOKTA İŞLEMLERİ
#################################################

def parlaklik_ayarla(goruntu, c):
    yeni_goruntu = np.clip(goruntu.astype(np.int16) + c, 0, 255)
    return yeni_goruntu.astype(np.uint8)

def kontrast_ayarla(goruntu, factor):
    yeni_goruntu = factor * (goruntu.astype(np.float32) - 128) + 128
    yeni_goruntu = np.clip(yeni_goruntu, 0, 255)
    return yeni_goruntu.astype(np.uint8)

def negatif_al(goruntu):
    yeni_goruntu = 255 - goruntu
    return yeni_goruntu

def esikleme(goruntu, esik_degeri):
    yeni_goruntu = np.where(goruntu > esik_degeri, 255, 0)
    return yeni_goruntu.astype(np.uint8)

#################################################
# SORU 2: HİSTOGRAM ANALİZİ VE İSTATİSTİKLER
#################################################

def manuel_histogram_hesapla(goruntu):
    duz_goruntu = goruntu.ravel()
    hist = np.bincount(duz_goruntu, minlength=256)
    return hist

def goruntu_istatistikleri(goruntu, hist):
    M, N = goruntu.shape
    toplam_piksel = M * N
    
    ortalama = np.mean(goruntu)
    std_sapma = np.std(goruntu)
    min_deger = np.min(goruntu)
    max_deger = np.max(goruntu)
    
    prob = hist / toplam_piksel
    prob_pozitif = prob[prob > 0]
    entropi = -np.sum(prob_pozitif * np.log2(prob_pozitif))
    
    print("\n--- Soru 2: Görüntü İstatistikleri ---")
    print(f"  Boyutlar (M x N): {M} x {N}")
    print(f"  Toplam Piksel: {toplam_piksel}")
    print(f"  Min Piksel Değeri: {min_deger}")
    print(f"  Max Piksel Değeri: {max_deger}")
    print(f"  Ortalama (Mean): {ortalama:.2f}")
    print(f"  Standart Sapma: {std_sapma:.2f}")
    print(f"  Entropi: {entropi:.2f}")
    print("--------------------------------------")
    
    return ortalama, std_sapma, entropi, min_deger, max_deger

#################################################
# SORU 3: KONTRAST GERME (CONTRAST STRETCHING)
#################################################

def kontrast_germe(goruntu):
    min_val = np.min(goruntu)
    max_val = np.max(goruntu)
    
    if min_val == max_val:
        return goruntu
        
    goruntu_float = goruntu.astype(np.float32)
    yeni_goruntu = ((goruntu_float - min_val) / (max_val - min_val)) * 255
    
    return yeni_goruntu.astype(np.uint8)

#################################################
# SORU 4: HİSTOGRAM EŞİTLEME (MANUEL)
#################################################

def manuel_histogram_esitleme(goruntu):
    """
    Soru 4a: Histogram eşitleme algoritmasını sıfırdan uygular.
    Hazır fonksiyon (cv2.equalizeHist) kullanmaz.
    *** BU BÖLÜM DÜZELTİLDİ ***
    """
    # 1. Görüntünün histogramını hesapladım
    hist = manuel_histogram_hesapla(goruntu)
    
    # 2. Kümülatif histogramı (CDF) hesapladım
    cdf = hist.cumsum()
    
    # 3. Dönüşüm fonksiyonunu oluşturdum: s_k = (L-1) * Σ(nj / MN)
    # L-1 = 255
    # MN = Toplam piksel sayısı = cdf[-1]
    M_N = cdf[-1]
    
    # Görüntü boşsa (veya M_N = 0 ise) sıfıra bölme hatasını engellemek için:
    if M_N == 0:
        return goruntu
        
    # Ödevdeki formül:
    cdf_normalized = (cdf * 255 / M_N).astype(np.uint8)

    # 4. Her pikseli dönüştür
    # NumPy ile pikselleri eşleme
    esitlenmis_goruntu = cdf_normalized[goruntu]
    
    return esitlenmis_goruntu

#################################################
# SORU 5: GAMMA DÜZELTMESİ
#################################################

def gamma_duzeltme(goruntu, gamma):
    goruntu_norm = goruntu / 255.0
    duzeltmis = np.power(goruntu_norm, gamma)
    yeni_goruntu = (255 * duzeltmis).astype(np.uint8)
    return yeni_goruntu

#################################################
# ANA ÇALIŞTIRMA BLOĞU
#################################################

if __name__ == "__main__":
    
    goruntu_path = 'test_goruntu.png'
    orijinal_goruntu = cv2.imread(goruntu_path, cv2.IMREAD_GRAYSCALE)
    
    if orijinal_goruntu is None:
        print(f"HATA: '{goruntu_path}' dosyası bulunamadı veya okunamadı.")
        print("Lütfen 'test_goruntu.png' dosyasının 'odev3.py' ile aynı klasörde olduğundan emin olun.")
    else:
        print(f"Orijinal görüntü '{goruntu_path}' başarıyla yüklendi.")
        
        # Orijinal görüntüyü göster ve KAYDET
        gorsel_goster("Orijinal Görüntü (Gri Tonlama)", orijinal_goruntu)
        plt.savefig("Cikti_0_Orijinal.png")
        print("-> 'Cikti_0_Orijinal.png' DOSYAYA KAYDEDİLDİ.")

        # --- SORU 1 ÇALIŞTIRMA ---
        print("\n--- Soru 1 Çalıştırılıyor ---")
        parlak_goruntu = parlaklik_ayarla(orijinal_goruntu, 50)
        karanlik_goruntu = parlaklik_ayarla(orijinal_goruntu, -50)
        kontrastli_goruntu = kontrast_ayarla(orijinal_goruntu, 1.8)
        negatif_goruntu = negatif_al(orijinal_goruntu)
        esiklenmis_goruntu = esikleme(orijinal_goruntu, 128)
        
        plt.figure(figsize=(15, 5))
        plt.suptitle("Soru 1: Temel Nokta İşlemleri", fontsize=16)
        plt.subplot(1, 5, 1); plt.title("Parlak (+50)"); plt.imshow(parlak_goruntu, cmap='gray'); plt.axis('off')
        plt.subplot(1, 5, 2); plt.title("Karanlık (-50)"); plt.imshow(karanlik_goruntu, cmap='gray'); plt.axis('off')
        plt.subplot(1, 5, 3); plt.title("Kontrast (1.8)"); plt.imshow(kontrastli_goruntu, cmap='gray'); plt.axis('off')
        plt.subplot(1, 5, 4); plt.title("Negatif"); plt.imshow(negatif_goruntu, cmap='gray'); plt.axis('off')
        plt.subplot(1, 5, 5); plt.title("Eşikleme (128)"); plt.imshow(esiklenmis_goruntu, cmap='gray'); plt.axis('off')
        plt.savefig("Cikti_1_Nokta_Islemleri.png")
        print("-> 'Cikti_1_Nokta_Islemleri.png' DOSYAYA KAYDEDİLDİ.")

        # --- SORU 2 ÇALIŞTIRMA ---
        print("\n--- Soru 2 Çalıştırılıyor ---")
        orijinal_hist = manuel_histogram_hesapla(orijinal_goruntu)
        histogram_ciz("Soru 2: Orijinal Histogram", orijinal_hist)
        plt.savefig("Cikti_2_Histogram.png")
        print("-> 'Cikti_2_Histogram.png' DOSYAYA KAYDEDİLDİ.")
        
        goruntu_istatistikleri(orijinal_goruntu, orijinal_hist) 

        # --- SORU 3 ÇALIŞTIRMA ---
        print("\n--- Soru 3 Çalıştırılıyor ---")
        gerilmis_goruntu = kontrast_germe(orijinal_goruntu)
        gerilmis_hist = manuel_histogram_hesapla(gerilmis_goruntu)
        
        plt.figure(figsize=(10, 8))
        plt.suptitle("Soru 3: Kontrast Germe", fontsize=16)
        plt.subplot(2, 2, 1); plt.title("Orijinal Görüntü"); plt.imshow(orijinal_goruntu, cmap='gray'); plt.axis('off')
        plt.subplot(2, 2, 2); plt.title("Gerilmiş Görüntü"); plt.imshow(gerilmis_goruntu, cmap='gray'); plt.axis('off')
        plt.subplot(2, 2, 3); plt.title("Orijinal Histogram"); plt.bar(range(256), orijinal_hist); plt.xlim([0, 255])
        plt.subplot(2, 2, 4); plt.title("Gerilmiş Histogram"); plt.bar(range(256), gerilmis_hist); plt.xlim([0, 255])
        plt.savefig("Cikti_3_Kontrast_Germe.png")
        print("-> 'Cikti_3_Kontrast_Germe.png' DOSYAYA KAYDEDİLDİ.")
        
        # --- SORU 4 ÇALIŞTIRMA ---
        print("\n--- Soru 4 Çalıştırılıyor ---")
        esitlenmis_goruntu = manuel_histogram_esitleme(orijinal_goruntu)
        esitlenmis_hist = manuel_histogram_hesapla(esitlenmis_goruntu)
        
        plt.figure(figsize=(10, 8))
        plt.suptitle("Soru 4: Histogram Eşitleme", fontsize=16)
        plt.subplot(2, 2, 1); plt.title("Orijinal Görüntü"); plt.imshow(orijinal_goruntu, cmap='gray'); plt.axis('off')
        plt.subplot(2, 2, 2); plt.title("Eşitlenmiş Görüntü"); plt.imshow(esitlenmis_goruntu, cmap='gray'); plt.axis('off')
        plt.subplot(2, 2, 3); plt.title("Orijinal Histogram"); plt.bar(range(256), orijinal_hist); plt.xlim([0, 255])
        plt.subplot(2, 2, 4); plt.title("Eşitlenmiş Histogram"); plt.bar(range(256), esitlenmis_hist); plt.xlim([0, 255])
        plt.savefig("Cikti_4_Histogram_Esitleme.png")
        print("-> 'Cikti_4_Histogram_Esitleme.png' DOSYAYA KAYDEDİLDİ.")
        
        # --- SORU 5 ÇALIŞTIRMA ---
        print("\n--- Soru 5 Çalıştırılıyor ---")
        gamma_degerleri = [0.5, 1.5, 2.0, 2.5] 
        
        plt.figure(figsize=(20, 5)) 
        plt.suptitle("Soru 5: Gamma Düzeltmesi", fontsize=16)
        
        plt.subplot(1, 5, 1); plt.title("Orijinal (Gamma=1.0)"); plt.imshow(orijinal_goruntu, cmap='gray'); plt.axis('off')
        
        for i, gamma in enumerate(gamma_degerleri):
            gamma_goruntu = gamma_duzeltme(orijinal_goruntu, gamma)
            plt.subplot(1, 5, i + 2)
            plt.title(f"Gamma = {gamma}")
            plt.imshow(gamma_goruntu, cmap='gray')
            plt.axis('off')
        plt.savefig("Cikti_5_Gamma.png")
        print("-> 'Cikti_5_Gamma.png' DOSYAYA KAYDEDİLDİ.")

        # Soru 5 Analiz kısmı
        print("\n--- Soru 5: Gamma Analizi (Raporuna Ekleyebilirsin) ---")
        print(" * Gamma < 1 (örn: 0.5): Görüntünün karanlık bölgelerinin detaylarını aydınlatır, genel olarak görüntüyü 'parlatır'. Koyu (underexposed) çekilmiş fotoğrafları düzeltmek için kullanılır.")
        print(" * Gamma = 1 (örn: 1.0): Görüntüyü değiştirmez (input = output).")
        print(" * Gamma > 1 (örn: 1.5, 2.0, 2.5): Görüntünün aydınlık bölgelerini karartır, genel olarak görüntüyü 'karartır'. Çok parlak (overexposed) çekilmiş fotoğrafları dengelemek için kullanılır.")
        
        print("\n*** TÜM İŞLEMLER TAMAMLANDI ***")
        print("Tüm grafikler 'Cikti_...' olarak KOD KLASÖRÜNE KAYDEDİLDİ.")