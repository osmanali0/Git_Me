"""
 # How to Extract Image Metadata in Python
 # https://www.thepythoncode.com/article/extracting-image-metadata-in-python
 # https://github.com/python-pillow/Pillow/blob/master/src/PIL/ExifTags.py
 #
 # 
 #
 #
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
    
    """[
ExifVersion              : 0220
ShutterSpeedValue        : (406, 100)
ApertureValue            : (1851, 1000)       
DateTimeOriginal         : 2016:11:10 18:22:47
DateTimeDigitized        : 2016:11:10 18:22:47
BrightnessValue          : (-109, 100)        
ExposureBiasValue        : (0, 10)
MaxApertureValue         : (1851, 1000)       
MeteringMode             : 2
Flash                    : 0
FocalLength              : (220, 100)
UserComment              :
ColorSpace               : 1
ExifImageWidth           : 2592
FocalLengthIn35mmFilm    : 22
SceneCaptureType         : 0
ExifImageHeight          : 1944
ImageWidth               : 2592
ImageLength              : 1944
Make                     : samsung
Model                    : SM-G920F
Orientation              : 8
YCbCrPositioning         : 1
ExposureTime             : (1, 17)
XResolution              : (72, 1)
YResolution              : (72, 1)
FNumber                  : (19, 10)
FNumber                  : (19, 10)
ImageUniqueID            : B05LLHA01PM
ISOSpeedRatings          : 400
ISOSpeedRatings          : 400
ISOSpeedRatings          : 400
ISOSpeedRatings          : 400
ResolutionUnit           : 2
ExifOffset               : 226
ExposureMode             : 0
FlashPixVersion          : 0100
WhiteBalance             : 0
Software                 : G920FXXS4DPI4
DateTime                 : 2016:11:10 18:22:4
MakerNote                :       0100                      Z   @         P          
                                                           Z   @         P
    ]
    """