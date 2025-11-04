import re
import smtplib
from email.message import EmailMessage


def validate_tc_number(tc: str) -> bool:
    """Basit bir TC kimlik numarası doğrulaması (mock).
    Kurallar:
    - 11 hane
    - ilk rakam 0 olamaz
    - son rakam, diğerlerinin toplamının 10 ile modulus'ine eşit olmalı (örnek mock kural)
    Not: Gerçek doğrulama için resmi algoritma / servis kullanılmalı.
    """
    if not isinstance(tc, str):
        return False

    if not re.fullmatch(r"[1-9]\d{10}", tc):
        return False

    digits = list(map(int, tc))
    return sum(digits[:-1]) % 10 == digits[-1]


def send_email(smtp_host, smtp_port, smtp_user, smtp_pass, subject, body, to):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = smtp_user or "noreply@example.com"
    msg["To"] = to
    msg.set_content(body)

    with smtplib.SMTP(smtp_host, smtp_port, timeout=10) as s:
        s.ehlo()
        try:
            s.starttls()
        except Exception:
            pass
        if smtp_user and smtp_pass:
            s.login(smtp_user, smtp_pass)
        s.send_message(msg)
