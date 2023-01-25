# jarvis
STT input and TTS output verbal chatbot using OpenAI API and AWS's Amazon Polly.

Similar to JARVIS from Iron Man, this script uses OpenAI's text-davinci-three engine to create responses to user-generated queries.

Requirements:
    Must have an OpenAI API Key (https://beta.openai.com/account/api-keys)
    Must have an AWS account before accessing Amazon Polly (free for the first 120 hours of verbal response)
    Must attain an AWS Access Key ID and an AWS Secret Access Key 
        AWS -> IAM -> Users -> New User -> [Give Permissions] -> Security Credentials -> Access Keys

Within the script feel free to change:
    Max Tokens (How long the response will be)
    The VoiceID (Options: https://docs.aws.amazon.com/polly/latest/dg/voicelist.html)
    Output Format (Currently mp3)
