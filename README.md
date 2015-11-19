## Quaternary Image Encryption

Python implementation of http://ijns.jalaxy.com.tw/contents/ijns-v17-n3/ijns-2015-v17-n3-p322-327.pdf

## Dependencies

**Requires [Python 2.7](https://www.python.org/downloads/) and [Python Imaging Library (PIL)](http://www.pythonware.com/products/pil/)**
* `pip install --allow-external pil`

## Image
sample.jpg by Rijksdienst voor het Cultureel Erfgoed [CC BY-SA 3.0 nl](http://creativecommons.org/licenses/by-sa/3.0/nl/deed.en), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Overzicht_van_de_voorkant_-_Tungelroy_-_20421367_-_RCE.jpg)

## Usage
`main.py` can be run with or without a filename passed as an argument. If no arguments are passed, the user is prompted to enter a filename to process.
* `main.py sample.jpg`

## TODO
* Fix encryption method in rsa.py (rsa.RSA.encryptBaseFour() doesn't encrypt pixel values properly)
* Implement decryption algorithm
