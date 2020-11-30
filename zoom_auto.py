import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
 

def sign_in(meetingid, pswd):
	#opensup the zoom app
	subprocess.call(["C:/Users/Harsh Patel/AppData/Roaming/Zoom/bin/Zoom.exe"])
	time.sleep(10)

	#clicks the join button
	join_btn=pyautogui.locateCenterOnScreen('join_btn.png')
	pyautogui.moveTo(join_btn)
	pyautogui.click()

	# type the meeting id 
	meeting_id_btn= pyautogui.locateCenterOnScreen('meetid_btnnn.png')
	pyautogui.moveTo(meeting_id_btn)
	#pyautogui.click()
	#pyautogui.click(clicks=3, interval=.25)
	pyautogui.PAUSE = 1 
	pyautogui.write(meetingid,interval=0.25)


	audio_sil= pyautogui.locateCenterOnScreen('audio_off.png')
	pyautogui.moveTo(audio_sil)
	pyautogui.click()
	video_sil= pyautogui.locateCenterOnScreen('video_off.png')
	pyautogui.moveTo(video_sil)
	pyautogui.click()

	join2_bt= pyautogui.locateCenterOnScreen('join2_btn.png')
	pyautogui.moveTo(join2_bt)
	pyautogui.click()

	time.sleep(5)

	meet_passw= pyautogui.locateCenterOnScreen('meet_pass.png')
	pyautogui.moveTo(meet_passw)
	pyautogui.write(pswd,interval=0.25)

	final_join= pyautogui.locateCenterOnScreen('fjoin_btn.png')
	pyautogui.moveTo(final_join)
	pyautogui.click()

	#pyautogui.write(meetingid)
df= pd.read_csv('time.csv')

while True:
	now=datetime.now().strftime("%H:%M")
	if now in str(df['timings']):
		row=df.loc[df['timings']== now]
		m_id=str(row.iloc[0,1])
		m_pswd=str(row.iloc[0,2])

		sign_in(m_id, m_pswd)
		time.sleep(40)
		print('signed in')


#sign_in('74872676027','7i9DcQ')	
