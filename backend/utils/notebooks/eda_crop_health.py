"""
AgriAssist AI - Phase 1
Exploratory Data Analysis (EDA) - Crop Health Dataset
This script inspects crop disease image dataset using pandas and visualization libraries.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np

# ---------- LOAD DATA ----------
DATA_PATH = os.path.join(os.path.dirname(__file__), "../datasets/crop_images")

# Assume dataset folder structure: crop_images/<class_name>/<image_files>
classes = []
counts = []

for class_name in os.listdir(DATA_PATH):
    class_dir = os.path.join(DATA_PATH, class_name)
    if os.path.isdir(class_dir):
        img_files = [f for f in os.listdir(class_dir) if f.lower().endswith((".jpg",".png",".jpeg"))]
        classes.append(class_name)
        counts.append(len(img_files))

# Create DataFrame for summary
df = pd.DataFrame({"class": classes, "image_count": counts})
print("Crop Health Dataset Summary:\n", df)

# ---------- VISUALIZATIONS ----------

# Class distribution bar chart
plt.figure(figsize=(10,6))
sns.barplot(x="class", y="image_count", data=df, palette="Set2")
plt.title("Distribution of Crop Health Classes")
plt.xlabel("Class")
plt.ylabel("Number of Images")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("eda_crop_health_class_distribution.png")
plt.close()

# Inspect sample image sizes
sample_sizes = []
for class_name in classes:
    class_dir = os.path.join(DATA_PATH, class_name)
    img_files = [f for f in os.listdir(class_dir) if f.lower().endswith((".jpg",".png",".jpeg"))]
    if img_files:
        img_path = os.path.join(class_dir, img_files[0])
        with Image.open(img_path) as img:
            sample_sizes.append(img.size)

sizes_df = pd.DataFrame(sample_sizes, columns=["width","height"])
print("\nSample image sizes:\n", sizes_df.describe())

# Histogram of image widths and heights
plt.figure(figsize=(8,5))
sns.histplot(sizes_df["width"], bins=20, color="blue", kde=True)
plt.title("Distribution of Image Widths")
plt.xlabel("Width (pixels)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("eda_crop_health_widths.png")
plt.close()

plt.figure(figsize=(8,5))
sns.histplot(sizes_df["height"], bins=20, color="green", kde=True)
plt.title("Distribution of Image Heights")
plt.xlabel("Height (pixels)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("eda_crop_health_heights.png")
plt.close()

# ---------- PIXEL INTENSITY CHECK ----------
# Inspect one sample image pixel intensity distribution
if classes:
    sample_class = classes[0]
    sample_dir = os.path.join(DATA_PATH, sample_class)
    sample_img = [f for f in os.listdir(sample_dir) if f.lower().endswith((".jpg",".png",".jpeg"))][0]
    sample_path = os.path.join(sample_dir, sample_img)
    with Image.open(sample_path).convert("L") as img_gray:
        arr = np.array(img_gray).flatten()
        plt.figure(figsize=(8,5))
        sns.histplot(arr, bins=50, color="purple")
        plt.title(f"Pixel Intensity Distribution ({sample_class} sample)")
        plt.xlabel("Pixel Intensity (0-255)")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig("eda_crop_health_pixel_intensity.png")
        plt.close()

print("EDA complete. Crop health plots saved as PNG files in current directory.")
