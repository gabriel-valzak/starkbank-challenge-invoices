import os
import starkbank

def load_starkbank_user():
    project_id = os.getenv("STARKBANK_PROJECT_ID")
    private_key_path = os.getenv("STARKBANK_PRIVATE_KEY_PATH")
    environment = os.getenv("STARKBANK_ENVIRONMENT", "sandbox")

    if not project_id or not private_key_path:
        raise Exception("...")

    # lê a chave privada
    with open(private_key_path, "r") as key_file:
        private_key = key_file.read()

    starkbank.user = starkbank.Project(
        environment=environment,
        id=project_id,
        private_key=private_key
    )
