#include "Adafruit_NeoPixel.h"

#define PIN 4
#define LED_COUNT 110

Adafruit_NeoPixel strip = Adafruit_NeoPixel(LED_COUNT, PIN, NEO_GRB + NEO_KHZ800);

void setup()
{
  strip.begin();
  strip.show(); 
  
  Serial.begin(250000); 
  while (!Serial) {;}
  Serial.println("Ready");
}

void loop(){
  uint8_t buffer[LED_COUNT*3] = {0};
  uint8_t received_count = 0;
  
  Serial.readBytes((char*)buffer, LED_COUNT*3);
  
  for(int index = 0; index < LED_COUNT; ++index){
    strip.setPixelColor(index, buffer[(index * 3) + 1], buffer[(index * 3) + 2], buffer[index * 3]);
  }
  strip.show();
}
