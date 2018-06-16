from flask import Flask
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer():
    """Respond to incoming buzzer requests"""

    return approve_response()


def approve_response():
    """Response to approve a buzzer request"""

    resp = VoiceResponse()
    resp.play('', digits='w9', loop=0)

    return str(resp)


def reject_response():
    """Response to reject a buzzer request"""

    resp = VoiceResponse()
    resp.hangup()

    return str(resp)


if __name__ == "__main__":
    app.run()
