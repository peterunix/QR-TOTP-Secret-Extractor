from PIL import Image
from pyzbar.pyzbar import decode
from urllib.parse import urlparse, parse_qs
import os


def get_valid_image_file():
    while True:
        filepath = input("Enter the path to a TOTP PNG or JPG file: ").strip()
        if not os.path.isfile(filepath):
            print("That file doesn't exist. Try again.")
            continue
        if not (filepath.lower().endswith('.png') or filepath.lower().endswith('.jpg') or filepath.lower().endswith('.jpeg')):
            print("That file is not a .png or .jpg. Try again.")
            continue

        return filepath



# Prompt for image path
filename = get_valid_image_file()

# Loading the QR code image
img = Image.open(filename)

# Decode the image
decoded = decode(img)
if not decoded:
    print("No QR code found.")
else:
    data = decoded[0].data.decode("utf-8")
    print("TOTP URI:", data)

    # Parsing and returning the secret key
    parsed = urlparse(data)
    params = parse_qs(parsed.query)
    secret = params.get('secret', [None])[0]
    print("Secret key:", secret)
