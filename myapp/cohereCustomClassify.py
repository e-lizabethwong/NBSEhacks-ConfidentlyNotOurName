import cohere
import base64
from openai import OpenAI


oa_api_key = "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"
ch_api_key = "fVHw36A8DdVfH3ubOgu6bjQotk37QinmZLz4X0sq"

vision = OpenAI(api_key=oa_api_key)

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image
# cant open the sql :(((

image_path = "myapp/media/images/walmartReceipt.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)


client = OpenAI(api_key=oa_api_key)
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What was purchased in this receipt? How much was it?",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        # replace with front end input
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)

imageDescription = response.choices[0].message.content

co = cohere.Client(ch_api_key)
# get the custom model object
ft = co.get_custom_model_by_name('fVHw36A8DdVfH3ubOgu6bjQotk37QinmZLz4X0sq')

classifiedPurchase = co.classify(
    inputs=["classify this!"],
    model=ft.model_id,
)

# Printing the model's response.
print(classifiedPurchase)