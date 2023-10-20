from PIL import Image

def crop_center(image_path, output_path, size):
    """
    画像の中心を指定されたサイズにトリミングします。

    :param image_path: 入力画像へのパス
    :param output_path: トリミングされた画像を保存するパス
    :param size: 新しいサイズのための(幅、高さ)のタプル
    """
    with Image.open(image_path) as img:
        width, height = img.size
        new_width, new_height = size

        left = (width - new_width)/2
        top = (height - new_height)/2
        right = (width + new_width)/2
        bottom = (height + new_height)/2

        # Crop the center of the image
        img_cropped = img.crop((left, top, right, bottom))
        img_cropped.save(output_path)
