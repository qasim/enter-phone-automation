from flask import Flask
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)


@app.route("/answer")
def answer():
    """Respond to incoming buzzer requests"""

    resp = VoiceResponse()
    resp.redirect('/approve')

    return str(resp)


@app.route("/approve")
def approve():
    """Approve a buzzer request"""

    resp = VoiceResponse()
    resp.play('', digits='w9')
    resp.redirect('/approve')

    return str(resp)


@app.route("/reject")
def reject():
    """Reject a buzzer request"""

    resp = VoiceResponse()
    resp.hangup()

    return str(resp)


if __name__ == "__main__":
    app.run()
