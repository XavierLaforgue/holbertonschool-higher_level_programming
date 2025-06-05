#!/usr/bin/python3
"""
Module Name: task_02_csv.

Contains a function to serialize csv files.
"""
import csv
import json


def convert_csv_to_json(CSVfilename: str):
    """Convert csv file to json file."""
    try:
        with open(CSVfilename, "r", encoding="utf-8") as csvfile:
            list_of_dict_from_csv = list(csv.DictReader(csvfile))
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(list_of_dict_from_csv, jsonfile)
        return True
    except Exception as e:
        print(e)
        return False
