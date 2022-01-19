#!/bin/bash

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
VENTILATOR=$(echo $DATA | jq '.[0].onVentilatorCurrently')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalizedCurrently')
NEGATIVE=$(echo $DATA | jq '.[0].negative')

echo "On $TODAY, there were $POSITIVE positive COVID cases and $NEGATIVE negative tests."
echo "There are $HOSPITALIZED people hospitalized currently."
echo "Of those hospitalized, $VENTILATOR people are currently on a ventilator"

