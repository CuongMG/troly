#include <WiFi.h>
#include <WebServer.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "cosmic";
const char* password = "aptx48694062";

WebServer server(80);

#define led_blue 2
#define led_yellow 18

HTTPClient client;
DynamicJsonDocument json(1024);

DynamicJsonDocument postJson(1024);


void handleRequest(){
  client.begin("https://tro-ly-ao-c6d33-default-rtdb.firebaseio.com/esp_get/.json");
  client.addHeader("Content-Type", "application/json");

  int httpCode = client.GET();
  if(httpCode > 0){
    String content = client.getString();
    Serial.println(content);
    deserializeJson(json, content);
    if(json["blue"] == 1){
      digitalWrite(led_blue, 1);
    }else{
      digitalWrite(led_blue, 0);
    }
    if(json["yellow"] == 1){
      digitalWrite(led_yellow, 1);
    }else{
      digitalWrite(led_yellow, 0);
    }
  }
}

void postToFirebase(){
  client.begin("https://tro-ly-ao-c6d33-default-rtdb.firebaseio.com/esp_patch/.json");
  client.addHeader("Content-Type", "application/json");

  int temper = random(30, 40);
  int humi = random(80, 100);

  // if(digitalRead(led_blue) == 1){
  //   postJson["esp_get"]["blue"] = 1;
  // }else{
  //   postJson["esp_get"]["blue"] = 0;
  // }
  // if(digitalRead(led_yellow) == 1){
  //   postJson["esp_get"]["yellow"] = 1;
  // }else{
  //   postJson["esp_get"]["yellow"] = 0;
  // }

  postJson["temperature"] = temper;
  postJson["humidity"] = humi;

  String postBody;
  serializeJson(postJson, postBody);

  int httpResponseCode = client.PATCH(postBody);

  if(httpResponseCode>0){
    Serial.print("Post json success: ");
    Serial.println(httpResponseCode);
  }
  else{
    Serial.print("Post json failed: ");
    Serial.println(httpResponseCode);
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(led_blue, OUTPUT);
  pinMode(led_yellow, OUTPUT);

  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED);
  Serial.print(WiFi.localIP());

  // client.begin("https://tro-ly-ao-c6d33-default-rtdb.firebaseio.com/.json")
  // client.addHeader("Content-Type", "application/json");
}

void loop() {
  postToFirebase();
  delay(1000);
  handleRequest();
}
