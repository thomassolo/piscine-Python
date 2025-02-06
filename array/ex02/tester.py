from load_image import ft_load

try:
    print(ft_load("landscape.jpg"))
except (ValueError, FileNotFoundError) as e:
    print(e)
