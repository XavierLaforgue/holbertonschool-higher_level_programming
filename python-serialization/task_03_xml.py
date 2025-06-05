#!/usr/bin/python3
"""
Module Name: task_03_xml.

Contains function to serialize xml file.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize dictionary into xml and save in file."""
    root = ET.Element("data")
    for k, v in dictionary.items():
        child = ET.SubElement(root, str(k))
        child.text = str(v)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """Read XML data from file and deserialize to python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    my_dict = {}
    for child in root:
        my_dict[child.tag] = child.text
        
    return my_dict
