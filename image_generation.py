from PIL import Image

def print_image(image):
    image = Image.open(image)
    width, height = 120, 80
    aspect_ratio = height/width
    terminal_width = 80  
    new_width = terminal_width
    new_height = int(terminal_width * aspect_ratio)
    image = image.resize((new_width, new_height))

    image = image.convert('L')
    ascii_chars = '@*#. '
    for y in range(new_height):
        for x in range(new_width):
            pixel_value = image.getpixel((x, y))
            char_index = int(pixel_value / 52)
            print(ascii_chars[char_index], end='')
        print()
    return 