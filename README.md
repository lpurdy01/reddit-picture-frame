# Reddit Picture Frame
!There be bugs and lazy code here!


This repo is designed to make a nice picture frame like display from photos posted to a subreddit. Originally designed to pull from r/dalle2, but it should be reasonably adaptable.

For the default scripts to work, must be cloned into

```/home/pi/repos/reddit-picture-frame```

Such that the ep_st.html is located at

```/home/pi/repos/reddit-picture-frame/ep_st.html```


A venv should be setup:

```python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Installing praw will fail, simply install with

```pip3 install praw```


You need chromium for this to work. I used

```sudo apt-get install chromium x11-xserver-utils matchbox unclutter```

And some *making stuff executable*. You probably need to do this to ```ep_st.py``` and ```fullscreen.sh```

```
sudo chmod 777 ep_st.py
sudo chmod +x ep_st.py
```

```./fullscreen.sh``` is the start command. Look at it before you run it. It runs both ep_st.py and a chromium instance. You have to manually go kill those processes before running it again.


# Setup Notes From Earthporn Showerthoughts

Setup in terminal:
```shell
git clone https://gitlab.com/scul/earthporn_showerthoughts.git
cd earthporn_showerthoughts 
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Change the file paths in `ep_st.config` for:
- `template`: where you have stored the template (should be the same folder)
- `display`:  where you want the output file (`ep_st.html`)
- `log`:      where to put the log file (`ep_st.log`)  

default location for all 3 above is the same folder as 'ep_st.py

If desired, set the display_path to somewhere accessible by your webserver, otherwise does not matter
Run the python3 script (from the containing folder: `./ep_st.py`)
Go to the output file, and display it in your webbrowser.

Feel free to tinker with the settings (minSize, number of posts to get, etc...)

## Other Useful Sites I Took Stuff From

[ShowerThoughts and EarthPorn: Make an Inspiring Raspberry Pi Photo Frame](https://www.makeuseof.com/tag/showerthoughts-earthporn-make-inspiring-raspberry-pi-photo-frame/)
