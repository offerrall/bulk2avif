import subprocess
from pathlib import Path

def main():
    images = []
    for ext in ['.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff']:
        images.extend(Path.cwd().glob(f"*{ext}"))
        images.extend(Path.cwd().glob(f"*{ext.upper()}"))
    
    if not images:
        print("No images found")
        return
    
    print(f"Converting {len(images)} images to AVIF...")
    
    for img in images:
        avif_path = img.with_suffix('.avif')
        
        result = subprocess.run([
            'ffmpeg', '-i', str(img),
            '-c:v', 'libaom-av1', '-crf', '30',
            '-y', str(avif_path)
        ], capture_output=True)
        
        if result.returncode == 0:
            img.unlink()
            print(f"✓ {img.name}")
        else:
            print(f"✗ {img.name}")

if __name__ == "__main__":
    main()