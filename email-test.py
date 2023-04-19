import smtplib
import dns.resolver

email_to = '<<email address>>'  # <- Email Address
email_from = 'no_reply@domain.com'
email_subject = "A email subject"
email_message = "Email message body"

email_message = f"""From: <{email_from}>
To: <{email_to}>
Subject: {email_subject}

{email_message}
"""

domain = email_to.split('@')[1]
domain_mx_list = dns.resolver.resolve(domain, 'MX')
domain_mx = str(domain_mx_list[0].exchange)

try:
    smtp_obj = smtplib.SMTP(domain_mx)
    smtp_obj.sendmail(email_from, email_to, email_message)
    print("Successfully sent email...")
except smtplib.SMTPException:
    print("Error: unable to send email")
