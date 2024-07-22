import keyring

token = keyring.get_password("github", "access_token")
print(f"Token: {token}")

