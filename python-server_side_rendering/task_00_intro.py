#!/usr/bin/python3

import sys

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template must be a string")
        sys.exit()
    if not isinstance(attendees, list):
        print("Attendees must be a list of dictionaries")
        sys.exit()

    if len(template) == 0:
        print("Template is empty, no output files generated.")
        sys.exit()
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        sys.exit()

    keys = ["name", "event_title", "event_date", "event_location"]

    for i in range(len(attendees)):
        output = template
        for key in keys:
            try:
                output = output.replace("{" + "{}".format(key) + "}", attendees[i]["{}".format(key)])
            except (TypeError, KeyError):
                output = output.replace("{" + "{}".format(key) + "}", "N/A")

        with open("output_{}.txt".format(i + 1), 'w') as file:
            file.write(output)
