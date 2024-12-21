from PIL import Image
from ForImages.image_processor import ImageProcessor

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        try:
            self.image = Image.open(self.image_path)
        except FileNotFoundError:
            print(f"Ошибка: Файл '{self.image_path}' не найден.")
            raise

    def resize_image(self, size=(300, 300)):
        self.image = self.image.resize(size)
        print(f"Размер картинки изменен на {size[0]}x{size[1]} пикселей.")

    def save_image(self, filename="output.png"):
        self.image.save(filename, "PNG")
        print(f"Картинка сохранена как {filename}.")

    def process_image(self):
        return ImageProcessor(self.image)
