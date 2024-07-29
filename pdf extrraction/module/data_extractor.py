def extractor(input_pdf_path, template):
    import PyPDF2
    import re
    from datetime import datetime
    if template == 1:
        def extract_text_from_pdf(pdf_path):
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text()
            return text

        def parse_po_info(text):
            po_info = {}

            # Extract PO number
            po_match = re.search(r'Purchase Order No\.\s*(\d+)', text)
            if po_match:
                po_info['po_number'] = po_match.group(1)

            # Extract PO date
            date_match = re.search(r'Dated\s*(\d{1,2}-[A-Za-z]+-\d{4})', text)
            if date_match:
                po_info['po_date'] = datetime.strptime(
                    date_match.group(1), '%d-%B-%Y').date()

            # Extract supplier info
            supplier_match = re.search(
                r'Supplier\s*([\s\S]*?)(?=GST No\.)', text)
            if supplier_match:
                po_info['supplier'] = supplier_match.group(1).strip()

            # Extract ship to address
            ship_to_match = re.search(r'Ship To\s*([\s\S]*?)(?=STATE :)', text)
            if ship_to_match:
                po_info['ship_to'] = ship_to_match.group(1).strip()

            # Extract line items
            items_match = re.findall(
                r'(\d+)\s+(.*?)\s+(\d+)\s+(\d+(?:\.\d+)?)\s+(?:Pc|pc)\s+(\d+(?:,\d+)*(?:\.\d+)?)', text)
            po_info['line_items'] = [
                {
                    'sl_no': item[0],
                    'description': item[1],
                    'quantity': item[2],
                    'rate': item[3],
                    'amount': item[4].replace(',', '')
                }
                for item in items_match
            ]

            # Extract total amount
            total_match = re.search(r'Total\s*Rs\s*([\d,]+)', text)
            if total_match:
                po_info['total_amount'] = total_match.group(1).replace(',', '')

            # Extract payment terms
            payment_terms_match = re.search(
                r'Payments Terms :(.*?)(?=\d\.)', text, re.DOTALL)
            if payment_terms_match:
                po_info['payment_terms'] = payment_terms_match.group(1).strip()

            # Extract delivery schedule
            delivery_match = re.search(
                r'Delivery / Schedule:(.*?)(?=\d\.)', text, re.DOTALL)
            if delivery_match:
                po_info['delivery_schedule'] = delivery_match.group(1).strip()

            return po_info

        # Usage
        # pdf_path = 'path/to/your/pdf/file.pdf'
        pdf_text = extract_text_from_pdf(input_pdf_path)
        po_info = parse_po_info(pdf_text)

        # Print extracted information
        for key, value in po_info.items():
            print(f"{key}: {value}")
        return po_info
    elif template == 2:

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
            po_match = re.search(
                r'PO No\s*(PS/\d{4}/\d{2}-\d{2})\s*\n\s*Date\s*(\d{2}/\d{2}/\d{4})', text)
            if po_match:
                po_info['po_number'] = po_match.group(1)
                try:
                    po_info['po_date'] = datetime.strptime(
                        po_match.group(2), '%d/%m/%Y').date()
                except ValueError:
                    po_info['po_date'] = None  # Handle invalid date format

            # Extract supplier info
            supplier_match = re.search(
                r"Supplier's Name :\s*([\s\S]*?)(?=GSTIN)", text)
            if supplier_match:
                po_info['supplier'] = supplier_match.group(1).strip()

            # Extract supplier GSTIN
            gstin_match = re.search(r'GSTIN :\s*(\S+)', text)
            if gstin_match:
                po_info['supplier_gstin'] = gstin_match.group(1)

            # Extract delivery schedule
            delivery_match = re.search(r'Delivery Schedule\s*(.*)', text)
            if delivery_match:
                po_info['delivery_schedule'] = delivery_match.group(1).strip()

            # Extract payment terms
            payment_match = re.search(r'Payment Terms\s*(.*)', text)
            if payment_match:
                po_info['payment_terms'] = payment_match.group(1).strip()

            # Extract line items
            items_match = re.findall(
                r'(\d+)\s+(.*?)\s+(\d+)\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s+NOS\s+(\d+(?:\.\d+)?)', text)
            po_info['line_items'] = [
                {
                    'sr_no': item[0],
                    'description': item[1],
                    'hsn': item[2],
                    'quantity': item[3],
                    'rate': item[4],
                    'unit': 'NOS',
                    'amount': item[5]
                }
                for item in items_match
            ]

            # Extract total amount
            total_match = re.search(r'Final Amount\s*([\d.]+)', text)
            if total_match:
                po_info['total_amount'] = total_match.group(1)

            # Extract GST amount
            gst_match = re.search(
                r'Total GST Value \(In Word\) :\s*(.*)', text)
            if gst_match:
                po_info['gst_amount_words'] = gst_match.group(1)

            return po_info

        # Usage
        # pdf_path = 'path/to/your/pdf/file.pdf'
        pdf_text = extract_text_from_pdf(input_pdf_path)
        po_info = parse_po_info(pdf_text)

        # Print extracted information
        for key, value in po_info.items():
            print(f"{key}: {value}")
        return po_info
    elif template == 3:

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
            po_match = re.search(
                r'PO No\.: (\d+)\s*PO Date: (\d{2}/\d{2}/\d{4})', text)
            if po_match:
                po_info['po_number'] = po_match.group(1)
                po_info['po_date'] = datetime.strptime(
                    po_match.group(2), '%d/%m/%Y').date()

            # Extract supplier info
            supplier_match = re.search(
                r'Consignor \[Supplier\'s Details\](.*?)Consignee', text, re.DOTALL)
            if supplier_match:
                po_info['supplier'] = supplier_match.group(1).strip()

            # Extract customer info
            customer_match = re.search(
                r'Consignee \[Receiver\'s Details\](.*?)PO Details', text, re.DOTALL)
            if customer_match:
                po_info['customer'] = customer_match.group(1).strip()

            # Extract line items
            items_match = re.findall(
                r'(\d+)\s+Item Code:.*?Item Name: (.*?)\s+Item Description:.*?(\d{2}-\d{2}-\d{4})\s+(\d+)\s+(\w+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+(?:,\d+)*\.\d+)', text)
            po_info['line_items'] = [
                {
                    'item_no': item[0],
                    'description': item[1],
                    'delivery_date': item[2],
                    'hsn_code': item[3],
                    'uom': item[4],
                    'quantity': item[5],
                    'rate': item[6],
                    'amount': item[7].replace(',', '')
                }
                for item in items_match
            ]

            # Extract total amount
            total_match = re.search(r'Total PO Amount\s+([\d,]+\.\d+)', text)
            if total_match:
                po_info['total_amount'] = total_match.group(1).replace(',', '')

            # Extract payment terms
            payment_terms_match = re.search(r'Payment Terms\s+(.*)', text)
            if payment_terms_match:
                po_info['payment_terms'] = payment_terms_match.group(1).strip()

            # Extract freight terms
            freight_terms_match = re.search(r'Freight Terms\s+(.*)', text)
            if freight_terms_match:
                po_info['freight_terms'] = freight_terms_match.group(1).strip()

            # Extract destination
            destination_match = re.search(r'Destination\s+(.*)', text)
            if destination_match:
                po_info['destination'] = destination_match.group(1).strip()

            # Extract PO remark
            remark_match = re.search(r'PO Remark:\s+(.*)', text)
            if remark_match:
                po_info['po_remark'] = remark_match.group(1).strip()

            return po_info

        # Usage
        pdf_text = extract_text_from_pdf(input_pdf_path)
        po_info = parse_po_info(pdf_text)

        # Print extracted information
        for key, value in po_info.items():
            print(f"{key}: {value}")
        return 0
    elif template == 4:
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
            po_match = re.search(
                r'PO Number\s*:\s*(\d+)\s*PO Date\s*:\s*(\d{2}\.\d{2}\.\d{4})', text)
            if po_match:
                po_info['po_number'] = po_match.group(1)
                po_info['po_date'] = datetime.strptime(
                    po_match.group(2), '%d.%m.%Y').date()

            # Extract supplier info
            supplier_match = re.search(
                r'Supplier Details\s*:(.*?)Supplier GST\s*:', text, re.DOTALL)
            if supplier_match:
                po_info['supplier'] = supplier_match.group(1).strip()

            # Extract supplier GST
            gst_match = re.search(r'Supplier GST\s*:\s*(\S+)', text)
            if gst_match:
                po_info['supplier_gst'] = gst_match.group(1)

            # Extract customer info
            customer_match = re.search(
                r'ASHOK LEYLAND LTD\.(.*?)GST Number : (\S+)', text, re.DOTALL)
            if customer_match:
                po_info['customer'] = customer_match.group(1).strip()
                po_info['customer_gst'] = customer_match.group(2)

            # Extract line items
            items_match = re.findall(
                r'(\d+)\s+(\d+)\s+(.*?)\s+Dly\. Date:(\d{2}\.\d{2}\.\d{4})\s+(\d+)\s+(.*?)\s+AU\s+(\d+\.\d+)\s+([\d,]+\.\d+)\s+([\d,]+\.\d+)', text)
            po_info['line_items'] = [
                {
                    'po_line_no': item[0],
                    'sac_code': item[1],
                    'description': item[2],
                    'delivery_date': datetime.strptime(item[3], '%d.%m.%Y').date(),
                    'line_no': item[4],
                    'service_line_desc': item[5],
                    'quantity': item[6],
                    'rate': item[7].replace(',', ''),
                    'net_value': item[8].replace(',', '')
                }
                for item in items_match
            ]

            # Extract total amounts
            total_match = re.search(
                r'Total Net Value :([\d,]+\.\d+)\s*Total Tax Value :([\d,]+\.\d+)\s*Total Order Value :([\d,]+\.\d+)', text)
            if total_match:
                po_info['total_net_value'] = total_match.group(
                    1).replace(',', '')
                po_info['total_tax_value'] = total_match.group(
                    2).replace(',', '')
                po_info['total_order_value'] = total_match.group(
                    3).replace(',', '')

            # Extract payment terms
            payment_terms_match = re.search(
                r'Payment Terms : (.*?)Mode of Despatch', text)
            if payment_terms_match:
                po_info['payment_terms'] = payment_terms_match.group(1).strip()

            return po_info

        # Usage
        pdf_text = extract_text_from_pdf(input_pdf_path)
        po_info = parse_po_info(pdf_text)

        # Print extracted information
        for key, value in po_info.items():
            print(f"{key}: {value}")
        return po_info
    elif template == 5:
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
            po_match = re.search(
                r'P\.O\. No:\s*(DTA/\d+-\d+/\w+/\d+)\s*P\. O\. Date:\s*(\d{2}-\d{2}-\d{4})', text)
            if po_match:
                po_info['po_number'] = po_match.group(1)
                po_info['po_date'] = datetime.strptime(
                    po_match.group(2), '%d-%m-%Y').date()

            # Extract supplier info
            supplier_match = re.search(
                r"SUPPLIER'S NAME\s*(.*?)\s*P\. O\. Date:", text, re.DOTALL)
            if supplier_match:
                po_info['supplier'] = supplier_match.group(1).strip()

            # Extract customer info
            customer_match = re.search(
                r'DAKSH TOOLS & APPLIANCES \(P\) LTD\.(.*?)GSTIN-\s*(\S+)', text, re.DOTALL)
            if customer_match:
                po_info['customer'] = 'DAKSH TOOLS & APPLIANCES (P) LTD.'
                po_info['customer_address'] = customer_match.group(1).strip()
                po_info['customer_gstin'] = customer_match.group(2)

            # Extract line items
            items_match = re.findall(
                r'(\d+)\s+(.*?)\s+(\d+(?:,\d+)*)\s+([\d.]+)\s+([\d,]+\.\d+)', text)
            po_info['line_items'] = [
                {
                    'sl_no': item[0],
                    'description': item[1],
                    'quantity': item[2].replace(',', ''),
                    'rate': item[3],
                    'amount': item[4].replace(',', '')
                }
                for item in items_match
            ]

            # Extract total amount
            total_match = re.search(r'NET AMOUNT\s+([\d,]+\.\d+)', text)
            if total_match:
                po_info['total_amount'] = total_match.group(1).replace(',', '')

            # Extract terms and conditions
            po_info['terms_conditions'] = {}

            taxes_match = re.search(r'Taxes:\s*(.*)', text)
            if taxes_match:
                po_info['terms_conditions']['taxes'] = taxes_match.group(
                    1).strip()

            delivery_match = re.search(r'Delivery Period:\s*(.*)', text)
            if delivery_match:
                po_info['terms_conditions']['delivery_period'] = delivery_match.group(
                    1).strip()

            payment_match = re.search(r'Payment Terms:\s*(.*)', text)
            if payment_match:
                po_info['terms_conditions']['payment_terms'] = payment_match.group(
                    1).strip()

            shipment_match = re.search(r'Mode of Shipment:\s*(.*)', text)
            if shipment_match:
                po_info['terms_conditions']['mode_of_shipment'] = shipment_match.group(
                    1).strip()

            return po_info

        # Usage
        pdf_text = extract_text_from_pdf(input_pdf_path)
        po_info = parse_po_info(pdf_text)

        # Print extracted information
        for key, value in po_info.items():
            print(f"{key}: {value}")
            return po_info

    elif template == 6:
        return 0
    elif template == 7:
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
            po_match = re.search(
                r'PO\.NO\.\s*:\s*(\d+).*?Date\s*:\s*(\d{2}-\d{2}-\d{4})', text, re.DOTALL)
            if po_match:
                po_info['po_number'] = po_match.group(1)
                po_info['po_date'] = datetime.strptime(
                    po_match.group(2), '%d-%m-%Y').date()

            # Extract PO validity
            validity_match = re.search(
                r'Po Validity date\s*:\s*(\d{2}-\d{2}-\d{4})', text)
            if validity_match:
                po_info['po_validity'] = datetime.strptime(
                    validity_match.group(1), '%d-%m-%Y').date()

            # Extract buyer info
            buyer_match = re.search(
                r'STUDDS ACCESSORIES LIMITED\. \(Plant-I\)(.*?)Details of Supplier', text, re.DOTALL)
            if buyer_match:
                po_info['buyer'] = buyer_match.group(1).strip()

            # Extract buyer GST
            buyer_gst_match = re.search(r'GST IN\s*:\s*(\w+)', text)
            if buyer_gst_match:
                po_info['buyer_gst'] = buyer_gst_match.group(1)

            # Extract supplier info
            supplier_match = re.search(
                r'Name\s*:\s*(.*?)Address\s*:', text, re.DOTALL)
            if supplier_match:
                po_info['supplier'] = supplier_match.group(1).strip()

            # Extract supplier address
            address_match = re.search(
                r'Address\s*:\s*(.*?)Ph\. No\.', text, re.DOTALL)
            if address_match:
                po_info['supplier_address'] = address_match.group(1).strip()

            # Extract supplier GST
            supplier_gst_match = re.search(r'GSTIN\s*:\s*(\w+)', text)
            if supplier_gst_match:
                po_info['supplier_gst'] = supplier_gst_match.group(1)

            # Extract line items
            items_match = re.findall(
                r'(\d+)\s+(\w+)\s+(\d+)\s+(.*?)\s+As Per\s+(\w+)\s+Open\s+([\d.]+)', text)
            po_info['line_items'] = [
                {
                    'sr_no': item[0],
                    'item_code': item[1],
                    'hsn_sac': item[2],
                    'description': item[3].strip(),
                    'uom': item[4],
                    'unit_price': item[5]
                }
                for item in items_match
            ]

            # Extract total amounts
            total_basic_match = re.search(
                r'Total Basic Value\s+([\d.]+)', text)
            if total_basic_match:
                po_info['total_basic_value'] = total_basic_match.group(1)

            total_po_match = re.search(r'Total PO Value\s+([\d.]+)', text)
            if total_po_match:
                po_info['total_po_value'] = total_po_match.group(1)

            # Extract payment terms
            payment_terms_match = re.search(
                r'Payment Term\s*:\s*(.*?)$', text, re.MULTILINE)
            if payment_terms_match:
                po_info['payment_terms'] = payment_terms_match.group(1).strip()

            return po_info

        # Usage
        pdf_text = extract_text_from_pdf(input_pdf_path)
        po_info = parse_po_info(pdf_text)

        # Print extracted information
        for key, value in po_info.items():
            print(f"{key}: {value}")
        return 0
    elif template == 8:
        return 0
    elif template == 9:
        return 0
    elif template == 10:
        return 0
    return 0
