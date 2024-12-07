# import time
# from HPMA115S0 import HPMA115S0

# def main():
#     # Define the serial port for the sensor
#     sensor_port = "/dev/serial0"  # Update with the actual port

#     # Initialize the sensor
#     sensor = HPMA115S0(sensor_port)
#     print("Initializing the HPMA115S0 sensor...")
#     sensor.init()
#     time.sleep(1)

#     try:
#         print("Starting to read PM2.5 and PM10 data...")
#         while True:
#             # Read particle measurement
#             if sensor.readParticleMeasurement():
#                 pm2_5 = sensor._pm2_5
#                 pm10 = sensor._pm10
#                 print(f"PM2.5: {pm2_5} ug/m3, PM10: {pm10} ug/m3")
#             else:
#                 print("Failed to read particle data.")
            
#             # Delay before the next reading
#             time.sleep(2)

#     except KeyboardInterrupt:
#         print("\nStopping sensor measurement...")
#     finally:
#         # Stop sensor measurement and close the connection
#         sensor.stopParticleMeasurement()
#         sensor._serial.close()
#         print("Sensor stopped and connection closed.")

# if __name__ == "__main__":
#     main()

import time
from HPMA115S0 import HPMA115S0
import google.generativeai as genai

# Configure the Google Generative AI API
genai.configure(api_key="")  # Replace with your actual API key

def main():
    # Define the serial port for the sensor
    sensor_port = "/dev/serial0"  # Update with the actual port

    # Initialize the sensor
    sensor = HPMA115S0(sensor_port)
    print("Initializing the HPMA115S0 sensor...")
    sensor.init()
    time.sleep(1)

    # Initialize the Generative AI model
    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        print("Starting to read PM2.5 and PM10 data and analyzing with Generative AI...")
        while True:
            # Read particle measurement
            if sensor.readParticleMeasurement():
                pm2_5 = sensor._pm2_5
                pm10 = sensor._pm10
                print(f"PM2.5: {pm2_5} ug/m3, PM10: {pm10} ug/m3")

                # Create the input prompt for the model
                prompt = (
                    f"The PM2.5 value is {pm2_5} ug/m3 and the PM10 value is {pm10} ug/m3. "
                    f"Analyze these readings and provide insights or recommendations in one sentence only."
                )

                # Send the prompt to the model and get the response
                response = model.generate_content(prompt)

                # Print the AI-generated response
                print("AI Response:", response.text)

            else:
                print("Failed to read particle data.")

            # Delay before the next reading and AI request
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nStopping sensor measurement...")
    finally:
        # Stop sensor measurement and close the connection
        sensor.stopParticleMeasurement()
        sensor._serial.close()
        print("Sensor stopped and connection closed.")

if __name__ == "__main__":
    main()
