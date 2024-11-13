import os
from PIL import Image

def create_thumbnails(source_dir, target_dir, thumbnail_size=(128, 128)):
    """
    Create thumbnails for all images in the source directory and save them to the target directory.
    """
    # Make sure target directory exists
    os.makedirs(target_dir, exist_ok=True)

    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # Check if it's a file and if it's an image
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    # Create the thumbnail
                    img.thumbnail(thumbnail_size)

                    # Save the thumbnail to the target directory
                    base, ext = os.path.splitext(filename)
                    thumb_filename = f"{base}_T{ext}"
                    thumb_path = os.path.join(target_dir, thumb_filename)
                    img.save(thumb_path)
                    #print(f"Thumbnail saved to: {thumb_path}")

            except Exception as e:
                print(f"Error processing file {filename}: {e}")