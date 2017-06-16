import Cayenne.client
import time

class CayenneRunner(object):
    # Cayenne authentication info.
    def __init__(self):
        self.MQTT_USERNAME  = "674bb4c0-529c-11e7-8ab6-097b71ab053c"
        self.MQTT_PASSWORD  = "153bb352f5dd66528fa819307b297aea6bd35012"
        self.MQTT_CLIENT_ID = "cf752200-529e-11e7-910e-05c4802271ed"
        self.Client = Cayenne.client.CayenneMQTTClient()
        self.SendInterval = 10
    def MainLoop(self):
        self.Client.on_message = self.on_message
        self.Client.begin(self.MQTT_USERNAME, self.MQTT_PASSWORD, self.MQTT_CLIENT_ID)
        localTimeStamp = time.time()
        while True:
            self.Client.loop()
            # Get Current Time
            if (time.time() > localTimeStamp + self.SendInterval):
                self.Client.luxWrite(2, 5)
                # Update localTimeStamp
                localTimeStamp = time.time()
                print("Sent")
    # The callback for when a message is received from Cayenne.
    def on_message(self, message):
        print("message received: " + str(message))
        # If there is an error processing the message return an error string, otherwise return nothing.

if __name__ == "__main__":
    # Create Controller Loop
    CayenneRunner = CayenneRunner()
    # Run Infinite Loop
    CayenneRunner.MainLoop()