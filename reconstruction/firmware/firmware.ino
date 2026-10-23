// Reconstructed ESP32/UNO telemetry. Original cloud credentials are not embedded.
#include <Arduino.h>
#include <DHT.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#if defined(ESP32)
const int SOIL=34,DHT_PIN=27,ONEWIRE_PIN=14,PIR=25;const int ADC_MAXIMUM=4095;
#else
const int SOIL=A0,DHT_PIN=2,ONEWIRE_PIN=3,PIR=4;const int ADC_MAXIMUM=1023;
#endif
DHT dht(DHT_PIN,DHT11);OneWire oneWire(ONEWIRE_PIN);DallasTemperature water(&oneWire);unsigned long last=0;
void setup(){Serial.begin(115200);dht.begin();water.begin();pinMode(PIR,INPUT);}
void loop(){unsigned long now=millis();if(now-last<2000)return;last=now;
 float t=dht.readTemperature(),h=dht.readHumidity();water.requestTemperatures();float probe=water.getTempCByIndex(0);int soil=analogRead(SOIL);
 Serial.print("{\"uptime_ms\":");Serial.print(now);Serial.print(",\"source\":\"hardware\",\"soil_raw\":");Serial.print(soil);
 Serial.print(",\"temperature_c\":");if(isnan(t))Serial.print("null");else Serial.print(t);
 Serial.print(",\"humidity_percent\":");if(isnan(h))Serial.print("null");else Serial.print(h);
 Serial.print(",\"probe_temperature_c\":");if(probe==DEVICE_DISCONNECTED_C)Serial.print("null");else Serial.print(probe);
 Serial.print(",\"motion\":");Serial.print(digitalRead(PIR)==HIGH?"true":"false");Serial.println("}");}
