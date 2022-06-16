from time import sleep
import numpy
from matplotlib import pyplot as plt
import pytesseract
import screenshot

flyff_window_title = "Flyff Universe"

def main():
    while True:
        try:
            window = screenshot.get_window("Chrome")
            image = screenshot.take_screenshot(window)
            processed_image = screenshot.process_image(image, (0.55, 1, 0.2, 0.02), use_contour_inversion=True)
            text = screenshot.read_image_text(processed_image)
            print(text)
        except Exception as e:
            print(e)

        sleep(2)

if __name__ == "__main__":
    main()