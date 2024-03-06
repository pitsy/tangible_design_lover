from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  api_key = os.getenv("OPENAI_API_KEY")
)

current_dir = os.path.dirname(__file__)  # Gets the directory where the current script is located
detail_file_path = os.path.join(current_dir, 'prompt_detail.txt')  # Builds the path to the detail file

# Read the file content once and store it
with open(detail_file_path, "r", encoding="utf-8") as file:
    detail_content = file.read()

def generate_text(prompt):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": detail_content},
      {"role": "user", "content": prompt}
    ]
  )
  return completion.choices[0].message.content

def generate_image(prompt):
  try:
    response = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      n=1,
      size="1024x1024"
    )
    # Extract the URL of the generated image
    image_url = response.data[0].url
    return image_url
  except Exception as e:
    print(f"An error occurred while generating the image: {e}")
    return None
