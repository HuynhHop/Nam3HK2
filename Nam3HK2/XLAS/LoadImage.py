# import cv2
# path=r'D:\Nam3HK2\XLAS\anh-gai-k5-1.jpg'
# img=cv2.imread(path)
# # cv2.imshow('Load Image', img)
# cv2.waitKey()
#Piecewise_liner, gamma, làm trơn ảnh (lọc trung bình, lọc Gauss, lọc trung vi), làm sáng histogram
import cv2
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import numpy as np

def load_image():
    global original_image
    file_path = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img.thumbnail((250, 250))
        img = ImageTk.PhotoImage(img)

        panel.img = img
        panel.config(image=img)
        original_image = np.array(Image.open(file_path))  # Save the original image

def apply_log_transform(c_value):
    global original_image
    if original_image is not None:
        # Apply the log transformation
        c = c_value / 10.0
        transformed_img = np.log(1 + c * original_image)
        transformed_img = (transformed_img / transformed_img.max()) * 255
        transformed_img = transformed_img.astype(np.uint8)

        # Display the transformed image in the empty frame
        transformed_img = Image.fromarray(transformed_img)
        transformed_img.thumbnail((250, 250))
        transformed_img = ImageTk.PhotoImage(transformed_img)

        panel_empty.img = transformed_img
        panel_empty.config(image=transformed_img)

def apply_piecewise_linear_transform(low_value, high_value):
    global original_image
    if original_image is not None:
        # Apply the piecewise-linear transformation
        low_coefficient = low_value / 10.0
        high_coefficient = high_value / 10.0
        transformed_img = np.piecewise(original_image,
                                       [original_image <= low_coefficient,
                                        (original_image > low_coefficient) & (original_image <= high_coefficient),
                                        original_image > high_coefficient],
                                       [lambda x: 0, lambda x: 255 * (x - low_coefficient) / (high_coefficient - low_coefficient), lambda x: 255])

        # Display the transformed image in the empty frame
        transformed_img = Image.fromarray(transformed_img.astype(np.uint8))
        transformed_img.thumbnail((250, 250))
        transformed_img = ImageTk.PhotoImage(transformed_img)

        panel_empty.img = transformed_img
        panel_empty.config(image=transformed_img)

def apply_gamma_transform(c_value, gamma_value):
    global original_image
    if original_image is not None:
        # Apply the gamma transformation
        c = c_value / 10.0
        gamma = gamma_value / 10.0
        transformed_img = c * (original_image ** gamma)
        transformed_img = (transformed_img / transformed_img.max()) * 255
        transformed_img = transformed_img.astype(np.uint8)

        # Display the transformed image in the empty frame
        transformed_img = Image.fromarray(transformed_img)
        transformed_img.thumbnail((250, 250))
        transformed_img = ImageTk.PhotoImage(transformed_img)

        panel_empty.img = transformed_img
        panel_empty.config(image=transformed_img)

def save_transformed_image():
    global original_image
    if original_image is not None:
        transformed_image = panel_empty.img
        if transformed_image is not None:
            # Save the edited image
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                transformed_image = Image.open(transformed_image)
                transformed_image.save(file_path)

def reset_image():
    # Remove the edited image
    panel_empty.img = None
    panel_empty.config(image=None)

# Create a tkinter window and set the interface screen size to 1000x500
root = tk.Tk()
root.title("Image Transformation Tool")
root.geometry("1000x500")
root.configure(bg="gray")

# Create a frame for buttons and place it in column 0, row 0
button_frame = tk.Frame(root, width=800, height=200, bg="gray")
button_frame.grid(row=0, column=0, columnspan=5, sticky="nsew")

# Create the Load Image button and place it in row 0 within the button_frame
button_load = tk.Button(button_frame, text="Load Image", command=load_image, bg="red", fg="white")
button_load.grid(row=0, column=0, padx=10, pady=10)

# Create a frame for the original image and place it in column 0, row 1
image_frame_original = tk.Frame(root, width=400, height=300, bg="gray")
image_frame_original.grid(row=1, column=0, padx=10, pady=10)

# Create a label to display the original image and place it in row 0 within image_frame_original
panel = tk.Label(image_frame_original, text="Original Image", bg="white")
panel.grid(row=0)

# Create a frame for the edited image and place it in column 1, row 1
image_frame_empty = tk.Frame(root, width=400, height=300, bg="gray")
image_frame_empty.grid(row=1, column=1, padx=10, pady=10)

# Create a label to display the edited image and place it in row 0 within image_frame_empty
panel_empty = tk.Label(image_frame_empty, text="Edited Image", bg="white")
panel_empty.grid(row=0)

# Create a frame for text and sliders and place it in column 0, row 2
log_transform_frame = tk.Frame(root, width=800, height=50, bg="gray")
log_transform_frame.grid(row=2, column=0, columnspan=5, pady=10)

# Create a frame to hold text and set its background color to blue
text_frame_log = tk.Frame(log_transform_frame, width=150, height=50, bg="blue")
text_frame_log.grid(row=0, column=0, padx=10)

# Text line for Log Transform
label_log_transform = tk.Label(text_frame_log, text="Log Transform", bg="blue", fg="white")
label_log_transform.grid(row=0, column=0, padx=10)

# Log coefficient slider
log_coefficient_value = tk.DoubleVar()
log_coefficient_slider = ttk.Scale(log_transform_frame, from_=0, to=50, variable=log_coefficient_value,
                                   orient=tk.HORIZONTAL, length=150)
log_coefficient_slider.set(0)
log_coefficient_slider.grid(row=0, column=1, padx=10)

# Apply Log Transform button
apply_log_button = tk.Button(log_transform_frame, text="Apply Log Transform", command=lambda: apply_log_transform(log_coefficient_value.get()))
apply_log_button.grid(row=0, column=2, padx=10)

# Create a frame for Piecewise-Linear Transformation and place it in column 0, row 3
piecewise_linear_frame = tk.Frame(root, width=800, height=50, bg="gray")
piecewise_linear_frame.grid(row=3, column=0, columnspan=5, pady=10)

# Text line for Piecewise-Linear Transform
text_frame_piecewise = tk.Frame(piecewise_linear_frame, width=150, height=50, bg="blue")
text_frame_piecewise.grid(row=0, column=0, padx=10)

# Text line for Piecewise-Linear Transform
label_piecewise_transform = tk.Label(text_frame_piecewise, text="Piecewise Transform", bg="blue", fg="white")
label_piecewise_transform.grid(row=0, column=0, padx=10)

# Low coefficient slider
low_coefficient_value = tk.DoubleVar()
low_coefficient_slider = ttk.Scale(piecewise_linear_frame, from_=0, to=50, variable=low_coefficient_value,
                                   orient=tk.HORIZONTAL, length=150)
low_coefficient_slider.set(0)
low_coefficient_slider.grid(row=0, column=1, padx=10)

# High coefficient slider
high_coefficient_value = tk.DoubleVar()
high_coefficient_slider = ttk.Scale(piecewise_linear_frame, from_=0, to=50, variable=high_coefficient_value,
                                    orient=tk.HORIZONTAL, length=150)
high_coefficient_slider.set(50)
high_coefficient_slider.grid(row=0, column=2, padx=10)

# Apply Piecewise-Linear Transform button
apply_piecewise_button = tk.Button(piecewise_linear_frame, text="Apply Piecewise-Linear Transform",
                                   command=lambda: apply_piecewise_linear_transform(low_coefficient_value.get(),
                                                                                    high_coefficient_value.get()))
apply_piecewise_button.grid(row=0, column=3, padx=10)

# Create a frame for Gamma Transformation and place it in column 0, row 4
gamma_transform_frame = tk.Frame(root, width=800, height=50, bg="gray")
gamma_transform_frame.grid(row=4, column=0, columnspan=5, pady=10)

# Text line for Gamma Transform
text_frame_gamma = tk.Frame(gamma_transform_frame, width=150, height=50, bg="blue")
text_frame_gamma.grid(row=0, column=0, padx=10)

# Text line for Gamma Transform
label_gamma_transform = tk.Label(text_frame_gamma, text="Gamma Transform", bg="blue", fg="white")
label_gamma_transform.grid(row=0, column=0, padx=10)

# Gamma coefficient slider
gamma_coefficient_value = tk.DoubleVar()
gamma_coefficient_slider = ttk.Scale(gamma_transform_frame, from_=0, to=50, variable=gamma_coefficient_value,
                                     orient=tk.HORIZONTAL, length=150)
gamma_coefficient_slider.set(0)
gamma_coefficient_slider.grid(row=0, column=1, padx=10)

# Gamma slider
gamma_value = tk.DoubleVar()
gamma_slider = ttk.Scale(gamma_transform_frame, from_=0, to=50, variable=gamma_value,
                         orient=tk.HORIZONTAL, length=150)
gamma_slider.set(0)
gamma_slider.grid(row=0, column=2, padx=10)

# Apply Gamma Transform button
apply_gamma_button = tk.Button(gamma_transform_frame, text="Apply Gamma Transform",
                               command=lambda: apply_gamma_transform(gamma_coefficient_value.get(),
                                                                    gamma_value.get()))
apply_gamma_button.grid(row=0, column=3, padx=10)

# Create a Save button to save the edited image and place it in column 4, row 5
save_button = tk.Button(gamma_transform_frame, text="Save", command=save_transformed_image)
save_button.grid(row=0, column=4, padx=10)

# Create a Reset button to remove the edited image and place it in column 5, row 5
reset_button = tk.Button(gamma_transform_frame, text="Reset", command=reset_image)
reset_button.grid(row=0, column=5, padx=10)

# Run the tkinter window
root.mainloop()