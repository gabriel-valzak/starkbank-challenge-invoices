import starkbank
from config.stark import load_starkbank_user

DEST_ACCOUNT = {
    "bank_code": "20018183",
    "branch_code": "0001",
    "account_number": "6341320293482496",
    "tax_id": "20.018.183/0001-80",
    "name": "Stark Bank S.A.",
    "account_type": "payment",
}

def process_webhook(payload):
    try:
        load_starkbank_user()
        
        invoice = payload["event"]["log"]["invoice"]

        transfer = starkbank.Transfer(
            amount=(invoice["amount"] - invoice["fee"]),
            bank_code=DEST_ACCOUNT["bank_code"],
            branch_code=DEST_ACCOUNT["branch_code"],
            account_number=DEST_ACCOUNT["account_number"],
            account_type=DEST_ACCOUNT["account_type"],
            tax_id=DEST_ACCOUNT["tax_id"],
            name=DEST_ACCOUNT["name"],
            tags=["webhook-transfer", f"invoice:{invoice["id"]}"],
        )
        transfer = starkbank.transfer.create([transfer])

        return transfer

    except Exception as e:
        return {
            'status_code': 500,
            'content': {'error': str(e)},
            'success': False
        }
