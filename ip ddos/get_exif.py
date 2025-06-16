import sys
from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open(sys.argv[1])
exif = img._getexif()
if not exif:
    print("Ingen EXIF-data")
else:
    for tag, val in exif.items():
        name = TAGS.get(tag, tag)
        print(f"{name}: {val}")
