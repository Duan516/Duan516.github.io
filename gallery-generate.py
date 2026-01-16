import os
from PIL import Image
import re

def resize_image(input_path, output_path, scale_factor=0.25):
    """Resize image to a fraction of original size while maintaining aspect ratio."""
    with Image.open(input_path) as img:
        # Calculate new dimensions
        width, height = img.size
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        
        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Save the resized image
        resized_img.save(output_path, optimize=True, quality=85)

def process_shanghai_folder():
    folder_path = r'e:\personal website\6.0 20251214\Drawer-DSX\assets\img\gallery\2025\欧洲'
    
    try:
        files = os.listdir(folder_path)
        image_files = [f for f in files 
                      if re.search(r'\.(jpg|jpeg|png|gif)$', f, re.IGNORECASE) 
                      and '- 副本' not in f]
        
        # Create thumbnails (resized copies)
        for file in image_files:
            input_path = os.path.join(folder_path, file)
            name, ext = os.path.splitext(file)
            output_path = os.path.join(folder_path, f"{name} - 副本{ext}")
            
            # Create resized copy
            resize_image(input_path, output_path)
            print(f"Created thumbnail: {output_path}")
        
        html = ''
        count = 0
        
        for file in image_files:
            if count % 4 == 0:  # Start new row every 4 images
                if count > 0: 
                    html += '  </div>\n'  # Close previous row
                html += '  <div class="row">\n'
            
            # Get image dimensions
            full_path = os.path.join(folder_path, file)
            with Image.open(full_path) as img:
                width, height = img.size
            
            # Find matching thumbnail (format: name-副本.ext)
            name, ext = os.path.splitext(file)
            thumbnail = f"{name} - 副本{ext}"
            
            html += f"""    <div class="col-md-3 col-sm-6 mb-4">
      <a href="assets/img/gallery/2025/欧洲/{file}"
        data-pswp-width="{width}"
        data-pswp-height="{height}"
        target="_blank">
        <img src="assets/img/gallery/2025/欧洲/{thumbnail}" class="img-fluid" alt="" />
      </a>
    </div>
"""
            
            count += 1
        
        html += '  </div>'  # Close final row
        
        print('Generated HTML:')
        print(html)
        
        # Write to file
        with open('./generated-gallery.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print('\nOutput saved to generated-gallery.html')
        
    except Exception as err:
        print(f'Error processing folder: {err}')

if __name__ == "__main__":
    process_shanghai_folder()