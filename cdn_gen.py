import os
image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
thumb_dir = os.path.join(image_dir, 'thumbnails')
with open('index_cdn_image.txt', 'w') as index_file:
    for root, dirs, files in os.walk(thumb_dir):
        for file in files:
            index_file.write(file + '\n')
