import re

def analyze_sms(sms_content):
    # Regular expressions to search for common phishing keywords or patterns
    phishing_keywords = ['verify', 'login', 'password', 'account', 'urgent', 'confirm']
    suspicious_patterns = [r'\bhttps?://\S+\b', r'\b\d{4,}\b']

    # Check for phishing keywords in the SMS content
    for keyword in phishing_keywords:
        if keyword in sms_content.lower():
            return True

    # Check for suspicious patterns (e.g., URLs, numeric codes)
    for pattern in suspicious_patterns:
        if re.search(pattern, sms_content):
            return True

    return False

def prevent_smishing(sms_content):
    if analyze_sms(sms_content):
        print("Suspicious SMS detected. Take appropriate action (e.g., warn user, block message).")
    else:
        print("SMS appears to be safe.")

# Example usage
if _name_ == "_main_":
    sms_content = "Your account needs verification. Click here: http://example.com/verify"
    prevent_smishing(sms_content)
