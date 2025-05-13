#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) > 0:
        return sorted(a_dictionary.items(), key=lambda kv: kv[1])[-1][0]
