import os.path
import sys
from PIL import Image


def main():
    check_args()
    image_merging()


def check_args():
    allowed_extensions = [".jpg", ".jpeg", ".png"]

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        if os.path.splitext(sys.argv[1])[1].lower() not in allowed_extensions:
            sys.exit("Invalid input")
        elif os.path.splitext(sys.argv[2])[1].lower() not in allowed_extensions:
            sys.exit("Invalid output")
        elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
            sys.exit("Input and output have different extensions")


def image_merging():
    try:
        input_image = Image.open(sys.argv[1])
        overlay_image = Image.open("shirt.png")
        output_image = sys.argv[2]

        # check for biggest side to resize picture
        # the second side ll be set up in 900px - more than enough to avoid changing of aspect ratio
        if input_image.width >= input_image.height:
            input_image.thumbnail((900, 600))
        elif input_image.width <= input_image.height:
            input_image.thumbnail((600, 900))
        # set up a box to crop image and crop it
        box = (input_image.width - 600, input_image.height - 700, input_image.width, input_image.height - 100)
        new_image = input_image.crop(box)
        # overlay pictures and save
        new_image.paste(overlay_image, overlay_image)
        new_image.save(output_image)

    except OSError:
        sys.exit("Input does not exist")


if __name__ == '__main__':
    main()
