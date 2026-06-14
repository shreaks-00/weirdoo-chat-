from PIL import Image
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    # If the pixel is very close to white, make it transparent
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save(output_path, "PNG")
print("Saved transparent image to", output_path)
