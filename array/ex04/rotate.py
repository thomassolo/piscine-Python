from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(data: np.ndarray):
    """
    Crops the center of the image to a 400x400 region and converts it to grayscale.
    
    Args:
        data: A 3D NumPy array representing the image.
    
    Returns:
        A 3D NumPy array of the grayscale cropped region (with shape (400, 400, 1)).
    """
    try:
        # Ensure the input is a proper 3D NumPy array
        if not isinstance(data, np.ndarray) or data.ndim != 3:
            raise ValueError("Invalid image format. Expected a 3D NumPy array.")

        # Get image dimensions
        height, width, _ = data.shape

        # Ensure the image is large enough
        if height < 400 or width < 400:
            raise ValueError("The image is too small to zoom to 400x400.")

        # Calculate the center coordinates
        center_y, center_x = height // 2, width // 2

        # Calculate crop boundaries
        start_y = center_y - 200
        start_x = center_x - 200
        end_y = center_y + 200
        end_x = center_x + 200

        # Extract the 400x400 cropped region
        zoomed = data[start_y:end_y, start_x:end_x]

        # Convert the region to grayscale using the mean of the RGB channels
        grayscale = np.mean(zoomed, axis=2, keepdims=True).astype(np.uint8)

        print("New shape after cropping:", grayscale.shape)
        # Optionally, you can comment out the next line if the full array output is too verbose:
        # print(grayscale)
        
        return grayscale

    except Exception as e:
        print(f"Error during zooming: {str(e)}")
        return None


def ft_rotate(data: np.ndarray):
    """
    Rotates an image by 90 degrees clockwise.
    
    Args:
        data: A NumPy array representing the image (either 2D or 3D).
    
    Returns:
        The rotated image as a NumPy array.
    """
    try:
        # Ensure the input is a NumPy array
        if not isinstance(data, np.ndarray):
            raise ValueError("Invalid image format. Expected a NumPy array.")

        # Handle grayscale images with an extra channel dimension
        if data.ndim == 3 and data.shape[2] == 1:
            squeezed = data.squeeze()
            transposed = squeezed.T
            rotated = np.flip(transposed, axis=1)
            rotated = np.expand_dims(rotated, axis=2)
        elif data.ndim == 3:
            transposed = np.transpose(data, (1, 0, 2))
            rotated = np.flip(transposed, axis=1)
        elif data.ndim == 2:
            transposed = data.T
            rotated = np.flip(transposed, axis=1)

        else:
            raise ValueError("Unsupported image dimensions. Expected a 2D or 3D array.")

        print("Original shape:", data.shape)
        print("Rotated shape:", rotated.shape)

        # Display the original and rotated images side by side
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        if data.ndim == 3 and data.shape[2] == 1:
            plt.imshow(data.squeeze(), cmap='gray')
        else:
            plt.imshow(data)
        plt.title('Original Image')

        plt.subplot(1, 2, 2)
        if rotated.ndim == 3 and rotated.shape[2] == 1:
            plt.imshow(rotated.squeeze(), cmap='gray')
        else:
            plt.imshow(rotated)
        plt.title('Rotated Image')

        plt.tight_layout()
        plt.show()

        return rotated

    except Exception as e:
        print(f"Error during rotation: {str(e)}")
        return None

def main():
    path = "animal.jpeg"
    data = ft_load(path)
    if data is None:
        print("Error: Image could not be loaded.")
        return

    # Crop and convert the image to grayscale
    zoomed = ft_zoom(data)
    
    # Rotate the zoomed image if the zoom was successful
    if zoomed is not None:
        ft_rotate(zoomed)

if __name__ == "__main__":
    main()
