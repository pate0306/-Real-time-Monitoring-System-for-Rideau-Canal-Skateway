from datetime import datetime
import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=assignmentiothub007.azure-devices.net;DeviceId=DowsLake;SharedAccessKey=q7uvwEMEYytAn14RElH+x1SpNpYx2lK4kKwyOpJgDS0="

def get_telemetry():
    return {
        "location":"Dow's Lake",
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