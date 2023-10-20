# image_cropper

`image_cropper`は、画像の中心を指定したサイズでトリミングする Python ツールです。このユーティリティは、大きな画像から特定のサイズで中央部分を切り取りたい場合に便利です。

## 前提条件

- Python 3.6 以上がインストールされていること。
- PIL（Python Imaging Library）またはそのフォークである Pillow がインストールされていること。

## インストール

このプロジェクトを使用するには、リポジトリをクローンし、必要な依存関係をインストールします。

```bash
git clone [リポジトリのURL]
cd image_cropper
pip install -r requirements.txt
```

## 使用方法

スクリプトはコマンドラインから直接、または Python プロジェクト内からプログラムとして実行することができます。

### コマンドライン

```bash
python image_cropper/main.py --image input/image.jpg --output output/cropped.jpg --size 1535 1024
```

### プログラム

```python
from image_cropper import cropper

cropper.crop_center("input/image.jpg", "output/cropped.jpg", (1535, 1024))
```

## 機能

- 指定されたピクセルサイズで画像の中心をトリミングします。
- トリミングした画像を指定された出力パスに保存します。

## コントリビューション

プルリクエストは歓迎します。大きな変更をする場合は、まず何を変更したいかを議論するために issue を開いてください。

## ライセンス

[MIT](https://choosealicense.com/licenses/mit/)
