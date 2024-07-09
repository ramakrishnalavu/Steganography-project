from PIL import Image

def encode_image(img, msg):
    # Ensure message is short enough
    length = len(msg)
    if length > 255:
        print("Message is too long!")
        return False

    # Ensure image is large enough
    width, height = img.size
    if width * height < length:
        print("Image is too small!")
        return False

    # Add length of message to front of message
    msg = chr(length) + msg

    # Convert message to binary
    b_message = ''.join([format(ord(i), "08b") for i in msg])
    
    # Get the pixels from the image
    pixels = list(img.getdata())
    
    # Change LSB of each pixel according to the binary message
    new_pixels = []
    index = 0
    for pixel in pixels:
        if index < len(b_message):
            new_pixel = (pixel[0] & ~1 | int(b_message[index]), pixel[1], pixel[2])
            index += 1
        else:
            new_pixel = pixel
        new_pixels.append(new_pixel)
    
    # Create a new image with the new pixels
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)
    
    return new_img

def decode_image(img):
    pixels = list(img.getdata())
    bits = ""
    
    for pixel in pixels:
        bits += str(pixel[0] & 1)
    
    # Convert bits to characters
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    
    # Extract the message length
    length = ord(chars[0])
    msg = ''.join(chars[1:length + 1])
    
    return msg

# Usage example
img = Image.open("input_image.png")
msg = "Hello, this is a hidden message!"

encoded_img = encode_image(img, msg)
if encoded_img:
    encoded_img.save("encoded_image.png")
    decoded_msg = decode_image(encoded_img)
    print(f"Decoded message: {decoded_msg}")