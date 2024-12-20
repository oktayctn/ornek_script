# Example script designed to trigger GitGuardian detections

# Hardcoded sensitive string that mimics an SSH key
ssh_private_key_simulated = "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAA...\n-----END OPENSSH PRIVATE KEY-----"

# Encoded secret that appears harmless to some scanners
encoded_secret = "U0VDUkVUX1RPS0VOX0VYQU1QTEU="  # Base64 for "SECRET_TOKEN_EXAMPLE"

# Comments with sensitive-looking content
# Secret: abcdef1234567890supersecrettoken

# Static API token in an unusual format
def custom_api_token():
    return "custom-token-example-1234-5678-abcdef"

# Hardcoded credentials that resemble generic text but are detectable
ftp_password = "ftp_secure_pass_Example1234!"

print("Simulated sensitive data initialized.")
