import openai


def get_structured_data_from_gpt(extracted_text):
    openai.api_key = 'sk-proj-O1lLtgULE6AidA0RFFK2T3BlbkFJjZEI74AfQiBs6YMabkQx'

    response = openai.completions.create(
        model="text-davinci-003",
        prompt=f"Extract the relevant data from the following Purchase Order text and format it as a dictionary for creating a Sales Order:\n\n{extracted_text}\n\n",
        max_tokens=500
    )

    structured_data = eval(response.choices[0].text.strip())
    return structured_data
