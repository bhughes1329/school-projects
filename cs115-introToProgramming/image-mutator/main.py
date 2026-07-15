# === CS 115 Homework 4 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Brooke Hughes
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 4 ===
from hw4_library import ppm_to_list_of_lists_of_rgbs, save_string_to_txt


def rgb_to_grayscale(image):
    """
    Mutates a 2D list of RGB pixels to a 2D list of grayscale values.
    Uses the CCIR 601 standard brightness formula:
        gray = int (0.299*red + 0.587*green + 0.114*blue)
    Does not return anything
    """
    image[:] = list(map(lambda row: list(map(lambda col: int(0.299*col[0] + 0.587*col[1] + 0.114*col[2]), row)), image))

def brightness_to_ascii(brightness):
    """
    TODO: Fill in your own docstring here based on 
    the homework description
    Use the table on the homework for specific ranges
    of brightness to ASCII
    """
    if brightness <= 25.99:
        return "@"
    elif brightness <= 51.99:
        return "#"
    elif brightness <= 76.99:
        return "%"
    elif brightness <= 102.99:
        return "*"
    elif brightness <= 127.99:
        return "="
    elif brightness <= 153.99:
        return "+"
    elif brightness <= 179.99:
        return "-"
    elif brightness <= 204.99:
        return ":"
    elif brightness <= 230.99:
        return "."
    elif brightness <= 255:
        return " "


def image_to_ascii_string(image):
    """
    Convert a 2D list of grayscale values (0–255)
    into a single string of ASCII characters where
    each row in the image corresponds to a line
    in the ASCII string. 

    Each line break is represented with \n\r
    to ensure compatibility with Windows 
    
    returns that string, only containing valid ASCII
    characters
    """
    return '\r\n'.join(
        map(lambda row: ''.join(map(brightness_to_ascii, row)), image))

def invert(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    image[:] = list(map(lambda row: list(map(lambda col: 255-col, row)), image))


def lighten(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    image = map(lambda row: map(lambda col: min(col*1.3, 255), row), image)


def darken(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    image = map(lambda row: map(lambda col: max(col*0.7, 0), row), image)


def erase(image):
    """
    Erases an image by turning all of its RBG or grayscale values into 0s
    Returns nothing, just mutates the given list of pixel values
    """
    image[:] = list(map(lambda row: list(map(lambda col: 0, row)), image))


def load_rgb_image(image_name):
    """
    Given a filename, image_name, returns 
    a grayscale image, 
    represented as a 2D list of intensities

    Do not change this function. It is just here for reference.
    """
    image = ppm_to_list_of_lists_of_rgbs(image_name)
    return image 


if __name__ == "__main__":
    # All code you want to run goes in this indented block
    # You can change the name of ppm_image_filename
    ppm_image_filename = r"C:\Users\brook\CS 115\hw\hw4\treasure_map.ppm"

    # This line calls our library function to load the image as 
    # a list of lists of rgb values
    image = load_rgb_image(ppm_image_filename)
    rgb_to_grayscale(image)
    
    ascii_string = image_to_ascii_string(image)

    invert(image)
    lighten(image)

    save_string_to_txt(ascii_string)
