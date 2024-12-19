from ForImages.image_handler import ImageHandler

def main():
    image_path = input("Enter the path to the image (e.g., images/image.jpg): ")
    try:
        handler = ImageHandler(image_path)

        handler.resize_image()
        handler.save_image()

        processor = handler.process_image()
        processor.blur_image()
        processor.add_text()

        processor.image.show()
        processor.image.save("processed_image.png")
        print("Processed image saved as 'processed_image.png'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()