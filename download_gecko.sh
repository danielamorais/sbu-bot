#!/bin/sh
GECKO_VERSION='v0.14.0'
GECKO_PLATFORM='linux64'

GECKO_FILE="geckodriver-"$GECKO_VERSION"-"$GECKO_PLATFORM".tar.gz"
GECKO_URL="https://github.com/mozilla/geckodriver/releases/download/"$GECKO_VERSION"/"$GECKO_FILE

wget $GECKO_URL
tar -zxvf $GECKO_FILE
rm $GECKO_FILE
