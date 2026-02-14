import requests
import json
from config import GEMINI_API_KEY


def generate_script(topic):

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    prompt = f"""
Create a professional and product-focused YouTube explainer script (90–120 seconds total) about:

"{topic}"

Structure it strictly into 3 scenes using this exact format:

### Scene 1:
Explain the hiring problem – large applicant volumes, manual resume screening, recruiter workload, bias, and slow decision-making.

### Scene 2:
Explain how AI resume parsing and video interview analysis works – NLP-based keyword extraction, skills matching, automated scoring, facial expression analysis, communication evaluation, and data-driven insights.

### Scene 3:
Explain the business impact – faster hiring, improved candidate matching, reduced bias, scalability, cost efficiency, and smarter talent acquisition strategies.

Tone Guidelines:
- Professional and modern
- Clear and concise
- Product-demo style
- No dramatic storytelling
- No unnecessary filler lines
"""

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    print("Status Code:", response.status_code)

    result = response.json()

    if "candidates" not in result:
        raise Exception("API error: " + response.text)

    return result["candidates"][0]["content"]["parts"][0]["text"]
