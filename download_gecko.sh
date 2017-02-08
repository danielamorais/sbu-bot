#!/bin/bash
GECKO_VERSION='v0.14.0'
GECKO_PLATFORM='linux64'

GECKO_FILE="geckodriver-"$GECKO_VERSION"-"$GECKO_PLATFORM".tar.gz"
GECKO_URL="https://github.com/mozilla/geckodriver/releases/download/"$GECKO_VERSION"/"$GECKO_FILE

if [[ ! -e ./geckodriver ]]
then
    wget $GECKO_URL --quiet
    tar -zxvf $GECKO_FILE > /dev/null
    rm $GECKO_FILE > /dev/null
fi
