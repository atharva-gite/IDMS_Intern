import re
from datetime import datetime
import json
import PyPDF2

def extract_info(document_content):
    def safe_search(pattern, content):
        match = re.search(pattern, content)
        return match.group(1) if match else None

    # Extract basic information
    po_number = safe_search(r'PO\. No\.\s+(\w+)', document_content)
    po_date = safe_search(r'Date\s+(\d{2}/\d{2}/\d{4})', document_content)
    if po_date:
        po_date = datetime.strptime(po_date, '%d/%m/%Y').strftime('%Y-%m-%d')

    # Extract vendor information
    vendor_name = safe_search(r'M/S : (.+)', document_content)
    vendor_address = safe_search(r'Address :\s+(.*?)(?=GST No\.)', document_content)
    if vendor_address:
        vendor_address = vendor_address.strip()
    vendor_gst = safe_search(r'GST No\.\s+(\w+)', document_content)

    # Extract ship to information
    ship_to_name = safe_search(r'SHIP TO\s+M/S : (.+)', document_content)
    ship_to_address = safe_search(r'SHIP TO.*?Address :\s+(.*?)(?=GST No\.)', document_content)
    if ship_to_address:
        ship_to_address = ship_to_address.strip()
    ship_to_gst = safe_search(r'SHIP TO.*?GST No\.\s+(\w+)', document_content)

    # Extract line items
    items = []
    for match in re.finditer(r'(\d+)\s+(.*?)\s+(\w+)\s+(\d+\.\d+)\s+(\d+)\s+Nos\.\s+(\d+\.\d+)\s+(\d+,\d+\.\d+)', document_content):
        items.append({
            'sr_no': match.group(1),
            'product_name': match.group(2),
            'item_code': match.group(3),
            'quantity': match.group(4),
            'hsn_no': match.group(5),
            'rate': match.group(6),
            'amount': match.group(7).replace(',', '')
        })

    # Extract totals
    sub_total = safe_search(r'Sub-Total\s+([\d,]+\.\d+)', document_content)
    if sub_total:
        sub_total = sub_total.replace(',', '')
    cgst = safe_search(r'CGST\s+([\d,]+\.\d+)', document_content)
    if cgst:
        cgst = cgst.replace(',', '')
    sgst = safe_search(r'SGST\s+([\d,]+\.\d+)', document_content)
    if sgst:
        sgst = sgst.replace(',', '')
    grand_total = safe_search(r'Grand Total\s+([\d,]+\.\d+)', document_content)
    if grand_total:
        grand_total = grand_total.replace(',', '')

    return {
        'po_number': po_number,
        'po_date': po_date,
        'vendor': {
            'name': vendor_name,
            'address': vendor_address,
            'gst': vendor_gst
        },
        'ship_to': {
            'name': ship_to_name,
            'address': ship_to_address,
            'gst': ship_to_gst
        },
        'items': items,
        'sub_total': sub_total,
        'cgst': cgst,
        'sgst': sgst,
        'grand_total': grand_total
    }

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Usage
pdf_path = '6.pdf'
document_content = extract_text_from_pdf(pdf_path)
extracted_info = extract_info(document_content)

# Print extracted information
print(json.dumps(extracted_info, indent=2))
