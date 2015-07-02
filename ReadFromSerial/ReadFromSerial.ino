#include "Adafruit_NeoPixel.h"

#define PIN 6
#define LED_COUNT 60

Adafruit_NeoPixel strip = Adafruit_NeoPixel(LED_COUNT, PIN, NEO_GRB + NEO_KHZ800);

uint8_t started = 0;
uint8_t defaultColor[] = {0,10,25};
uint8_t buffer[LED_COUNT*3] = {0};

void setup()
{
  //Setup Default Color; Only turns on every other LED to show that Arduino is in a default state
  for(int index = 0; index < LED_COUNT * 3; index+=6){
    buffer[index] = defaultColor[0];
    buffer[index + 1] = defaultColor[1];
    buffer[index + 2] = defaultColor[2];
  }
  
  strip.begin();
  
  Serial.begin(250000); 
  while (!Serial) {;}
  Serial.println("Ready");
  started = 1;
  
}

void loop(){

  uint8_t received_count = 0;

  if(started){
    Serial.readBytes((char*)buffer, LED_COUNT*3);
  }
  for(int index = 0; index < LED_COUNT; ++index){
    strip.setPixelColor(index, buffer[(index * 3)], buffer[(index * 3) + 1], buffer[(index * 3) + 2]);
  }
  strip.show();
}
