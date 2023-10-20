import sys
from .cropper import crop_center

def main():
    if len(sys.argv) != 4:
        print("Usage: python -m image_cropper.main [path_to_image] [output_path] [size]")
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = sys.argv[2]
    size = tuple(map(int, sys.argv[3].split('x')))  # Convert "1535x1024" to (1535, 1024)

    crop_center(image_path, output_path, size)

if __name__ == "__main__":
    main()
