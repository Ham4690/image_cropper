from setuptools import setup, find_packages

setup(
    name='image_cropper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow==8.3.2',
    ],
    entry_points={
        'console_scripts': [
            'image_cropper=image_cropper.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple image cropping utility',
    keywords='image cropping, automation',
    url='http://github.com/yourusername/image_cropper',  # replace with the URL of your project on GitHub or other repository
)
