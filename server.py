from flask import Flask, redirect, url_for
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer():
    """Respond to incoming buzzer requests"""

    return redirect(url_for('approve'))


@app.route("/approve", methods=['GET', 'POST'])
def approve():
    """Approve a buzzer request"""

    resp = VoiceResponse()
    resp.play('', digits='9')
    resp.redirect(url_for('approve'))

    return str(resp)


@app.route("/reject", methods=['GET', 'POST'])
def reject():
    """Reject a buzzer request"""

    resp = VoiceResponse()
    resp.hangup()

    return str(resp)


if __name__ == "__main__":
    app.run()
