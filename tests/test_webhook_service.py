from unittest.mock import patch
from services.process_webhook_service import process_webhook
import starkbank


@patch("starkbank.transfer.create")
def test_process_webhook_success(mock_transfer_create):
    mock_transfer_create.return_value = ["transfer1"]

    payload = {
        "event": {
            "log": {
                "invoice": {
                    "id": "123",
                    "amount": 5000,
                    "fee": 200
                }
            }
        }
    }

    with patch.object(starkbank, "user", None):
        transfer = process_webhook(payload)

    assert transfer == ["transfer1"]
    mock_transfer_create.assert_called_once()


def test_process_webhook_error():
    payload = {"invalid": "structure"}

    result = process_webhook(payload)

    assert result["status_code"] == 500
    assert result["success"] is False
    assert "error" in result["content"]
