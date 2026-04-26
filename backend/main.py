from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()
client = OpenAI()

@app.get("/")
def home():
    return {"msg": "Copy Sản Phẩm Shopee PRO 🚀"}

@app.post("/rewrite")
def rewrite(data: dict):
    prompt = f"Rewrite chuẩn SEO Shopee:\n{data}"

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return {"text": res.choices[0].message.content}
