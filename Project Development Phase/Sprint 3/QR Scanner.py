import cv2
import numpy as np
import time
import pyzbar.pyzbar as pyzbar
from ibmcloudant import CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator 
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator('apikey-v2-1g7cjqnq8808x36x3w0x6lcztrf4jyuov0h2pv6xrx3p', 'bf62988cf8a35e964d9d86e3d28d1feb')
service = CloudantV1(authenticator=authenticator)

service.set_service_url('https://apikey-v2-1g7cjqnq8808x36x3w0x6lcztrf4jyuov0h2pv6xrx3p:bf62988cf8a35e964d9d86e3d28d1feb@0cac9b27-cd14-4e73-9014-bd2d30bf5399-bluemix.cloudantnosqldb.appdomain.cloud')

cap= cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
	_, frame = cap.read()
	decodedObjects = pyzbar.decode (frame)
	for obj in decodedObjects:
		#print ("Data", obj.data)
		a=obj.data.decode('UTF-8')
		cv2.putText(frame, "Ticket", (50, 50), font, 2,	(255, 0, 0), 3)

		#print (a)
		try:
			response = service.get_document(
				db='booking',
				doc_id = a
			).get_result()
			print (response)
			time.sleep(5)
		except Exception as e:
			print ("Not a Valid Ticket")
			time.sleep(5)

	cv2.imshow("Frame",frame)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
client.disconnect()
