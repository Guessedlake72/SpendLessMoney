# SpendLessMoney
uses OCR to convert sainsbury's receipts into csv documents. I have a problem of shopping for food way too often, without knowing where my money went. This is hopefully a way to help fix that problem by tracking my receipts by week. In the future, I will add a webscraper portion that queries the sainsbury's website to tell what category of product each item is (ie. food, drinks, household essentials)

Uses:
 - pytesseract
 - numpy
 - will be adding scrapy later

## Usage
install the required libraries, and when you want to add a receipt into this week's csv, just run this line
python3 ocr.py --image receipt.jpg

receipt.jpg is a picture of the receipt

## Gallery
### Original receipt
![Original receipt](/images/receipt.jpg)
### Terminal Screenshot
![terminal](/images/terminal.png)
### Csv File
![output](/images/output.png)

## Other Info
Some example code when learning to use pytesseract is still in the code, maybe i'll clean that up later.
https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
