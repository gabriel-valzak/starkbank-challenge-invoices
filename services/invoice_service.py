from random import choice,randint
import starkbank
from config.stark import load_starkbank_user


CLIENTS = [
    {"name": "João Pedro Silva", "tax_id": "964.989.460-83"},
    {"name": "Mariana Oliveira", "tax_id": "338.210.290-05"},
    {"name": "Lucas Ferreira", "tax_id": "121.833.660-95"},
    {"name": "Ana Beatriz Costa", "tax_id": "068.286.790-08"},
]


def create_invoices():
    load_starkbank_user()

    count = randint(8, 12)
    invoices = []
    for _ in range(count):
        client = choice(CLIENTS)
        amount_cents = randint(1000, 9000) * 10

        invoice = starkbank.Invoice(
            amount=amount_cents,
            name=client["name"],
            tax_id=client["tax_id"],
            tags=["auto-generated"],
        )
        invoices.append(invoice)

    invoices = starkbank.invoice.create(invoices)

    return invoices