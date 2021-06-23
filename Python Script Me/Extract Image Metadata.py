"""

 # How to Extract Image Metadata in Python
 # https://www.thepythoncode.com/article/extracting-image-metadata-in-python
 # 
"""
from PIL import Image
#import os
from PIL.ExifTags import TAGS

#imagename = ('D:/GitHub/Git_Me/20190223_092203583_iOS.jpg')  # path to the image or video
imagename = ('image.jpg')                                     # path to the image or video
image = Image.open(imagename)                                 # read the image data using PIL
exifdata = image.getexif()                                     # extract EXIF data
#print (exifdata)

# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:60}: {data}")
    
