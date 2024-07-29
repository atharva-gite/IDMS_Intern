# from module import input_processor, template_matcher, data_extractor, data_validator, so_generator


# def process_po(po_file):
#     # Read PO
#     po_text = input_processor.read_po(po_file)

#     # Match template
#     template = template_matcher.find_best_match(po_text)

#     # Extract data
#     po_data = data_extractor.extract_data(po_text, template)

#     # Validate data
#     validated_data = data_validator.validate(po_data)

#     # Generate SO
#     so = so_generator.generate_so(validated_data)

#     return so


# if __name__ == "__main__":
#     po_file = "1.pdf"
#     so = process_po(po_file)
#     print(so)
from module import template_matcher, data_extractor, so_generator
input_path = 'po_formats\\template1.pdf'
a, b = template_matcher.main(input_path)
template_number = a[19]
text = data_extractor.extractor(input_path, int(template_number))
so_generator.so_maker(text, int(template_number))
print(text)
# text = extract1.extract_po_information(input_path)
# print(text)
# generate1.generate_sales_order(text)
# for key,value in text:
#     print(f"{key}\t{value}\n")
