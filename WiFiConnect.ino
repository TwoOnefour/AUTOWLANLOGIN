#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#define WIFI_SSID "WHUT-DORM"  // 这里写你宿舍里wifi的名称，如我这里是WHUT-DORM

const char *username = "your_username"; // 你的上网用户名
const char *password = "your_password"; // 你的上网密码
static WiFiClient client;
const int LED = LED_BUILTIN;

void setup() {
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
  wifiInit(WIFI_SSID); // 连接wifi获取dhcp分配的ip
  connectWiFi();  // 抓包获取的api认证
}

void loop() {
  // 在这里写你的联网逻辑
}

void wifiInit(const char *ssid) {
  WiFi.begin(ssid);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("WiFi not Connect");
  }
  Serial.println("Connected to AP");
  Serial.print("IP is:");
  Serial.println(WiFi.localIP());
}

void connectWiFi() {
  const char *keys[] = { "Location" };
  HTTPClient http;
  http.collectHeaders(keys, 1);
  http.begin(client, "http://captive.apple.com");
  String url = http.header("Location");
  // String url = "http://172.30.21.100/api/r/" + nasId + "?userip=" + WiFi.localIP().toString() + "&wlanacname=&acip=172.30.1.220&acname=WHUT-YQ-Bras-ME60";
  http.begin(client, url);
  http.GET();
  http.end();
  
  HTTPClient http1;
  String url1 = "http://172.30.21.100/api/account/login";
  http1.begin(client, url1);
  http1.addHeader("Content-Type", "application/x-www-form-urlencoded");
  http1.addHeader("X-Requested-With", "XMLHttpRequest");
  
  char *query_string = new char[83 + 1 + strlen(password)];
  char *tmp = "userIpv4=&userMac=&captcha=&captchaId=&switchip=&username=";
  strcat(tmp, username);
  strcat(tmp, "&password=");
  strcat(tmp, password);
  const char *nasId = "&nasId=" + url[27] + url[28];
  strcat(tmp, nasId);
  strcpy(query_string, tmp);
  int httpCode = http1.POST(query_string);
  if (httpCode > 0) {
    if (httpCode == HTTP_CODE_OK) {
      Serial.println("Portal verifying passed.");
      digitalWrite(LED, HIGH);
    }
  }
  http1.end();
}
