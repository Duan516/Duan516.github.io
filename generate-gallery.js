// generate-gallery.js
const fs = require('fs').promises;
const path = require('path');
const imageSize = require('image-size');  // Correct way to import image-size

async function processShanghaiFolder() {
    // Update the path to match your actual folder location
    const folderPath = 'e:/personal website/6.0 20251214/Drawer-DSX/assets/img/gallery/2025/上海';
    
    try {
        const files = await fs.readdir(folderPath);
        const imageFiles = files.filter(file => 
            /\.(jpg|jpeg|png|gif)$/i.test(file) && 
            !file.includes('-副本')  // Exclude thumbnails
        );
        
        let html = '';
        let count = 0;
        
        for (const file of imageFiles) {
            if (count % 4 === 0) {  // Start new row every 4 images
                if (count > 0) html += '  </div>\n';  // Close previous row
                html += '  <div class="row">\n';
            }
            
            const fullPath = path.join(folderPath, file).replace(/\\/g, '/');
            const dimensions = imageSize(fullPath);  // Use imageSize instead of sizeOf
            
            // Find matching thumbnail (assuming format: name-副本.ext)
            const ext = path.extname(file);
            const baseName = path.basename(file, ext);
            const thumbnail = `${baseName}-副本${ext}`;
            
            html += `    <div class="col-md-3 col-sm-6 mb-4">
      <a href="assets/img/gallery/2025/上海/${file}"
        data-pswp-width="${dimensions.width}"
        data-pswp-height="${dimensions.height}"
        target="_blank">
        <img src="assets/img/gallery/2025/上海/${thumbnail}" class="img-fluid" alt="" />
      </a>
    </div>\n`;
            
            count++;
        }
        
        html += '  </div>';  // Close final row
        
        console.log('Generated HTML:');
        console.log(html);
        
        // Optionally write to file
        await fs.writeFile('./generated-gallery.html', html);
        console.log('\nOutput saved to generated-gallery.html');
        
    } catch (err) {
        console.error('Error processing folder:', err.message);
    }
}

processShanghaiFolder();