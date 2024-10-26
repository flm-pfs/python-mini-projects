from PIL import Image


def resize_image(input_path, output_path, size):
    """
    Resize an image to the specified size and save it to the output path.

    :param input_path: Path to the input image file.
    :param output_path: Path to save the resized image file.
    :param size: Tuple of (width, height) for the new size.
    """
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize(size, Image.Resampling.LANCZOS)
            resized_img.save(output_path)
            print(f"Image successfully resized and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    input_image_path = "ImageResizer/input_image.jpg"  # Path to the input image
    # Path to save the resized image
    output_image_path = "ImageResizer/output_image.jpg"
    new_size = (800, 600)  # New size (width, height)

    resize_image(input_image_path, output_image_path, new_size)
