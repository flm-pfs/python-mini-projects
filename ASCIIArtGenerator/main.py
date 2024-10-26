from PIL import Image


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayscale_image(image):
    return image.convert("L")


def pixels_to_ascii(image, ascii_chars=" .:-=+*#%@"):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ascii_chars[pixel_value * (len(ascii_chars) - 1) // 255]
    return ascii_str


def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}.")
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayscale_image(image)
    ascii_str = pixels_to_ascii(image)

    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    return ascii_img


if __name__ == "__main__":
    image_path = r"ASCIIArtGenerator\flm.png"
    width = int(input("Enter the width of the ASCII art (default: 100): "))

    ascii_art = convert_image_to_ascii(image_path, width)
    if ascii_art:
        print(ascii_art)
