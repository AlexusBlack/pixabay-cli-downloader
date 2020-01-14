# pixabay-cli-downloader
Command line interface to download images from pixabay. Based on momozor / python-pixabay.

*WARNING* Pixabay does not allow systematic mass download.

## Installation
```
git clone https://github.com/AlexusBlack/pixabay-cli-downloader.git
pip install python-pixabay
```

## Usage
```
usage: pixabay-cli.py [-h] -k API_KEY [-q QUERY]
                      [-l {cs,da,de,en,es,fr,id,it,hu,nl,no,pl,pt,ro,sk,fi,sv,tr,vi,th,bg,ru,el,ja,ko,zh}]
                      [-t {all,photo,illustration,vector}]
                      [--orientation {all,horizontal,vertical}]
                      [-c {fashion,nature,backgrounds,science,education,people,feelings,religion,health,places,animals,industry,food,computer,sports,transportation,travel,buildings,business,music}]
                      [--min-width MIN_WIDTH] [--min-height MIN_HEIGHT]
                      [--colors [{grayscale,transparent,red,orange,yellow,green,turquoise,blue,lilac,pink,white,gray,black,brown} [{grayscale,transparent,red,orange,yellow,green,turquoise,blue,lilac,pink,white,gray,black,brown} ...]]]
                      [--editors] [--safe] [-o {popular,latest}] [-p PAGE]
                      [--per-page PER_PAGE]
                      path

Parser for Pixabay CLI

positional arguments:
  path                  Path to save images

optional arguments:
  -h, --help            show this help message and exit
  -k API_KEY, --api-key API_KEY
                        Your Pixabay API key
  -q QUERY, --query QUERY
                        Search query
  -l {cs,da,de,en,es,fr,id,it,hu,nl,no,pl,pt,ro,sk,fi,sv,tr,vi,th,bg,ru,el,ja,ko,zh}, --lang {cs,da,de,en,es,fr,id,it,hu,nl,no,pl,pt,ro,sk,fi,sv,tr,vi,th,bg,ru,el,ja,ko,zh}
                        Search language
  -t {all,photo,illustration,vector}, --image_type {all,photo,illustration,vector}
                        Images type
  --orientation {all,horizontal,vertical}
                        Images orientation
  -c {fashion,nature,backgrounds,science,education,people,feelings,religion,health,places,animals,industry,food,computer,sports,transportation,travel,buildings,business,music}, --category {fashion,nature,backgrounds,science,education,people,feelings,religion,health,places,animals,industry,food,computer,sports,transportation,travel,buildings,business,music}
                        Images category
  --min-width MIN_WIDTH
                        Min image width in pixels
  --min-height MIN_HEIGHT
                        Min image height in pixels
  --colors [{grayscale,transparent,red,orange,yellow,green,turquoise,blue,lilac,pink,white,gray,black,brown} [{grayscale,transparent,red,orange,yellow,green,turquoise,blue,lilac,pink,white,gray,black,brown} ...]]
                        Image colors
  --editors             Images must be editors choice
  --safe                Images must be suitable for all ages
  -o {popular,latest}, --order {popular,latest}
                        Order images by popular or latest
  -p PAGE, --page PAGE  Page of the request
  --per-page PER_PAGE   Number of images per page
```
