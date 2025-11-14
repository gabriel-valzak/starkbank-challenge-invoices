from unittest.mock import patch
from services import invoice_service
import starkbank


@patch("starkbank.invoice.create")
def test_create_invoices(mock_create):
    mock_create.return_value = ["invoice1", "invoice2"]

    with patch.object(starkbank, "user", None):
        invoices = invoice_service.create_invoices()

    assert isinstance(invoices, list)
    assert len(invoices) == 2
    mock_create.assert_called_once()
