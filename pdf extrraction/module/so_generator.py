from fpdf import FPDF


def so_maker(text, template):
    if template == 1:
        class PDF(FPDF):

            def header(self):
                self.set_font('Arial', 'B', 14)
                self.cell(0, 10, 'Sales Order', 0, 1, 'C')
                self.ln(10)

            def chapter_title(self, title):
                self.set_font('Arial', 'B', 12)
                self.cell(0, 10, title, 0, 1, 'L')
                self.ln(5)

            def chapter_body(self, body):
                self.set_font('Arial', '', 12)
                self.multi_cell(0, 10, body)
                self.ln()

            def add_table(self, line_items):
                self.set_font('Arial', 'B', 12)
                self.cell(20, 10, 'Sl No', 1)
                self.cell(100, 10, 'Description', 1)
                self.cell(30, 10, 'Quantity', 1)
                self.cell(20, 10, 'Rate', 1)
                self.cell(30, 10, 'Amount', 1)
                self.ln()

                self.set_font('Arial', '', 12)
                for item in line_items:
                    self.cell(20, 10, item['sl_no'], 1)
                    self.cell(100, 10, item['description'], 1)
                    self.cell(30, 10, item['quantity'], 1)
                    self.cell(20, 10, item['rate'], 1)
                    self.cell(30, 10, item['amount'], 1)
                    self.ln()

        def generate_sales_order(data, template):
            pdf = PDF()
            pdf.add_page()

            # PO Number and Date
            pdf.chapter_title(f'PO Number: {data["po_number"]}')
            pdf.chapter_title(f'PO Date: {data["po_date"]}')

            # Supplier Information
            pdf.chapter_title('Supplier:')
            pdf.chapter_body(data["supplier"])

            # Ship To Information
            pdf.chapter_title('Ship To:')
            pdf.chapter_body(data["ship_to"])

            # Line Items Table
            pdf.chapter_title('Line Items:')
            pdf.add_table(data["line_items"])

            # Total Amount
            pdf.chapter_title(f'Total Amount: {data["total_amount"]}')

            # Payment Terms
            pdf.chapter_title('Payment Terms:')
            pdf.chapter_body(data["payment_terms"])

            # Delivery Schedule
            pdf.chapter_title('Delivery Schedule:')
            pdf.chapter_body(data["delivery_schedule"])

            # Save the PDF to a file
            template=template
            filename = "sales_order{template}.pdf"
            pdf.output(filename)
        generate_sales_order(text, template)
        return 0
    elif template == 2:
        return 0
    elif template == 3:
        return 0
    elif template == 4:
        return 0
    elif template == 5:
        return 0
    elif template == 6:
        return 0
    elif template == 7:
        return 0
    elif template == 8:
        return 0
    elif template == 9:
        return 0
    elif template == 10:
        return 0
