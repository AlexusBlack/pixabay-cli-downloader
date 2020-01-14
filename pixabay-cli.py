import argparse
import os
import requests
from pixabay import Image

def parse_arguments():
    parser = argparse.ArgumentParser(description="Parser for Pixabay CLI")
    parser.add_argument("-k", "--api-key", type=str, required=True,
            help="Your Pixabay API key")
    parser.add_argument("-q", "--query", type=str,
            default="",
            help="Search query")
    parser.add_argument("-l", "--lang", type=str,
            choices=["cs", "da", "de", "en", "es", "fr", "id", "it", "hu", "nl", "no", "pl", "pt", "ro", "sk", "fi", "sv", "tr", "vi", "th", "bg", "ru", "el", "ja", "ko", "zh"],
            default="en",
            help="Search language")
    parser.add_argument("-t", "--image_type", type=str,
            choices=["all", "photo", "illustration", "vector"],
            default="all",
            help="Images type")
    parser.add_argument("--orientation", type=str,
            choices=["all", "horizontal", "vertical"],
            default="all",
            help="Images orientation")
    parser.add_argument("-c", "--category", type=str,
            choices=["fashion", "nature", "backgrounds", "science", "education", "people", "feelings", "religion", "health", "places", "animals", "industry", "food", "computer", "sports", "transportation", "travel", "buildings", "business", "music"],
            default="",
            help="Images category")
    parser.add_argument("--min-width", type=int,
            default=0,
            help="Min image width in pixels")
    parser.add_argument("--min-height", type=int,
            default=0,
            help="Min image height in pixels")
    parser.add_argument("--colors", type=str, nargs="*",
            choices=["grayscale", "transparent", "red", "orange", "yellow", "green", "turquoise", "blue", "lilac", "pink", "white", "gray", "black", "brown"],
            default="",
            help="Image colors")
    parser.add_argument("--editors", action="store_true",
            help="Images must be editors choice")
    parser.add_argument("--safe", action="store_true",
            help="Images must be suitable for all ages")
    parser.add_argument("-o", "--order", type=str,
            choices=["popular", "latest"],
            default="popular",
            help="Order images by popular or latest")
    parser.add_argument("-p", "--page", type=int,
            #choices=range(1,999),
            default=1,
            help="Page of the request")
    parser.add_argument("--per-page", type=int,
            #choices=range(3, 200),
            default=20,
            help="Number of images per page")
    parser.add_argument("path", type=str,
            help="Path to save images")



    args = parser.parse_args()
    if not os.path.isdir(args.path):
        print("Please specify output path")
        exit(1)

    return args

def save_to_file(content, path):
    with open(path, 'wb') as f:
        f.write(content)

def main():
    args = parse_arguments()
    image = Image(args.api_key)

    print("Requesting images...")
    result = image.search(
            q = args.query,
            lang = args.lang,
            image_type = args.image_type,
            orientation = args.orientation,
            category = args.category,
            min_width = args.min_width,
            min_height = args.min_height,
            colors = ",".join(args.colors),
            editors_choice = "true" if args.editors else "false",
            safesearch = "true" if args.safe else "false",
            order = args.order,
            page = args.page,
            per_page = args.per_page
    )

    print("Found {} images, downloading...".format(len(result["hits"])))

    # download images to a specific folder, name as ID
    for image in result["hits"]:
        r = requests.get(image["largeImageURL"], headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        })
        save_to_file(r.content, args.path + "/" + str(image["id"]) + ".jpg")



main()

