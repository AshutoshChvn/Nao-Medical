
import os
import google.generativeai as genai

def transc_ai(transcript, language):
    genai.configure(api_key="AIzaSyBGRUlx6A4UQN39MhA5hMQO0xlytcsouvg")
    
    # Create the model
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 40,
      "max_output_tokens": 800,
      "response_mime_type": "text/plain",
    }
    
    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config,
    )
    
    chat_session = model.start_chat(
      history=[
      ]
    )
    
    response = chat_session.send_message(f'''
    Here is transcript : {transcript}

    Instruction :
    1. Review the transcript for any incorrect wording or errors.
    2. Correct any errors found in the transcript.
    3. Translate the corrected transcript into the specified language: {language}.
    
    Return only the translated transcript as a string, without any additional text or commentary.
    ''')
    
    print(response.text)
    result = response.text
    return result