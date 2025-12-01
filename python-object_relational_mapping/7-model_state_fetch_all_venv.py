#!./orm-venv/bin/python
"""
Module Name: 7-model_state_fetch_all_venv.

Contains execution of model_state_fetch_all function.
"""
if __name__ == "__main__":
    model_state_fetch_all =\
        __import__('7-model_state_fetch_all').model_state_fetch_all

    model_state_fetch_all()
