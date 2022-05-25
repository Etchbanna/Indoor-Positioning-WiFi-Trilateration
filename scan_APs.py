import subprocess
import time



def scanAP_rssi(ss1,ss2,ss3):
	s1=s2=s3=0
	for i in range(10) :
		process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-s'], stdout=subprocess.PIPE)
		out, err = process.communicate()
		process.wait()
		out=str(out)
		
		ssid1=ss1
		start=out.find("-",out.rfind(ssid1))
		end=start+3
		rssi1=out[start:end].strip()
		print(rssi1)

		rssi1=int(rssi1)

		s1=s1+rssi1
		print('s1 is')
		print(str(s1))
		ssid2=ss2
		start=out.find("-",out.rfind(ssid2))
		end=start+3
		rssi2=out[start:end].strip()
		rssi2=int(rssi2)
		s2=s2+rssi2

		ssid3=ss3
		start=out.find("-",out.rfind(ssid3))
		end=start+3
		rssi3=out[start:end].strip()
		rssi3=int(rssi3)
		s3=s3+rssi3

	return (s1/10),(s2/10),(s3/10)



	# out=str(out)
	# ssid1=ss1
	# start=out.find("-",out.rfind(ssid1))
	# end=start+3
	# rssi1=out[start:end].strip()
	# rssi1=int(rssi1)

	# ssid2=ss2
	# start=out.find("-",out.rfind(ssid2))
	# end=start+3
	# rssi2=out[start:end].strip()
	# rssi2=int(rssi2)


	# ssid3=ss3
	# start=out.find("-",out.rfind(ssid3))
	# end=start+3
	# rssi3=out[start:end].strip()
	# rssi3=int(rssi3)











