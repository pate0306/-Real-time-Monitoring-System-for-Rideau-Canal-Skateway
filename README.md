
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
