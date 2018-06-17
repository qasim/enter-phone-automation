from os import getenv
from flask import Flask, Response, redirect, url_for, request
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer():
    """Respond to an incoming buzzer request"""

    # Forward calls that don't originate from the buzzer system to my
    # personal phone number (for emergency purposes)
    if request.args.get('From') != getenv('BUZZER_PHONE_NUMBER'):
        return redirect(url_for('forward?to=%s' % getenv('MY_PHONE_NUMBER')))

    # TODO: Submit notification to phone. Based on user action, redirect
    # to the appropriate choice between 'approve', 'reject', or 'forward'

    return redirect(url_for('approve'))


@app.route("/approve", methods=['GET', 'POST'])
def approve():
    """Approve a buzzer request"""

    resp = VoiceResponse()

    # Play the DTMF tone for '9'
    resp.play('', digits='9')

    # Redirect to same endpoint to play '9' continuously until the call
    # is ended by the enter phone system
    resp.redirect(url_for('approve'))

    return Response(str(resp), mimetype='text/xml')


@app.route("/reject", methods=['GET', 'POST'])
def reject():
    """Reject a buzzer request"""

    resp = VoiceResponse()

    # Hanging up the phone call will reject the buzzer request
    resp.hangup()

    return Response(str(resp), mimetype='text/xml')


@app.route("/forward", methods=['GET', 'POST'])
def reject():
    """Forward a buzzer request to a designated phone number"""

    resp = VoiceResponse()

    # Dial the designated phone number
    resp.dial(request.args.get('to'))

    return Response(str(resp), mimetype='text/xml')


if __name__ == "__main__":
    app.run()
