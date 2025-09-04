# Bulk2AVIF

**Convert all photos in a folder to AVIF format using FFmpeg.**

## What it does

This script automatically finds all images in the current folder (PNG, JPG, JPEG, WebP, BMP, TIFF) and bulk converts them to AVIF format. Original images are automatically deleted after successful conversion.

AVIF is a modern format that offers up to 50% smaller file sizes than JPEG with better quality.

## Requirements

- **FFmpeg** installed on your system and in your PATH.
  - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt install ffmpeg` or `sudo yum install ffmpeg`

## Usage

1. Put `bulk2avif.py` in the folder with your photos
2. Run:
   ```bash
   python bulk2avif.py
   ```

**⚠️ WARNING:** Original images are automatically deleted after conversion. Backup if needed.

## Example

```
$ python bulk2avif.py
Converting 15 images to AVIF...
✓ photo1.jpg
✓ photo2.png  
✓ vacation.jpeg
✗ corrupted.png
```

Simple, fast, automatic.

## License
MIT License.