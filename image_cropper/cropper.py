from PIL import Image

def crop_center(image_path, output_path, size):
    """
    画像の中心を指定されたサイズにトリミングします。

    :param image_path: 入力画像へのパス
    :param output_path: トリミングされた画像を保存するパス
    :param size: 新しいサイズのための(幅、高さ)のタプル
    """
    with Image.open(image_path) as img:
        img_width, img_height = img.size
        target_width, target_height = size

        # 画像のアスペクト比を維持しながら、指定されたサイズにリサイズ
        if img_width / img_height >= target_width / target_height:
            # 画像の幅がターゲットのアスペクト比よりも広い場合
            new_height = target_height
            new_width = int(img_width * (target_height / img_height))
        else:
            # 画像の高さがターゲットのアスペクト比よりも高い場合
            new_width = target_width
            new_height = int(img_height * (target_width / img_width))

        img = img.resize((new_width, new_height), Image.LANCZOS)

        # 新しいサイズでの画像の中心をトリミング
        left = (new_width - target_width) / 2
        top = (new_height - target_height) / 2
        right = (new_width + target_width) / 2
        bottom = (new_height + target_height) / 2

        img_cropped = img.crop((left, top, right, bottom))
        img_cropped.save(output_path)
