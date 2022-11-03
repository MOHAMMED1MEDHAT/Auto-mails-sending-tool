import send_email
from fastapi import FastAPI,Path


app=FastAPI()
@app.get("/")
def send():
    try:
        send_email.send()
        return "emails sent successfully"
    except:
        return"ERROR"
#initialize the app using command  (⁡⁢⁣⁡⁢⁣⁣uvicorn email_api:app --reload⁡⁡)