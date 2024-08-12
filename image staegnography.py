import cv2
import os

# Dictionaries to store character to integer and integer to character mappings
d = {}
c = {}

# Populate the dictionaries
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Load the image
x = cv2.imread(r"C:\Users\lavur\Downloads\bike.webp")

# Get the dimensions of the image
i = x.shape[0]
j = x.shape[1]
print("Image dimensions:", i, j)

# Get user inputs for the security key and the text to hide
key = input("Enter key to edit (Security Key): ")
text = input("Enter text to hide: ")

# Initialize variables
k1 = 0
tln = len(text)
z = 0  # decides plane
m = 0  # number of row
n = 0  # number of column

# Length of the text
l = len(text)

# Encode the text into the image
for i in range(l):
    x[n, m, z] = d[text[i]] ^ d[key[k1]]
    n += 1
    m += 1
    m = m % x.shape[1]  # Wrap around if m exceeds image width
    z = (z + 1) % 3  # Cycles through 0, 1, 2 for the RGB planes
    k1 = (k1 + 1) % len(key)  # Cycles through the key

# Save the encrypted image
cv2.imwrite(r"C:\Users\lavur\Downloads\bike.webp", x)
os.startfile(r"C:\Users\lavur\Downloads\bike.webp")
print("Data Hiding in Image completed successfully.")

# Option to extract data from the image
ch = int(input("\nEnter 1 to extract data from Image: "))

if ch == 1:
    key1 = input("\n\nRe-enter key to extract text: ")
    decrypt = ""

    if key == key1:
        # Reset variables for decryption
        k1 = 0
        z = 0
        m = 0
        n = 0
        
        for i in range(l):
            decrypted_char = c[x[n, m, z] ^ d[key[k1]]]  # Reverse the XOR operation
            decrypt += decrypted_char
            n += 1
            m += 1
            m = m % x.shape[1]
            z = (z + 1) % 3
            k1 = (k1 + 1) % len(key)
        
        print("Extracted text:", decrypt)
    else:
        print("Incorrect key! Decryption failed.")
else:
    print("Thank you. EXITING.")
