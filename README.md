
# README.md

## Scenario Description

To ensure citizen safety, the City of Ottawa has implemented a real-time data-gathering platform across three popular ice skating locations—Dow's Lake, Fifth Avenue, and the National Arts Centre (NAC). The platform collects critical metrics such as Ice Thickness, Surface Temperature, Snow Accumulation, and External Temperature. This data enables the city to make informed decisions regarding the opening or closing of skating rinks.

- Sensors are installed across the three locations to collect data continuously.
- Incoming data is processed in real time to support decision-making regarding rink availability.
- The collected data is stored in Azure Storage for future analysis and to aid in long-term planning and safety assessments.

## System Architecture

- **IoT Sensors:** Collect real-time data from the Rideau Canal, Dow's Lake, Fifth Avenue, and NAC.
- **Azure IoT Hub:** All sensor data is collected and centralized in the IoT Hub.
- **Azure Stream Analytics:** The data is analyzed and processed as required, such as calculating average ice thickness or snow accumulation on the surface.
- **Azure Blob Storage:** The processed data is stored in CSV/JSON formats for future analysis.

## Implementation Details

### IoT Sensor Simulation

- **Description:** Simulated IoT sensors generate and send data to Azure IoT Hub every 10 seconds, including location, ice thickness, surface temperature, snow accumulation, external temperature, and timestamp.
- **JSON Payload Structure:**

```json
{
    "location": "Dow's Lake",
    "iceThickness": 25.5,
    "surfaceTemperature": -3.2,
    "snowAccumulation": 12.3,
    "externalTemperature": -7.5,
    "timestamp": "2024-12-02T15:30:00Z"
}
```

### 3.2 Azure IoT Hub Configuration

#### Steps to Set Up IoT Hub:
1. **Create an IoT Hub**:
   - Navigate to the Azure portal.
   - Create a new IoT Hub and select the **Standard** tier to enable advanced features like message routing.
2. **Add a Device**:
   - In the IoT Hub, go to the **Devices** section.
   - Add a new device by specifying a unique **Device ID**.
   - Copy the **Connection String** for the newly created device; it will be used in the simulation script for authentication and data transmission.

---

### 3.3 Azure Stream Analytics Job

#### Steps to Configure the Job:
1. **Create a Stream Analytics Job**:
   - In the Azure portal, search for **Stream Analytics Jobs** and click **Create**.
   - Provide a name, select a resource group, and choose **Cloud** as the hosting environment.
   - Click **Create** to initialize the job.

2. **Set Up Input**:
   - Navigate to the **Inputs** section and click **Add**.
   - Select **IoT Hub** as the input source.
   - Configure the input with:
     - Existing IoT Hub namespace.
     - Authorization policy: Use `iothubowner`.
     - Consumer group: Choose `$Default` or create a new one.
     - Data format: Set as **JSON**.

3. **Set Up Output**:
   - Go to the **Outputs** section and click **Add**.
   - Choose **Blob Storage** as the output destination.
   - Configure the output with:
     - Select an Azure Storage Account.
     - Specify or create a container for storing processed data.
     - (Optional) Add a folder structure for file organization.
     - Select the output format: **JSON** or **CSV**.

4. **Write the Query**:
   - Create a SQL-like query to process data from the input.
   - Example Query:
     ```sql
     SELECT
         IoTHub.ConnectionDeviceId AS DeviceId,
         AVG(iceThickness) AS AvgIceThickness,
         MAX(snowAccumulation) AS MaxSnowAccumulation,
         System.Timestamp AS EventTime
     INTO
         [output]
     FROM
         [input]
     GROUP BY
         IoTHub.ConnectionDeviceId, TumblingWindow(minute, 5)
     ```


