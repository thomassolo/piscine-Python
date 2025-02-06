from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(data: np.ndarray):
    try:
        # Ensure image is valid
        if not isinstance(data, np.ndarray) or data.ndim != 3:
            raise ValueError("Invalid image format. Expected a 3D NumPy array.")

        # Get image size
        height, width, _ = data.shape

        # Ensure the image is large enough for a 400x400 crop
        if height < 400 or width < 400:
            raise ValueError("The image is too small to zoom to 400x400.")

        # Calculate the exact center
        center_y, center_x = height // 2, width // 2

        # Ensure cropping does not exceed the image boundaries
        start_y = center_y - 200
        start_x = center_x - 200
        end_y = center_y + 200
        end_x = center_x + 200

        # Extract the zoomed region
        zoomed = data[start_y:end_y, start_x:end_x]

        # Convert to grayscale using the mean of RGB channels
        grayscale = np.mean(zoomed, axis=2, keepdims=True).astype(np.uint8)

        print("New shape after slicing:", grayscale.shape)
        print(grayscale)  # Ensure correct format output

        # Display images
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.imshow(data)
        plt.title('Original Image')

        plt.subplot(1, 2, 2)
        plt.imshow(grayscale.squeeze(), cmap='gray')
        plt.title('Zoomed Grayscale Image')

        plt.show()

        return grayscale

    except Exception as e:
        print(f"Error during zooming: {str(e)}")
        return None


def main():
    path = "animal.jpeg"
    data = ft_load(path)
    print(data)
    if data is None:
        print("Error: Image could not be loaded.")
        return

    ft_zoom(data)


if __name__ == "__main__":
    main()
