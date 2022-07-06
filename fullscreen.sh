source /home/pi/repos/reddit-picture-frame/venv/bin/activate
export DISPLAY=":0"
python3 /home/pi/repos/reddit-picture-frame/ep_st.py &
unclutter &
matchbox-window-manager &
chromium --kiosk --user-data-dir="/var/tmp/chromium" --disable-web-security --start-fullscreen /home/pi/earthporn_showerthoughts/ep_st.html &


