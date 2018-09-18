# Hassio light action for Snips

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/Wav3/snips-skill-smartlight/master/LICENSE.txt)

## Introduction

With this action you are able to control your lights in home assistant via Snips.

## Setup

In order to be able to control your lights in home assistant via Snips, you must enable and configure the following home assistant components:
- [api](https://www.home-assistant.io/components/api/)
- [http](https://www.home-assistant.io/components/http/) (required for the component api)

For this action the following configuration variables from home assistant are required and should be saved:
- api_password (used for the value HTTP_API_PASSWORD in config.ini)
- server_port (used for the value HTTP_API_PORT in config.ini)

### Installation with Sam

This is the easiest way to install this action.  
You use [Sam](https://snips.gitbook.io/getting-started/installation) to install this action.  
`sam install actions -g https://github.com/Wav3/snips-skil-smartlight.git`  
  
Sam will ask during the installation for the following values to connect the action with hassio:  
- HTTP_API_PORT (The port where home assistant is listening (default: 8123))
- HTTP_API_HOSTNAME (The hostname of the home assistant (default: hassio))
- HTTP_API_PASSWORD (The password of the home assistant for the api)


### Manual installation

This skill requires some python dependencies to work properly, these are listed in the `requirements.txt`. You can use the `setup.sh` script to create a python virtualenv that will be recognized by the skill server and install them in it.
1. Clone the repository on your pi with `git clone https://github.com/Wav3/snips-skil-smartlight.git`
2. Run `setup.sh` (it will create a virtualenv, install all dependencies defined in 'requirements.txt' and rename config.ini.default to config.ini)
3. Provide the required values for HTTP_API_PORT, HTTP_API_HOSTNAME and HTTP_API_PASSWORD in the config.ini
4. Run `action-LightOff.py`
5. Run `action-LightOn.py`

## Copyright

This action is provided by Janek Kröger as Open Source software. See [LICENSE.txt](https://raw.githubusercontent.com/Wav3/snips-skill-smartlight/master/LICENSE.txt) for more information.