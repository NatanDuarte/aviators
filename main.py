from unsplash import UnsplashAPI
from utils import apply_kmeans, save

CUSTOM_ARGS = 'jet'

def main():
    try:
        image = UnsplashAPI().fetch_random_image(CUSTOM_ARGS)
    except:
        print("An error ocurred. Couldn't fetch image.")
        exit(1)

    final_image = apply_kmeans(image)

    save(final_image)


main()
