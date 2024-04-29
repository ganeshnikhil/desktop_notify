# it is used to send notification 
from notifypy import Notify

# to lag betweeen when nedded 
import time

# to get the current time
from datetime import datetime

# if you are a windows user 
   ## pip install notifypy

# if you are a mac user or linux user 
   ## pip3 install notifypy

'''
choose folder 
   if you want sound effect then choose : sound 
   if you want voice effect then choose : voice 
'''
folder_name = 'voice'

# all resources paths and message are put in the dictionary
dic = {
   'water':['icon/water.png', f'{folder_name}/water.wav', "Drink Water Nikhil.."],
   'study':['icon/study.png', f'{folder_name}/study.wav',"Go for study dude!"],
   'food':['icon/food.png' , f'{folder_name}/food.wav' , "Go eat some food.."],
   'walk':['icon/walk.png' ,f'{folder_name}/walk.wav',"Go for a walk dude"],
   'alarm':['icon/alarm.png',f'sound/alarm.wav' , "wakeup champ . it's time"]
}

# set a alarm 
alram_time = ['09:13 P']

# works is organized in the list
works = ['water','water','water','study','food','water' ,'water','water','walk']

# restrictive times
#for am
start_am , end_am = 1 , 7
#for pm 
start_pm , end_pm = 7 , 12 


# INTIALIZE THE NOTIFICATION LIBRARY WITH INITAL PARAMETERS 
notification = Notify(
   default_notification_title = "Hi how are you",
   default_application_name = "Notifier",
   default_notification_icon = "icon/icon.png",
   default_notification_audio = "sound/sound.wav",
)

# get the current time hour:minute PM/AM
def get_cur_time() -> str:
   tm = datetime.now()
   cur_time = tm.strftime('%I:%M %P')
   return cur_time 

# play sound as notification alarm 
def play_sound() -> None:
   icon_file, sound_file, msg = dic['alarm']
   notification.icon = icon_file
   notification.audio = sound_file
   notification.message = msg
   notification.send()

# if it is alarm time 
def is_alarm_time(time_now) -> bool:
   if time_now in alram_time:
      return True 
   return False 

# THE THE TIME IN HOUR AND AM OR PM 
def get_am_pm() -> list[str] :
   dt_obj = datetime.now()
   cur_time = dt_obj.strftime('%I:%P')
   return cur_time.split(':')

def notify_me(hour_gap = 5) -> None:
   # convert hour in seconds 
   lag = hour_gap * 60 * 60 
   lag = 15
   counter = 0 
   
   while True:
      
      if alram_time:
         time_now = get_cur_time()
         print(time_now)
         flag = is_alarm_time(time_now)
         if flag:
            print("[*] It's alarm time.....")
            play_sound()
            index = alram_time.index(time_now)
            alram_time.pop(index)
            
      work = works[counter]
      icon_file , sound_file , msg  = dic[work]
      notification.icon = icon_file 
      notification.audio = sound_file 
      notification.message = msg 
      
      hour, day_night = get_am_pm()
      hour = int(hour)
      
      # restricting the notifcation on sleeping and resting time ..
      if day_night == 'A' and hour in range(start_am, end_am) or day_night == 'P' and hour in range(start_pm, end_pm):
         print("[+] It's not a Suitable time....")
         return
      
      notification.send()

      counter = (counter + 1) % len(works)  # Loop through works list
      time.sleep(lag)

def main():
   notify_me()

if __name__ == '__main__':
   main()

