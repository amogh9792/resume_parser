import re

def extract_contact_details(text):
    """Extract email and phone number from text."""
    email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    phone = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    return email[0] if email else None, phone[0] if phone else None
