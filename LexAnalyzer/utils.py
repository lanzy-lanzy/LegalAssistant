import google.generativeai as genai
from django.conf import settings
import pdfplumber
import json

def analyze_document(file_path):
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel(settings.GEMINI_MODEL_NAME)
    
    # Extract text from PDF
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
            
    prompt = f"""
    Analyze the following legal document and provide a structured JSON response.
    Document Text: {text[:12000]}
    
    The JSON must follow this EXACT schema:
    {{
        "summary": "String - Concise executive summary",
        "risks": [
            {{
                "type": "String - e.g., Financial, Legal, Operational",
                "severity": "String - MUST be one of: 'rose' (high), 'amber' (medium), 'emerald' (low)",
                "text": "String - Detailed description of the risk",
                "category": "String - e.g., Liability, Compliance, IP"
            }}
        ],
        "clauses": ["String - Recommended mitigation clause text"],
        "key_dates": ["String - Format: 'Event Name: Date'"]
    }}
    
    Important: 
    - Return ONLY the JSON object. 
    - Do not include markdown formatting or '```json' tags.
    - Be critical and professional.
    """

    
    response = model.generate_content(prompt)
    
    try:
        clean_response = response.text.replace('```json', '').replace('```', '').strip()
        analysis_data = json.loads(clean_response)
        analysis_data['extracted_text'] = text # Include full text for the viewer
        return analysis_data

    except Exception as e:
        return {{
            "error": str(e),
            "summary": "Failed to analyze document.",
            "risks": [],
            "clauses": [],
            "key_dates": []
        }}
