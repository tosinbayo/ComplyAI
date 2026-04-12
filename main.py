from fastapi import FastAPI, UploadFile, File
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a senior cybersecurity GRC expert and ISO 27001 compliance auditor.

Analyze documents and identify:
- Compliance gaps
- Risk levels
- Recommendations

Be concise, structured, and practical.
"""

@app.get("/")
def home():
    return {"message": "ComplyAI AI Engine Running 🚀"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")

    prompt = f"""
Analyze the following document for ISO 27001 compliance:

{text}

Provide:
- Compliance score (0-100)
- Key risks
- Recommendations
"""

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "analysis": response.choices[0].message.content
    }
    import os
from fastapi import HTTPException
from fastapi.responses import FileResponse

@app.get("/download-report/{report_name}")
def download_report(report_name: str):
    safe_name = report_name.replace(" ", "_")
    file_path = f"reports/{safe_name}.pdf"

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Report file not found")

    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=f"{safe_name}_Compliance_Report.pdf"
    )
    from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)