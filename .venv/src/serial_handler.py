import serial
import time
from src.api import generate_text, generate_image

char_to_word = {
    "0": "very tall",
    "1": "very short",
    "2": "athletic",
    "3": "very skinny",
    "4": "overweight",
    "5": "lizard scales",
    "6": "lazy",
    "7": "overly friendly",
    "8": "green skin",
    "9": "multiple eyes",
    "A": "highly arrogant",
    "B": "highly creative",
    "C": "extremely serious",
    "D": "placid and boring",
}

def read_from_arduino(ser):
    mapped_words = []
    while True:
        if ser.in_waiting > 0:
            char = ser.read().decode('utf-8').strip()
            print(char)
            if char in char_to_word:
                mapped_words.append(char_to_word[char])
                print(f"prompt: {', '.join(mapped_words)}")
            elif char == "#":
                prompt = ", ".join(mapped_words)
                print(f"Sending prompt: {prompt}")
                send_prompt(prompt)
                mapped_words.clear()
            elif char == "*":
                if mapped_words:
                    mapped_words.pop()
                    print(f"prompt: {', '.join(mapped_words)}")

def send_prompt(prompt):
    text_response = generate_text(prompt)
    # text_response = "Generate an image based on the following description: A character stands before us, embodying a whimsical blend of traits. With seven mischievous eyes scattered across a hairy visage reminiscent of a tangled forest, this figure exudes a comical charm. Clad in mismatched, haphazard attire that suggests both adventurous spirit and a touch of laziness, the character's pose conveys a nonchalant yet curious demeanor. Imagine a photorealistic yet surreal scene inspired by Magritte, where conventional boundaries blur, and the unexpected reigns supreme. Incorporate all of the above characteristics into a cohesive and detailed portrayal. Make the portrayal full body, from head to toe. Do not use text in the image. Make the background white. Put the character in front view, looking at us.  Have just one character in the image. Make the style of the image photorealistic and emphasize surrealistic aspects in the style of famous surrealist painters. Do not output any text to accompany the image. Make the output image in portrait aspect ratio."

    if text_response:
        print(f"Text Response: {text_response}")
        image_url = generate_image(text_response)
        if image_url:
            print(f"Generated Image URL: {image_url}")
        else:
            print("Image generation failed.")
    else:
        print("Failed to get a text response.")