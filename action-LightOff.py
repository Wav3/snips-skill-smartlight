#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import requests
import json

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIGURATION_INI = "config.ini"

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section: {option_name : option for option_name, option in self.items(section)} for section in self.sections()}

def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intent_message):
    conf = read_configuration_file(CONFIGURATION_INI)
    action_wrapper(hermes, intent_message, conf)

def action_wrapper(hermes, intent_message, conf):
    apiport = conf['secret']['http_api_port']
    apihost = conf['secret']['http_api_hostname']
    url = 'http://{}:{}/api/services/light/turn_off'.format(apihost, apiport)
    header = {
        "Content-Type": "application/json",
        "x-ha-access": conf['secret']['http_api_password']
    }
    current_session_id = intent_message.session_id # get the current session id

    if len(intent_message.slots.Zimmer) > 0: #turns on a specific light
        zimmer = intent_message.slots.Zimmer.first().value # extract the value from the slot Zimmer
        result_sentence = "Licht in Raum {} eingeschaltet.".format(str(zimmer))
        body = {
            "entity_id": "light.{}".format(str(zimmer))
        }
        json_body = json.dumps(body)
        request = requests.post(url, data = json_body, headers = header)
    else: # turns on every known light
        result_sentence = "Alle Lichter wurden eingeschaltet"
        request = requests.post(url, headers = header)
    
    if request.status_code != 200: # if the action is failed, set the response to failed
        result_sentence = "Das Lichtanschalten ist fehlgeschlagen"
        print('Error during enabling light.\nStatuscode: {}\nResponse message: {}'.format(request.status_code, request.content))

    hermes.publish_end_session(current_session_id, result_sentence)

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("kroegerj:LightOff", subscribe_intent_callback).start()