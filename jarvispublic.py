import speech_recognition as sr
import openai
import boto3
import pygame
import time

openai.api_key = "YOUR_OPEN_AI_API_KEY"

r = sr.Recognizer()

session = boto3.Session(
    aws_access_key_id = "YOUR_AWS_ACCESS_KEY_ID",
    aws_secret_access_key = "YOUR_AWS_SECRET_ACCESS KEY",
)
polly = session.client("polly", region_name = "us-east-1")

with sr.Microphone() as source:
    print("How can I help you, sir?")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print("You said: " + text)

response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = text,
    max_tokens = 200
)

response_text = response["choices"][0]["text"]
print(response_text)

response = polly.synthesize_speech(
    Text = response_text,
    VoiceId = "Brian",
    OutputFormat = "mp3"
)

filename = f"response_{int(time.time())}.mp3"
with open(filename, "wb") as f:
    f.write(response["AudioStream"].read())

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)