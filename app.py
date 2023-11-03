import os
import re

from PIL import Image


def resize_image(path):
    errors_counter = 0
    for filename in os.listdir(path):
        if filename.endswith(('.jpg', '.jpeg', '.JPG', '.png', '.gif')):
            image_path = os.path.join(path, filename)
            try:
                img = Image.open(image_path)

                width, height = img.size
                max_width = 800 if width > height else 600
                max_height = max_width * height // width

                img.thumbnail((max_width, max_height))
                print(f"Resizing {filename}...")
                img.save(image_path)
            except Exception as e:
                errors_counter += 1
                print(f"Error processing {filename}: {str(e)}")
                continue
    print(f"Done! Proccess ended with {errors_counter} errors.")


class ImageProcessor:
    def __init__(self, path):
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
        max_width = 800 if width > height else 600
        max_height = max_width * height // width
        img.thumbnail((max_width, max_height))
        img.save(self.temp_path)


if __name__ == "__main__":
    path = input("Copy the folder path here: ")
    # resize_images(path)
    ImageProcessor(path).resize_images()
