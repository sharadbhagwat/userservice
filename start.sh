#!/usr/bin/env bash
export PYTHONPATH=$pwd;
export DJANGO_SETTINGS_MODULE=MyProject.db.settings.local_settings;
python MyProject/conf/service_app.py