from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Function to create Sales Order PDF
def create_sales_order_pdf(output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Purchase Order data (static)
    po_data = {
        'SO No': 'SO/0242/23-24',
        'Date': '26/07/2023',
        'Customer': 'PROTECH SPORTS AND SAFETY PRODUCTS PVT. LTD.',
        'Contact Person': 'REENA NAIK',
        'Email': 'reena@decaltech.in',
        'Phone No': '9833891091 / 9920674826',
        'Description': 'STIK RUD FRM - SRS FORMA ROUND STICKER (NEW)',
        'Quantity': '2000',
        'Rate': '3.00',
        'Total': '6000.00',
        'Delivery Schedule': 'At Our Factory GIDC\nDt. 1st Aug, 2023',
        'Payment Terms': '45-Days.',
        'Dispatch Through': 'At Our Factory GIDC',
    }

    # Add Sales Order Header
    c.drawString(100, height - 50, "Sales Order")
    c.drawString(100, height - 70, f"SO No: {po_data['SO No']}")
    c.drawString(100, height - 90, f"Date: {po_data['Date']}")
    
    # Add Customer Information
    c.drawString(100, height - 130, "Customer Information:")
    c.drawString(120, height - 150, f"Customer: {po_data['Customer']}")
    c.drawString(120, height - 170, f"Contact Person: {po_data['Contact Person']}")
    c.drawString(120, height - 190, f"Email: {po_data['Email']}")
    c.drawString(120, height - 210, f"Phone No: {po_data['Phone No']}")

    # Add Goods Information
    c.drawString(100, height - 250, "Goods Information:")
    c.drawString(120, height - 270, f"Description: {po_data['Description']}")
    c.drawString(120, height - 290, f"Quantity: {po_data['Quantity']}")
    c.drawString(120, height - 310, f"Rate: {po_data['Rate']}")
    c.drawString(120, height - 330, f"Total: {po_data['Total']}")

    # Add Additional Information
    c.drawString(100, height - 370, "Additional Information:")
    c.drawString(120, height - 390, f"Delivery Schedule: {po_data['Delivery Schedule']}")
    c.drawString(120, height - 410, f"Payment Terms: {po_data['Payment Terms']}")
    c.drawString(120, height - 430, f"Dispatch Through: {po_data['Dispatch Through']}")

    c.save()

# Main function
def main():
    output_pdf_path = '1sales_order.pdf'
    create_sales_order_pdf(output_pdf_path)
    print(f"Sales Order PDF created at: {output_pdf_path}")

if __name__ == "__main__":
    main()
