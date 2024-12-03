from datetime import datetime
import time
import json
import random
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=assignmentiothub007.azure-devices.net;DeviceId=NAC;SharedAccessKey=7kczs0B0SyWCqYQF6DNXn1krWMah7rJqtaqR6VJDkAw="

def get_telemetry():
    return {
        "location":"NAC",
        "iceThickness": round(random.uniform(5, 50), 2),
        "surfaceTemperature": round(random.uniform(-10, 5), 1),
        "snowAccumulation":round(random.uniform(0, 20), 1),
        "externalTemperature": round(random.uniform(-20, 10), 1),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }

def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print("Sending telemetry to IoT Hub...")
    try:
        while True:
            telemetry = get_telemetry()
            message = Message(str(telemetry))
            client.send_message(message)
            print(f"Sent message: {message}")
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopped sending messages.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()