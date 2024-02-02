from twilio.rest import Client

account_sid = 'AC0a7984a7e9eeab7e5eb04639fa730304'
auth_token = '1f269de38fded7a99f88e6ee099e7be4'
client = Client(account_sid, auth_token)

def sendAlert(accident_start_time, accident_end_time):

    message = client.messages.create(
    from_='+17652524743',
    body=f''' Emergency Alert!!!
            Accident Detected!
            from {accident_start_time:.2f} to {accident_end_time:.2f}''',
    to='+918240716218'
    )
    print("Alert sended!")
