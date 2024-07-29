# from fpdf import FPDF


# def generate_sales_order(info):
#     pdf = FPDF()
#     pdf.add_page()

#     pdf.set_font("Arial", size=12)

#     pdf.cell(200, 10, txt="Sales Order", ln=True, align='C')

#     pdf.cell(200, 10, txt=f"PO No: {info['PO No']}", ln=True)
#     pdf.cell(200, 10, txt=f"Date: {info['Date']}", ln=True)
#     pdf.cell(200, 10, txt=f"Supplier: {info['Supplier']}", ln=True)
#     pdf.cell(200, 10, txt=f"Contact Person: {info['Contact Person']}", ln=True)
#     pdf.cell(200, 10, txt=f"Email: {info['Email']}", ln=True)
#     pdf.cell(200, 10, txt=f"Phone: {info['Phone']}", ln=True)
#     pdf.cell(200, 10, txt=f"Description: {info['Description']}", ln=True)
#     pdf.cell(200, 10, txt=f"Quantity: {info['Quantity']}", ln=True)
#     pdf.cell(200, 10, txt=f"Delivery Date: {info['Delivery Date']}", ln=True)
#     pdf.cell(200, 10, txt=f"Amount: {info['Amount']}", ln=True)

#     pdf.output("Sales1_Order.pdf")


# Generate sales order
# generate_sales_order(extracted_info)

from fpdf import FPDF

def generate_sales_order(info):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Sales Order", ln=True, align='C')
    pdf.ln(10)
    
    pdf.cell(200, 10, txt=f"PO No: {info['PO No']}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {info['Date']}", ln=True)
    pdf.cell(200, 10, txt=f"Supplier: {info['Supplier']}", ln=True)
    pdf.cell(200, 10, txt=f"Consignor: {info['Consignor']}", ln=True)
    pdf.cell(200, 10, txt=f"Contact Person: {info['Contact Person']}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {info['Email']}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {info['Phone']}", ln=True)
    pdf.cell(200, 10, txt=f"Description: {info['Description']}", ln=True)
    pdf.cell(200, 10, txt=f"Quantity: {info['Quantity']}", ln=True)
    pdf.cell(200, 10, txt=f"Delivery Date: {info['Delivery Date']}", ln=True)
    pdf.cell(200, 10, txt=f"Amount: {info['Amount']}", ln=True)
    pdf.cell(200, 10, txt=f"Address: {info['Address']}", ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Line Items:", ln=True)
    pdf.ln(5)
    
    for item in info['Line Items']:
        pdf.cell(200, 10, txt=f"Sr. No: {item[0]}", ln=True)
        pdf.cell(200, 10, txt=f"Description: {item[1]}", ln=True)
        pdf.cell(200, 10, txt=f"HSN: {item[2]}", ln=True)
        pdf.cell(200, 10, txt=f"Quantity: {item[3]}", ln=True)
        pdf.cell(200, 10, txt=f"Rate: {item[4]}", ln=True)
        pdf.cell(200, 10, txt=f"Taxable Amount: {item[5]}", ln=True)
        pdf.ln(5)
    
    pdf.output("Sales1_Order.pdf")

# # Generate sales order
# generate_sales_order(extracted_info)
