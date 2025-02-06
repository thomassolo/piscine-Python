import matplotlib.image as mpimg
from numpy import array


def ft_load(path: str) -> array:
    if not path.endswith(('.jpg', '.jpeg')):
        raise ValueError("Error: File must be a .jpg or .png image")
    try:
        img = mpimg.imread(path)
        print("The shape of image is:", img.shape)
        return img
    except FileNotFoundError:
        raise FileNotFoundError("Error: File not found")
