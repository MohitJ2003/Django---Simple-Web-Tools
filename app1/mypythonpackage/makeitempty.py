import cv2
import pytesseract
import re

def extract_payment_history(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert image to grayscale for better OCR accuracy
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Extract text using Tesseract
    extracted_text = pytesseract.image_to_string(thresh)
    print(extracted_text)
    # Initialize a list to store transaction records
    transactions = []

    # Regex pattern to extract records (Example pattern for amount & transaction details)
    transaction_pattern = re.compile(r"(.+?)\n(Paid|Sent|Received) on (\d{1,2} \w{3}, \d{1,2}:\d{2} [AP]M)\n([-+₹\d.,]+)")

    for match in transaction_pattern.finditer(extracted_text):
        name, transaction_type, date_time, amount = match.groups()
        transactions.append({
            "Name": name.strip(),
            "Transaction Type": transaction_type.strip(),
            "Date & Time": date_time.strip(),
            "Amount": amount.strip()
        })

    return transactions

# Example usage
image_path = "D:\getPaytmPaymentRecords\paymentImages\IMG-20241005-WA0041.jpg"
transactions = extract_payment_history(image_path)
print(transactions)
# Print extracted transactions
for t in transactions:
    print(t)
            