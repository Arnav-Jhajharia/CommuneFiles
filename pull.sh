#!/bin/bash
echo $(git pull)
echo $(sudo systemctl daemon-reload)
echo $(sudo systemctl restart gunicorn)
echo$(sudo systemctl restart nginx)
echo $"All NEW FILES PULLED AND SYSTEM UPDATES! ALL DONE"

