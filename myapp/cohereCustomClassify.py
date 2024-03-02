import cohere
import base64
from openai import OpenAI


oa_api_key = "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"
ch_api_key = "qvsnPF32GyJsIFjGQXzzY8MCEUlNabK4TiVZ6sgX"


# Function to encode the image
def CustomClassify(image_field):
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    if not image_field:
        return None  # or some default value

    # If your ImageField stores files locally, use this:
    image_path = image_field.path

    # Encode the image to base64
    base64_image = encode_image(image_path)

    # machine vision implementation via API
    vision = OpenAI(api_key=oa_api_key)
    response = vision.chat.completions.create(
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
    )

    # get image description in String format
    imageDescription = response.choices[0].message.content

    # COHERE classify implementation
    co = cohere.Client(ch_api_key)
    # implement custom model
    ft = co.get_custom_model_by_name('purchasesort')

    classifiedPurchase = co.classify(
        inputs=[imageDescription],
        model=ft.model_id,
    )

    # getting the final answer from the model
    classification = classifiedPurchase.classifications[0].predictions[0]
    
    return classification