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
# input_pdf_path = '5.pdf'
# template_pdf_paths = ['po_formats\\template1.pdf', 'po_formats\\template2.pdf', 'po_formats\\template3.pdf', 'po_formats\\template4.pdf', 'po_formats\\template5.pdf',
#                       'po_formats\\template6.pdf', 'po_formats\\template7.pdf', 'po_formats\\template8.pdf', 'po_formats\\template9.pdf', 'po_formats\\template10.pdf']
# input_text = extract_text_from_pdf(input_pdf_path)
# input_text = preprocess_text(input_text)

# # Initialize variables to store the highest similarity and corresponding template
# highest_similarity = 0
# best_template = None

# # Iterate over each template PDF
# for template_pdf_path in template_pdf_paths:
#     # Extract and preprocess text from template PDF
#     template_text = extract_text_from_pdf(template_pdf_path)
#     template_text = preprocess_text(template_text)

#     # Calculate cosine similarity
#     similarity = calculate_cosine_similarity(input_text, template_text)

#     # Update highest similarity and best template if current one is higher
#     if similarity > highest_similarity:
#         highest_similarity = similarity
#         best_template = template_pdf_path

# # Print the best template and its similarity score
# print(f"Template with highest similarity: {best_template}")
# print(f"Highest Cosine Similarity Score: {highest_similarity}")

import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import nltk
from nltk.corpus import stopwords

# # Download NLTK resources if not already downloaded
# nltk.download('stopwords')

# Function to extract text from PDF


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Function to preprocess text


def preprocess_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Convert to lowercase
    text = text.lower()

    # Tokenize (split into words)
    words = text.split()

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Join the words back into a single string
    text = ' '.join(words)

    return text

# Function to calculate cosine similarity between two texts


def calculate_cosine_similarity(text1, text2):
    # Create TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the texts
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return cosine_sim[0][0]

# Function to find the most similar template


def find_most_similar_template(input_pdf_path, template_pdf_paths):
    input_text = extract_text_from_pdf(input_pdf_path)
    input_text = preprocess_text(input_text)

    # Initialize variables to store the highest similarity and corresponding template
    highest_similarity = 0
    best_template = None

    # Iterate over each template PDF
    for template_pdf_path in template_pdf_paths:
        # Extract and preprocess text from template PDF
        template_text = extract_text_from_pdf(template_pdf_path)
        template_text = preprocess_text(template_text)

        # Calculate cosine similarity
        similarity = calculate_cosine_similarity(input_text, template_text)

        # Update highest similarity and best template if current one is higher
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_template = template_pdf_path

    return best_template, highest_similarity

# Main function


def main(input_pdf_path):
    # Paths to your PDFs
    template_pdf_paths = ['po_formats/template1.pdf', 'po_formats/template2.pdf', 'po_formats/template3.pdf', 'po_formats/template4.pdf', 'po_formats/template5.pdf',
                          'po_formats/template6.pdf', 'po_formats/template7.pdf', 'po_formats/template8.pdf', 'po_formats/template9.pdf', 'po_formats/template10.pdf']

    best_template, highest_similarity = find_most_similar_template(
        input_pdf_path, template_pdf_paths)

    # Print the best template and its similarity score
    # print(f"Template with highest similarity: {best_template}")
    # print(f"Highest Cosine Similarity Score: {highest_similarity}")
    return best_template, highest_similarity


# Run main function if script is executed directly
if __name__ == "__main__":
    main()
