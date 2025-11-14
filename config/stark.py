import os
import base64
import starkbank

def load_starkbank_user():
    project_id = os.getenv("STARKBANK_PROJECT_ID")
    private_key_path = os.getenv("STARKBANK_PRIVATE_KEY_PATH")
    private_key_env = os.getenv("STARKBANK_PRIVATE_KEY")
    environment = os.getenv("STARKBANK_ENVIRONMENT", "sandbox")

    if not project_id:
        raise Exception("STARKBANK_PROJECT_ID não configurado")

    if private_key_env:
        try:
            decoded = base64.b64decode(private_key_env.encode())
            if decoded.strip().startswith(b"-----BEGIN"):
                private_key = decoded.decode()
            else:
                private_key = private_key_env
        except Exception:
            private_key = private_key_env
    elif private_key_path:
        with open(private_key_path, "r") as f:
            private_key = f.read()
    else:
        raise Exception("Nenhuma chave privada fornecida (STARKBANK_PRIVATE_KEY ou STARKBANK_PRIVATE_KEY_PATH)")

    starkbank.user = starkbank.Project(
        environment=environment,
        id=project_id,
        private_key=private_key
    )
