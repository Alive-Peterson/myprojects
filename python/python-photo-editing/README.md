# 🖼️ PyPhotoshop – A Simple Image Processing Library

**python-photo-editing** is a Python-based mini image processing toolkit that supports various effects like brightness adjustment, contrast manipulation, blurring, kernel filtering, and edge detection — all using just NumPy and basic image handling.

---

## 📦 Features

- 📈 Brighten or darken images  
- 🎨 Adjust image contrast  
- 🌫️ Apply blur filters  
- 🧮 Use custom kernels (e.g., Sobel filters)  
- 🖇️ Combine images with vector math  
- 🗂️ Lightweight and built only with Python and NumPy  

---

## 🛠️ Requirements

- Python 3.x  
- NumPy

Install required packages using:
```bash
pip install -r requirements.txt
```

## 🚀 How to Run
Run the main transformation script to apply filters:
```bash
python transform.py
```
It applies various effects to demo images like lake.png or city.png and writes output images such as:

brightened.png
darkened.png
increased_contrast.png
blur_k3.png
blur_k15.png
sobel_x.png, sobel_y.png, etc.

## 💡 Sample Usage
```python
from transform import adjust_brightness
from image import Image

img = Image(filename='lake.png')
bright = adjust_brightness(img, 1.5)
bright.write_image('brightened_lake.png')
```

## 🧮 Example Kernels
Sobel X (horizontal edge detection):
```python
sobel_x_kernel = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])
```
Sobel Y (vertical edge detection):
```python
sobel_y_kernel = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
])
```

## 🛠️ Customization Tips
Create new filters by editing transform_empty.py.

Add additional PNG support or compression features in png.py.

Experiment with combining images using vector operations like:
```pyhton
result = img1 + img2 * 0.5
```

## 🪪 License
This project is open-source and free to use for educational or personal use.