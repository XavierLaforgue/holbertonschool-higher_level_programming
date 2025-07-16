#!/usr/bin/python3
import os


def generate_invitations(template: str, attendees: list[dict]):
    try:
        if not isinstance(template, str):
            raise TypeError(f'Invalid template: template must be a string but\
                             it is of type {type(template)}.')
        if not isinstance(attendees, list):
            raise TypeError(f'Invalid attendees: attendees must be a list of \
                            dictionaries but it is of type {type(attendees)}.')
        filenames = []
        for idx in range(len(attendees)):
            if not isinstance(attendees[idx], dict):
                raise TypeError(f'Invalid attendee: each attendee must be \
                                dictionary but one is of type \
                                {type(attendees[idx])}.')
            filenames.append(f'output_{idx + 1}.txt')
        if len(template.strip()) == 0:
            raise ValueError('Template is empty, no output files generated.')
        if len(attendees) == 0:
            raise ValueError('No data provided, no output files generated.')
        for filename in filenames:
            if os.path.exists(filename):
                raise FileExistsError(f'File {filename} already exists, no \
                                      output files generated.')
    except Exception as e:
        return e
    for attendee, filename in zip(attendees, filenames):
        name = attendee.get('name')
        if name is None:
            name = 'name: N/A'
        title = attendee.get('event_title')
        if title is None:
            title = 'event_title: N/A'
        date = attendee.get('event_date')
        if date is None:
            date = 'event_date: N/A'
        location = attendee.get('event_location')
        if location is None:
            location = 'event_location: N/A'
        invitation = template.replace('{name}', name)\
            .replace('{event_title}', title)\
            .replace('{event_date}', date)\
            .replace('{event_location}', location)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(invitation)
