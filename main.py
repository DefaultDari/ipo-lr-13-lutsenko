from ForImages.image_handler import ImageHandler

def main():
    image_path = input("Введите полное название картинки (Например, image.jpg): ")
    try:
        handler = ImageHandler(f"Images/{image_path}")

        handler.resize_image()
        handler.save_image()

        processor = handler.process_image()
        processor.blur_image()
        processor.add_text()

        processor.image.show()
        processor.image.save("processed_image.png")
        print("Обработанная картинка сохранена как 'processed_image.png'.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
