import os
from PIL import Image

# Configuration
input_folder = 'input_images'
output_folder = 'output_images'
new_size = (800, 600)  # Width x Height
output_format = 'JPEG'  # Can be 'PNG', 'JPEG', etc.

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each file in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_name = os.path.splitext(filename)[0] + '.' + output_format.lower()
        output_path = os.path.join(output_folder, output_name)

        # Open, resize, and save image
        try:
            with Image.open(input_path) as img:
                resized_img = img.resize(new_size)
                resized_img = resized_img.convert("RGB")  # ensure compatibility
                resized_img.save(output_path, output_format)
                print(f"Resized and saved: {output_name}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
