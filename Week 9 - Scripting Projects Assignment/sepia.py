from images import Image

def grayscale(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b = image.getPixel(x, y)
            gray = int((r + g + b) / 3)
            image.setPixel(x, y, (gray, gray, gray))

def sepia(image):
    grayscale(image)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            red, green, blue = image.getPixel(x, y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
            image.setPixel(x, y, (red, green, blue))

if __name__ == "__main__":
    img = Image("smokey.gif")
    img.draw()
    sepia(img)
    img.draw()
