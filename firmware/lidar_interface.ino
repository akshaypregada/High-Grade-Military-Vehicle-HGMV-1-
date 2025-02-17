#include <SoftwareSerial.h>

#define LIDAR_RX 10
#define LIDAR_TX 11

SoftwareSerial lidarSerial(LIDAR_RX, LIDAR_TX);

void setup() {
    Serial.begin(115200);
    lidarSerial.begin(115200);
}

void loop() {
    if (lidarSerial.available()) {
        int distance = lidarSerial.read();
        Serial.print("LIDAR Distance: ");
        Serial.println(distance);
    }
    delay(100);
}
