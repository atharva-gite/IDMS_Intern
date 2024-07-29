# import PyPDF2
# import re


# def extract_po_information(pdf_path):
#     # Open the PDF file
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ""
#         for page_num in range(len(reader.pages)):
#             text += reader.pages[page_num].extract_text()

#     # Regular expressions to extract relevant information
#     po_no_pattern = re.compile(r'PO No\s*([^\n]+)')
#     date_pattern = re.compile(r'Date\s*([^\n]+)')
#     supplier_pattern = re.compile(r"Supplier's Name\s*:\s*([^\n]+)")
#     contact_person_pattern = re.compile(r'Contact Person\s*([^\n]+)')
#     email_pattern = re.compile(r'Email\s*([^\n]+)')
#     phone_pattern = re.compile(r'Phone No.\s*([^\n]+)')
#     description_pattern = re.compile(r'Description of Goods\s*([^\n]+)')
#     quantity_pattern = re.compile(r'Quantity\s*([^\n]+)')
#     delivery_date_pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
#     amount_pattern = re.compile(r'Final Amount\s*([^\n]+)')

#     # Extract the relevant information
#     po_no = po_no_pattern.search(text).group(
#         1).strip() if po_no_pattern.search(text) else ""
#     date = date_pattern.search(text).group(
#         1).strip() if date_pattern.search(text) else ""
#     supplier = supplier_pattern.search(text).group(
#         1).strip() if supplier_pattern.search(text) else ""
#     contact_person = contact_person_pattern.search(text).group(
#         1).strip() if contact_person_pattern.search(text) else ""
#     email = email_pattern.search(text).group(
#         1).strip() if email_pattern.search(text) else ""
#     phone = phone_pattern.search(text).group(
#         1).strip() if phone_pattern.search(text) else ""
#     description = description_pattern.search(text).group(
#         1).strip() if description_pattern.search(text) else ""
#     quantity = quantity_pattern.search(text).group(
#         1).strip() if quantity_pattern.search(text) else ""
#     delivery_date_match = delivery_date_pattern.search(text)
#     delivery_date = delivery_date_match.group(
#         0).strip() if delivery_date_match else ""
#     amount = amount_pattern.search(text).group(
#         1).strip() if amount_pattern.search(text) else ""

#     extracted_info = {
#         "PO No": po_no,
#         "Date": date,
#         "Supplier": supplier,
#         "Contact Person": contact_person,
#         "Email": email,
#         "Phone": phone,
#         "Description": description,
#         "Quantity": quantity,
#         "Delivery Date": delivery_date,
#         "Amount": amount
#     }

#     return extracted_info

# # Path to the PDF file
# pdf_path = 'path/to/2.pdf'

# # Extract information
# extracted_info = extract_po_information(pdf_path)
# print(extracted_info)

import pdfplumber
import re

def extract_po_information(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    # Print the extracted text for debugging purposes
    print(text)

    # Regular expressions to extract relevant information
    po_no_pattern = re.compile(r'PO No\s*PS/\d{4}/\d{2}-\d{2}')
    date_pattern = re.compile(r'D a t e\s*(\d{2}/\d{2}/\d{4})')
    supplier_pattern = re.compile(r"Supplier's Name\s*:\s*(.*)")
    consignor_pattern = re.compile(r"Consignor's Name\s*:\s*(.*)")
    contact_person_pattern = re.compile(r'Contact Person\s*(.*)')
    email_pattern = re.compile(r'Email\s*:\s*(.*)')
    phone_pattern = re.compile(r'Phone No.\s*:\s*(.*)')
    description_pattern = re.compile(r'Description of Goods\s*(.*)')
    quantity_pattern = re.compile(r'Quantity\s*(\d+.\d+)')
    delivery_date_pattern = re.compile(r'Delivery Schedule \\Dt\.\s*(\d{1,2}\w{2}\s\w+,?\s?\d{4})')
    amount_pattern = re.compile(r'Final Amount\s*:\s*(\d+.\d+)')
    address_pattern = re.compile(r'UNIT NO\.G-1A,\s*(.*)', re.DOTALL)
    line_items_pattern = re.compile(r'(\d+)\s+(.*?)(?:\d{2}-\d{2}-\d{4})?\s+(\d+)\s+(\d+\.\d{2})\s+(\d+\.\d{2})\s+\d+\.\d{2}\s+\d+\.\d{2}\s+\d+\.\d{2}', re.DOTALL)
    
    # Extract the relevant information
    po_no = po_no_pattern.search(text).group(0).strip() if po_no_pattern.search(text) else ""
    date = date_pattern.search(text).group(1).strip() if date_pattern.search(text) else ""
    supplier = supplier_pattern.search(text).group(1).strip() if supplier_pattern.search(text) else ""
    consignor = consignor_pattern.search(text).group(1).strip() if consignor_pattern.search(text) else ""
    contact_person = contact_person_pattern.search(text).group(1).strip() if contact_person_pattern.search(text) else ""
    email = email_pattern.search(text).group(1).strip() if email_pattern.search(text) else ""
    phone = phone_pattern.search(text).group(1).strip() if phone_pattern.search(text) else ""
    description = description_pattern.search(text).group(1).strip() if description_pattern.search(text) else ""
    quantity = quantity_pattern.search(text).group(1).strip() if quantity_pattern.search(text) else ""
    delivery_date = delivery_date_pattern.search(text).group(1).strip() if delivery_date_pattern.search(text) else ""
    amount = amount_pattern.search(text).group(1).strip() if amount_pattern.search(text) else ""
    address = address_pattern.search(text).group(1).strip() if address_pattern.search(text) else ""
    line_items = line_items_pattern.findall(text)
    
    extracted_info = {
        "PO No": po_no,
        "Date": date,
        "Supplier": supplier,
        "Consignor": consignor,
        "Contact Person": contact_person,
        "Email": email,
        "Phone": phone,
        "Description": description,
        "Quantity": quantity,
        "Delivery Date": delivery_date,
        "Amount": amount,
        "Address": address,
        "Line Items": line_items
    }

    return extracted_info

# # Path to the PDF file
# pdf_path = '/mnt/data/2.pdf'

# # Extract information
# extracted_info = extract_po_information(pdf_path)
# print(extracted_info)
