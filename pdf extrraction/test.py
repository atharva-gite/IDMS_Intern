# import fitz  # PyMuPDF
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import string
# import nltk
# from nltk.corpus import stopwords

# # Download NLTK resources if not already downloaded
# # nltk.download('stopwords')

# # Function to extract text from PDF


# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     text = ""
#     for page_num in range(len(doc)):
#         page = doc.load_page(page_num)
#         text += page.get_text()
#     return text

# # Function to preprocess text


# def preprocess_text(text):
#     # Remove punctuation
#     text = text.translate(str.maketrans('', '', string.punctuation))

#     # Convert to lowercase
#     text = text.lower()

#     # Tokenize (split into words)
#     words = text.split()

#     # Remove stopwords
#     stop_words = set(stopwords.words('english'))
#     words = [word for word in words if word not in stop_words]

#     # Join the words back into a single string
#     text = ' '.join(words)

#     return text

# # Function to calculate cosine similarity between two texts


# def calculate_cosine_similarity(text1, text2):
#     # Create TF-IDF Vectorizer
#     vectorizer = TfidfVectorizer()

#     # Fit and transform the texts
#     tfidf_matrix = vectorizer.fit_transform([text1, text2])

#     # Calculate cosine similarity
#     cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

#     return cosine_sim[0][0]


# # Paths to your PDFs
# pdf1_path = '3.pdf'
# pdf2_path = '4.pdf'

# # Extract text from PDFs
# text1 = extract_text_from_pdf(pdf1_path)
# text2 = extract_text_from_pdf(pdf2_path)

# # Preprocess text
# text1 = preprocess_text(text1)
# text2 = preprocess_text(text2)

# # Calculate cosine similarity
# cosine_similarity_score = calculate_cosine_similarity(text1, text2)

# print(f"Cosine Similarity between the two PDFs: {cosine_similarity_score}")
# # from PyPDF2 import PdfReader as pdr

# # reader=pdr("1.pdf")
# # pages=reader.pages[0]
# # output_text_path = 'extracted_text.txt'
# # with open(output_text_path, 'w', encoding='utf-8') as f:
# #     f.write(pages.extract_text(0))
# import PyPDF2
# import re
# from datetime import datetime

# def extract_text_from_pdf(pdf_path):
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ''
#         for page in reader.pages:
#             text += page.extract_text()
#     return text

# def parse_po_info(text):
#     po_info = {}

#     # Extract PO number
#     po_match = re.search(r'Purchase Order No\.\s*(\d+)', text)
#     if po_match:
#         po_info['po_number'] = po_match.group(1)

#     # Extract PO date
#     date_match = re.search(r'Dated\s*(\d{1,2}-[A-Za-z]+-\d{4})', text)
#     if date_match:
#         po_info['po_date'] = datetime.strptime(date_match.group(1), '%d-%B-%Y').date()

#     # Extract supplier info
#     supplier_match = re.search(r'Supplier\s*([\s\S]*?)(?=GST No\.)', text)
#     if supplier_match:
#         po_info['supplier'] = supplier_match.group(1).strip()

#     # Extract ship to address
#     ship_to_match = re.search(r'Ship To\s*([\s\S]*?)(?=STATE :)', text)
#     if ship_to_match:
#         po_info['ship_to'] = ship_to_match.group(1).strip()

#     # Extract line items
#     items_match = re.findall(r'(\d+)\s+(.*?)\s+(\d+)\s+(\d+(?:\.\d+)?)\s+(?:Pc|pc)\s+(\d+(?:,\d+)*(?:\.\d+)?)', text)
#     po_info['line_items'] = [
#         {
#             'sl_no': item[0],
#             'description': item[1],
#             'quantity': item[2],
#             'rate': item[3],
#             'amount': item[4].replace(',', '')
#         }
#         for item in items_match
#     ]

#     # Extract total amount
#     total_match = re.search(r'Total\s*Rs\s*([\d,]+)', text)
#     if total_match:
#         po_info['total_amount'] = total_match.group(1).replace(',', '')

#     # Extract payment terms
#     payment_terms_match = re.search(r'Payments Terms :(.*?)(?=\d\.)', text, re.DOTALL)
#     if payment_terms_match:
#         po_info['payment_terms'] = payment_terms_match.group(1).strip()

#     # Extract delivery schedule
#     delivery_match = re.search(r'Delivery / Schedule:(.*?)(?=\d\.)', text, re.DOTALL)
#     if delivery_match:
#         po_info['delivery_schedule'] = delivery_match.group(1).strip()

#     return po_info

# # Usage
# pdf_path = '1.pdf'
# pdf_text = extract_text_from_pdf(pdf_path)
# po_info = parse_po_info(pdf_text)

# # Print extracted information
# for key, value in po_info.items():
#     print(f"{key}: {value}")
import PyPDF2
import re
from datetime import datetime


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text


def parse_po_info(text):
    po_info = {}

    # Extract PO number and date
    po_number_match = re.search(r'PO No\s*:\s*(PS/\d{4}/\d{2}-\d{2})', text)
    date_match = re.search(r'Date\s*:\s*(\d{2}/\d{2}/\d{4})', text)
    if po_number_match and date_match:
        po_info['po_number'] = po_number_match.group(1).strip()
        date_str = date_match.group(1).strip()

        # Attempt to parse the date
        try:
            po_info['po_date'] = datetime.strptime(date_str, '%d/%m/%Y').date()
        except ValueError:
            po_info['po_date'] = None  # or handle appropriately

    # Extract supplier info
    supplier_match = re.search(
        r"Supplier's Name\s*:\s*([\s\S]*?)(?:\n|Email)", text)
    if supplier_match:
        po_info['supplier'] = supplier_match.group(1).strip()

    # Extract supplier GSTIN
    gstin_match = re.search(r'GSTIN\s*:\s*(\S+)', text)
    if gstin_match:
        po_info['supplier_gstin'] = gstin_match.group(1)

    # Extract delivery schedule
    delivery_match = re.search(
        r'Delivery Schedule\s*:\s*([\s\S]*?)(?:\n|Payment Terms)', text)
    if delivery_match:
        po_info['delivery_schedule'] = delivery_match.group(1).strip()

    # Extract payment terms
    payment_match = re.search(
        r'Payment Terms\s*:\s*([\s\S]*?)(?:\n|Dispatch Through)', text)
    if payment_match:
        po_info['payment_terms'] = payment_match.group(1).strip()

    # Extract line items
    items_pattern = re.compile(
        r'(\d+)\s+(.*?)\s+(\d{4})\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s+(NOS)\s+(\d+(?:\.\d+)?)')
    items_match = items_pattern.findall(text)
    po_info['line_items'] = [
        {
            'sr_no': item[0].strip(),
            'description': item[1].strip(),
            'hsn': item[2].strip(),
            'quantity': item[3].strip(),
            'rate': item[4].strip(),
            'unit': item[5].strip(),
            'amount': item[6].strip()
        }
        for item in items_match
    ]

    # Extract total amount
    total_match = re.search(r'Final Amount\s*:\s*([\d.]+)', text)
    if total_match:
        po_info['total_amount'] = total_match.group(1).strip()

    # Extract GST amount
    gst_match = re.search(r'Total GST Value \(In Word\)\s*:\s*(.*)', text)
    if gst_match:
        po_info['gst_amount_words'] = gst_match.group(1).strip()

    return po_info


# Usage
pdf_path = '2.pdf'
pdf_text = extract_text_from_pdf(pdf_path)
po_info = parse_po_info(pdf_text)

# Print extracted information
for key, value in po_info.items():
    print(f"{key}: {value}")
