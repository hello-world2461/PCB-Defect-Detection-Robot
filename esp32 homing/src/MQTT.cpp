#include <Arduino.h>
#include <Wifi.h>


void setupWifi(){
	delay(100);
	Serial.println("\nConnection to");
	Serial.println(ssid);

	WiFi.begin(ssid, password);
}