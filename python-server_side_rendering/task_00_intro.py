#!/usr/bin/python3
"""Substitutes key values into a template and generates a new file"""

import os


def generate_invitations(template, attendees):
    """
    Substitutes key values into a template and generates a new file
    """
    if (
    not isinstance(template, str) 
    or not isinstance(attendees, list)
    or not all(isinstance(item, dict) for item in attendees)
    ):
        print('Invalid input: expected a string template and a list of dictionaries.')
        return

    if not template:
        print('Template is empty, no output files generated.')
        return
    if not attendees:
        print('No data provided, no output files generated.')
        return

    for index, item in enumerate(attendees, start=1):   # loops through attendees
        invite_template = template[:]                   # creates a copy of the template

        placeholder = ["name", "event_title", "event_date", "event_location"]               # defines the items we're looking for in template
        for key in placeholder:
            if key in invite_template:                  # finds placeholder values in template
                value = item.get(key, "N/A")            # fetches value or falls back                                            
                invite_template = invite_template.replace("{" + key + "}", str(value))      # applies replacement data, and re-binds data to template

        try:
            new_filename = (f"output_{index}.txt")
            if not os.path.exists(new_filename):            # checks for existing filename first
                with open(new_filename, "w") as f:          # creates a file with new filename
                    f.write(invite_template)                # writes completed template data to new filename
        except Exception as e:
            return (f"error: {e}"
