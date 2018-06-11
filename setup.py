from distutils.core import setup

setup(
    name="abcMiner",
    version='0.1.0',
    author="VulcanoAhab",
    packages=["abcMiner", "abcTraining"],
    url="https://github.com/VulcanoAhab/abcMiner.git",
    description="Browsers Utils",
    install_requires=[
        "opencv-python==3.4.1.15",
        "Pillow==5.1.0",
        "pytesseract==0.2.2",
        "numpy==1.14.3"
        ]
)
