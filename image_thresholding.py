# Image Segmentation Using Thresholding Techniques in OpenCV
# Developed By: Subashini K
# Register No: 212225240160

import cv2
import matplotlib.pyplot as plt

# 1. Original Image
img = cv2.imread("city.jpg")

if img is None:
    print("Error: Image not found. Check the file path.")
else:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()

# 2. Original Grayscale Image
img_gray = cv2.imread("city.jpg", cv2.IMREAD_GRAYSCALE)
plt.imshow(img_gray, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")
plt.show()

# 3. Global Thresholding
_, result_global = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
plt.imshow(result_global, cmap="gray")
plt.title("Global Thresholding")
plt.axis("off")
plt.show()

# 4. Adaptive Thresholding
result_adaptive = cv2.adaptiveThreshold(
    img_gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 2
)
plt.imshow(result_adaptive, cmap="gray")
plt.title("Adaptive Thresholding")
plt.axis("off")
plt.show()

# 5. Otsu's Thresholding
_, result_otsu = cv2.threshold(
    img_gray, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
plt.imshow(result_otsu, cmap="gray")
plt.title("Otsu's Thresholding")
plt.axis("off")
plt.show()
