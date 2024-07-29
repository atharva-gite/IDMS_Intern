import api_call
import extract_text
import SO


def main():
    input_pdf_path = 'path_to_your_purchase_order.pdf'
    output_pdf_path = 'sales_order.pdf'

    # Step 2: Extract text from the uploaded PO PDF
    po_text = extract_text.extract_text_from_pdf(input_pdf_path)

    # Step 3: Send extracted text to GPT API and get structured data
    po_data = api_call.get_structured_data_from_gpt(po_text)

    # Step 4: Generate SO PDF using the structured data
    SO.create_sales_order_pdf(po_data, output_pdf_path)

    print(f"Sales Order PDF created at: {output_pdf_path}")


if __name__ == "__main__":
    main()
