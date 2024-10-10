from PIL import Image
import os

def resize_image(input_path, output_path, new_width, new_height):
    """Resizes a single image and saves it to the output path."""
    with Image.open(input_path) as img:
        resized_img = img.resize((new_width, new_height))
        resized_img.save(output_path)
        print(f"Resized image saved to {output_path}")

def resize_images_in_folder(input_folder, output_folder, new_width, new_height):
    """Resizes all images in the input folder and saves them to the output folder."""
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is an image (by extension)
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_image(input_path, output_path, new_width, new_height)

if __name__ == "__main__":
    # Define the input folder path
    input_folder = "folder_of_images/input_images"  # Replace with the path to your input folder
    # Define the output folder path
    output_folder = "folder_of_images/resized_images"  # Replace with your desired output folder
    
    # Desired dimensions
    width = 800  # Replace with the desired width
    height = 600  # Replace with the desired height
    
    # Resize all images in the input folder
    resize_images_in_folder(input_folder, output_folder, width, height)
