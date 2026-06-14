from PIL import Image
import sys

img_path = sys.argv[1]
img = Image.open(img_path)

# Ensure it's in RGBA mode to get correct bounding box based on alpha
img = img.convert("RGBA")

# getbbox() finds the tightest bounding box of non-zero alpha pixels
bbox = img.getbbox()

if bbox:
    cropped_img = img.crop(bbox)
    # Favicons look best when square, so let's make it a square by padding the smaller side
    width, height = cropped_img.size
    max_dim = max(width, height)
    
    # Create a new transparent square image
    square_img = Image.new('RGBA', (max_dim, max_dim), (0, 0, 0, 0))
    
    # Paste the cropped image into the center
    offset = ((max_dim - width) // 2, (max_dim - height) // 2)
    square_img.paste(cropped_img, offset)
    
    square_img.save(img_path, "PNG")
    print(f"Cropped and squared successfully. New size: {max_dim}x{max_dim}")
else:
    print("Image is empty or fully transparent.")
