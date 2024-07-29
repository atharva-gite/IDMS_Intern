import fitz  # PyMuPDF
import re

def safe_search(pattern, text, group=1, default=""):
    match = re.search(pattern, text)
    if match:
        return match.group(group).strip()
    return default

def extract_information_from_pdf(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""

    # Extract text from each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    # Extract information using regular expressions
    po_no = safe_search(r'PO No\s*(.*)', text)
    date = safe_search(r'Date\s*(.*)', text)

    supplier_name = safe_search(r'Supplier\'s Name\s*:\s*(.*)', text)
    supplier_gstin = safe_search(r'GSTIN\s*:\s*(\S+)', text)
    supplier_address = safe_search(r'UNIT NO\.[\s\S]+?421302 MUMBAI', text)
    supplier_email = safe_search(r'Email\s*(\S+)', text)
    supplier_phone = safe_search(r'Phone No\.\s*([\d\s/]+)', text)
    supplier_contact_person = safe_search(r'Contact Person\s*(.*)', text)

    consignor_name = safe_search(r'Consignor\'s Name\s*:\s*(.*)', text)
    consignor_gstin = safe_search(r'GSTIN\s*:\s*(\S+)', text)
    consignor_address = safe_search(r'850/3, G.I.D.C., MAKARPURA VADODARA 390010', text)
    consignor_phone = safe_search(r'Phone\s*:\s*([\d\s+-]+)', text)
    consignor_email = safe_search(r'Email\s*(\S+)', text)
    consignor_website = safe_search(r'Web-Site\s*:\s*(\S+)', text)
    consignor_pan_no = safe_search(r'Pan No\.\s*(\S+)', text)
    consignor_cin_no = safe_search(r'CIN No\.\s*(\S+)', text)

    line_items_match = re.findall(r'\d+\.\d+\s+\d+\.\d+\s+\d+\.\d+\s+\d+\.\d+\s+([\s\S]+?)\d{2}-\d{2}-\d{4}', text)
    line_items = []
    for item in line_items_match:
        item_details = re.split(r'\s{2,}', item)
        if len(item_details) >= 5:
            line_items.append({
                "description": item_details[0].strip(),
                "hsn": item_details[1].strip(),
                "quantity": float(item_details[2].strip()),
                "unit": item_details[3].strip(),
                "rate": float(item_details[4].strip()),
                "amount": float(item_details[5].strip())
            })

    cgst = safe_search(r'CGST Amt\s*(\d+\.\d+)', text)
    sgst = safe_search(r'SGST Amt\s*(\d+\.\d+)', text)
    igst = safe_search(r'IGST Amt\s*(\d+\.\d+)', text)
    total_tax = float(cgst) + float(sgst) + float(igst)

    total_amount = safe_search(r'Gross Total\s*(\d+\.\d+)', text)
    total_quantity = safe_search(r'Total Qty\s*(\d+\.\d+)', text)

    terms = re.findall(r'Terms\s*:\s*(\d\..+)', text)

    amount_in_words = safe_search(r'Total Invoice Value \(In Word\)\s*:\s*([\s\S]+?)\n', text)
    total_gst_in_words = safe_search(r'Total GST Value \(In Word\)\s*:\s*([\s\S]+?)\n', text)

    delivery_schedule = safe_search(r'Delivery Schedule\s*:\s*([\s\S]+?)(?=\n)', text)
    payment_terms = safe_search(r'Payment Terms\s*:\s*([\s\S]+?)(?=\n)', text)
    dispatch_through = safe_search(r'Dispatch Through\s*:\s*([\s\S]+?)(?=\n)', text)
    quotation_ref_no = safe_search(r'Quotation Ref. No.\s*:\s*([\s\S]+?)(?=\n)', text)

    data = {
        "purchase_order": {
            "po_no": po_no,
            "date": date
        },
        "supplier": {
            "name": supplier_name,
            "gstin": supplier_gstin,
            "address": supplier_address,
            "email": supplier_email,
            "phone": supplier_phone,
            "contact_person": supplier_contact_person
        },
        "consignor": {
            "name": consignor_name,
            "gstin": consignor_gstin,
            "address": consignor_address,
            "phone": consignor_phone,
            "email": consignor_email,
            "website": consignor_website,
            "pan_no": consignor_pan_no,
            "cin_no": consignor_cin_no
        },
        "line_items": line_items,
        "taxes": {
            "cgst": float(cgst),
            "sgst": float(sgst),
            "igst": float(igst),
            "total_tax": total_tax
        },
        "totals": {
            "taxable_amount": float(total_amount) - total_tax,
            "total_amount": float(total_amount),
            "total_quantity": float(total_quantity),
            "gross_total": float(total_amount)
        },
        "terms": terms,
        "amount_in_words": {
            "total_invoice_value": amount_in_words,
            "total_gst_value": total_gst_in_words
        },
        "delivery_schedule": delivery_schedule,
        "payment_terms": payment_terms,
        "dispatch_through": dispatch_through,
        "quotation_ref_no": quotation_ref_no
    }

    return data

# Example usage:
pdf_path = '2.pdf'
data = extract_information_from_pdf(pdf_path)
print(data)
