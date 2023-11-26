import os
import re

from PIL import Image


class ImageProcessor:
    def __init__(self, path, width, height):
        self.width = width
        self.height = height
        self.processing_errors_counter = 0
        self.unknown_errors_counter = 0
        self.path = path
        self.img_extension = None
        self.temp_path = None

    def resize_images(self):
        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.endswith(('.jpg', '.jpeg', '.JPG', '.png', '.gif')):
                    self.img_extension = re.search(
                        r'\.([a-zA-Z]+)$', filename).group(1)
                    self.path = os.path.join(root, filename)
                    try:
                        with Image.open(self.path) as img:
                            self.create_copy()
                            error = self.exceptions_handler(img)
                        if not error:
                            os.replace(self.temp_path, self.path)
                        continue
                    except Exception as e:
                        self.unknown_errors_counter += 1
                        print(f"An UNKNOWN ERROR occurred processing {
                              self.path}: {e}")
                        continue
        print(f"Done! Process ended with {self.processing_errors_counter} processing errors and {
              self.unknown_errors_counter} unknown errors.")

    def create_copy(self):
        self.temp_path = self.path + f".temp.{self.img_extension}"

    def exceptions_handler(self, img):
        try:
            self.process_image(img)
            return False
        except Exception as e:
            self.processing_errors_counter += 1
            print(f"A PROCESSING ERROR occurred with {self.path}: {e}")
            return True

    def process_image(self, img):
        print(f"Resizing {self.path}...")
        width, height = img.size
        max_width = self.width if width > height else self.height
        max_height = max_width * height // width
        img.thumbnail((max_width, max_height))
        img.save(self.temp_path)


if __name__ == "__main__":
    path = input("Copy the folder path here: ")
    width = int(input("Choose MAX WIDTH: "))
    height = int(input("Chose MAX HEIGHT: "))
    ImageProcessor(path, width, height).resize_images()
