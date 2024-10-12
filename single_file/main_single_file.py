from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    # Open an image file
    with Image.open(input_path) as img:
        # Resize the image
        resized_img = img.resize((new_width, new_height))
        # Save the resized image
        resized_img.save(output_path)
        print(f"Image saved to {output_path}")

if __name__ == "__main__":
    # Input image path
    input_image = "single_file/input_image.png"  # Replace with your image file path
    # Output image path
    output_image = "single_file/resized_image.png"
    # Desired dimensions
    width = 800  # Replace with desired width
    height = 600  # Replace with desired height
    
    resize_image(input_image, output_image, width, height)
