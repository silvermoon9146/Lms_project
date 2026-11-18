from celery import shared_task
import time

@shared_task
def send_otp_sms_task(phone, otp_code):
    #connect to sms panel api
    print(f'OTP Code {otp_code} sent to {phone}')

    time.sleep(2)
    return f'OTP Code {otp_code} sent to {phone}'