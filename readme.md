# PixelCrypt

Message Hiding Inside Image Using Image Processing

## Team Members
1. Arshit Jolapara
2. Azim Baldiwala

--- 

## Overview

PixelCrypt provides two methods for hiding messages inside images: lossy and lossless encoding and decoding.

### 1. Lossy Encoding and Decoding
- **Method**: Uses the Least Significant Bit (LSB) technique to hide messages within the image's pixels.
- **Process**: Converts the message into bits and embeds them in the image’s pixel RGB values. End delimiters mark the end of the message.
- **Advantages**:
  - Fast
  - Suitable for small messages
  - Easy to implement
- **Disadvantages**:
  - Noticeable image changes with longer messages

### 2. Lossless Encoding and Decoding
- **Method**: Similar to lossy, but hides message bits in randomly selected pixels based on a user-provided key.
- **Process**: Generates a random number using a key for encoding and requires the same key for decoding.
- **Advantages**:
  - Preserves image quality
  - Requires a key for decoding
- **Disadvantages**:
  - More complex to implement

---

## Dependencies
- Python 3.5 or later
- Flask
- Pillow
- Python-OpenCV
- Numpy

---

## Project Files
1. **app.py**: Backend file for Flask, contains all web routes.
2. **hide_lossy.py**: Implements the lossy message hiding method.
3. **hide_lossless.py**: Implements the lossless message hiding method.
4. **templates/**: Directory containing HTML files for the GUI.
5. **static/**: Directory with server data (user images, GUI dependencies).
6. **Sample_images/**: Contains sample image dataset.

---

## How to Run

**Method 1: Using Flask GUI**
1. Run `app.py`.
2. Open [http://localhost:5000](http://localhost:5000) in a web browser.

**Method 2: Using Console**
1. Open Command Prompt.
2. Execute `hide_lossy.py` or `hide_lossless.py` for console-based applications.


