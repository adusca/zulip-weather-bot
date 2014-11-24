import zulip
import pywapi
import string

def get_weather(location):
    """ Uses pywapi to get current weather information from weather.com"""
    weather_com_result = pywapi.get_weather_from_weather_com(location)
    msg =  "It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in New York.\n"
    return msg

client = zulip.Client()
client.register(event_types=['message'])

def respond(event):
    """Reply with weather info to whoever send it a message"""
    if event['type'] == 'message' and event['message']['sender_email'] != 'simple-weather-bot@students.hackerschool.com':
        client.send_message({
            "type" : "private",
            "to" : event['message']['sender_email'],
            "content" : get_weather('10013')
        })

client.call_on_each_event(respond)
