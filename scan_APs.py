import subprocess

process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-s'], stdout=subprocess.PIPE)
out, err = process.communicate()
process.wait()

out=str(out)

def scanAP_rssi(ss1,ss2,ss3):
	ssid1=ss1
	start=out.find("-",out.rfind(ssid1))
	end=start+3
	rssi1=out[start:end].strip()
	rssi1=int(rssi1)

	ssid2=ss2
	start=out.find("-",out.rfind(ssid2))
	end=start+3
	rssi2=out[start:end].strip()
	rssi2=int(rssi2)


	ssid3=ss3
	start=out.find("-",out.rfind(ssid3))
	end=start+3
	rssi3=out[start:end].strip()
	rssi3=int(rssi3)


	return rssi1,rssi2,rssi3








