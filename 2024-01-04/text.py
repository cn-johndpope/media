import os
from PIL import Image

def remove_metadata(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith('.png'):  # Check if the file is a PNG
            file_path = os.path.join(directory, filename)
            try:
                # Open the image
                with Image.open(file_path) as img:
                    # Remove metadata by saving only the data
                    data = img.tobytes()
                    img_without_metadata = Image.frombytes(img.mode, img.size, data)
                    
                    # Save the new image over the old one
                    img_without_metadata.save(file_path, "PNG")
                    
                    print(f"Removed metadata from: {filename}")
            except Exception as e:
                print(f"Failed to remove metadata from {filename}. Reason: {e}")

# Replace 'your_directory_path_here' with the path to the directory containing your images
remove_metadata('.')
