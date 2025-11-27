# 📸 Point Operations and Histogram

This project focuses on implementing fundamental image processing algorithms from scratch using the **NumPy** library, **without** using ready-made library functions such as `cv2.calcHist()` and `cv2.equalizeHist()`.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-ffffff?style=for-the-badge&logo=matplotlib&logoColor=blue)

---

## 🎯 Applied Techniques and Report View

In this project, 5 main image processing techniques were coded, and their results are presented below in a "report" format.

### 1. Original Image
All operations were performed on the 512x512 pixel grayscale version of the "Lena" test image.

![Original Image](Cikti_0_Orijinal.png)

### 2. Basic Point Operations
Brightness adjustment, contrast adjustment, negative transformation, and thresholding operations were applied. All overflow controls were handled using `np.clip`.

![Question 1 Output](Cikti_1_Nokta_Islemleri.png)

### 3. Histogram Analysis
The image's histogram was calculated manually using `np.bincount`.
* **Mean:** 132.43
* **Standard Deviation:** 44.90
* **Entropy:** 6.97

![Question 2 Output](Cikti_2_Histogram.png)

### 4. Contrast Stretching
The formula `output = ((input - min) / (max - min)) * 255` was implemented from scratch to expand the dynamic range of the image.

![Question 3 Output](Cikti_3_Kontrast_Germe.png)

### 5. Histogram Equalization
The histogram equalization algorithm was **manually** implemented using the Cumulative Distribution Function (CDF) `hist.cumsum()`.

![Question 4 Output](Cikti_4_Histogram_Esitleme.png)

### 6. Gamma Correction
The formula `output = 255 * (input / 255)^gamma` was applied for the gamma values (0.5, 1.5, 2.0, 2.5) requested in the assignment.

![Question 5 Output](Cikti_5_Gamma.png)

---

## 🚀 Setup and Running

1.  Make sure the necessary libraries are installed:
    ```bash
    pip install numpy matplotlib opencv-python pillow
    ```
2.  Ensure the `test_goruntu.png` file is in the same folder as the code.
3.  Run the script with the following command:
    ```bash
    python odev3.py
    ```
4.  The script will save all visual outputs as `Cikti_*.png` inside the folder.

---

## 👤 Project Owner
Artificial Intelligence Engineering Student

* **Gülnaz Aydemir**
* Ostim Technical University
