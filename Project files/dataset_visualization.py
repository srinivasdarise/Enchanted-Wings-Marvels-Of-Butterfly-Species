import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Set dataset path
data_dir = 'butterfly_dataset'  # <-- Replace with your actual path if needed

# Collect all image paths and corresponding labels
image_paths = []
labels = []

classes = os.listdir(data_dir)
for label in classes:
    class_path = os.path.join(data_dir, label)
    if not os.path.isdir(class_path):
        continue
    for img_file in glob.glob(os.path.join(class_path, '*.jpg')):
        image_paths.append(img_file)
        labels.append(label)

# Create a DataFrame
df = pd.DataFrame({
    'image_path': image_paths,
    'label': labels
})

print("Total images found:", len(df))
print("Classes found:", df['label'].nunique())

# Visualize class distribution
plt.figure(figsize=(14, 6))
sns.countplot(data=df, x='label', order=df['label'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Distribution of Butterfly Classes')
plt.xlabel('Class Name')
plt.ylabel('Number of Images')
plt.tight_layout()
plt.show()

# Display sample images from different classes
plt.figure(figsize=(10, 10))
for i in range(9):
    img = Image.open(df.iloc[i]['image_path'])
    plt.subplot(3, 3, i + 1)
    plt.imshow(img)
    plt.title(df.iloc[i]['label'])
    plt.axis('off')

plt.suptitle("Sample Images from Butterfly Dataset", fontsize=16)
plt.tight_layout()
plt.show()
