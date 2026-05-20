#include <Wire.h>
#include "MAX30105.h"
#include "heartRate.h"
MAX30102 particleSensor;

#define BLYNK_TEMPLATE_ID "TMPL3TFBS3p0F"
#define BLYNK_TEMPLATE_NAME "Nadi Tantra Project"
#define BLYNK_AUTH_TOKEN "4WgP9grTJxJHBHgNkWJ7w1nsn4vWQ173r"
#define BLYNK_PRINT Serial
#include <BlynkSimpleEsp32.h> // Change to Esp32 library

char auth[] = BLYNK_AUTH_TOKEN;
// type your wifi name
char ssid[] = "OnePlus"; 
// type your wifi password
char pass[] = "aditya88"; 
// Increase this for more averaging. 4 is good.
const byte RATE_SIZE = 4; 
byte rates[RATE_SIZE]; // Array of heart rates
byte rateSpot = 0;
long lastBeat = 0; // Time at which the last beat occurred

float beatsPerMinute;
int beatAvg;

void setup() {
    Serial.begin(115200);
    Serial.println("Initializing...");
    Blynk.begin(auth, ssid, pass);
    
    // Initialize sensor
    if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) { 
    // Use default I2C port, 400kHz speed
    Serial.print("MAX30102 was not found");
    Serial.println("Please check wiring/power. ");
    while (1);
    }
    Serial.print("Place your index finger on the ");
    Serial.println("sensor with steady pressure.");
    // Configure sensor with default settings
    particleSensor.setup(); 
    // Turn Red LED to low to indicate sensor is running
    particleSensor.setPulseAmplitudeRed(0x0A); 
    // Turn off Green LED
    particleSensor.setPulseAmplitudeGreen(0); 
}

void loop() {
    long irValue = particleSensor.getIR();

    if (checkForBeat(irValue) == true) {
    // We sensed a beat!
    long delta = millis() - lastBeat;
    lastBeat = millis();

    beatsPerMinute = 60 / (delta / 1000.0);

    if (beatsPerMinute < 255 && beatsPerMinute > 20) {
        // Store this reading in the array
        rates[rateSpot++] = (byte)beatsPerMinute; 
        rateSpot %= RATE_SIZE; // Wrap variable

        // Take average of readings
        beatAvg = 0;
        for (byte x = 0 ; x < RATE_SIZE ; x++) {
        beatAvg += rates[x];
        }
        beatAvg /= RATE_SIZE;

        // Send beatAvg to Blynk app
        // Assuming you use Virtual Pin V3
        Blynk.virtualWrite(V3, beatAvg); 
    }
    }

    Serial.print("IR=");
    Serial.print(irValue);
    Serial.print(", BPM=");
    Serial.print(beatsPerMinute);
    Serial.print(", Avg BPM=");
    Serial.println(beatAvg);

    if (irValue < 50000) {
    Serial.print(" No finger?");
    Serial.println();
    }

    Blynk.run(); // Process Blynk tasks
}
\end{verbatim}
