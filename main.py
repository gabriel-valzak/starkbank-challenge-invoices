from json import loads
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from services import invoice_service
from services.process_webhook_service import process_webhook

app = FastAPI()

@app.post("/api/webhook")
async def invoice_webhook(request: Request):
    raw_body = await request.body()

    payload = loads(raw_body)

    if payload["event"]["subscription"] == "invoice":
        transfer = process_webhook(payload)

    return JSONResponse({"ok": True})


@app.post("/api/invoices")
async def create_invoices():
    invoices = invoice_service.create_invoices()

    return JSONResponse({"ok": True})
