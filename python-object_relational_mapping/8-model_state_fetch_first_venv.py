#!./orm-venv/bin/python
"""
Module Name: 7-model_state_fetch_all_venv.

Contains execution of model_state_fetch_all function.
"""
if __name__ == "__main__":
    model_state_fetch_first =\
        __import__('8-model_state_fetch_first').model_state_fetch_first

    model_state_fetch_first()
