#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
/*
 * static const uint8_t D1   = 5;
static const uint8_t D2   = 4;
static const uint8_t D3   = 0;
static const uint8_t D4   = 2;
static const uint8_t D5   = 14;
static const uint8_t D6   = 12;
 */

#define FIREBASE_HOST "hydroponics-195ff.firebaseio.com"
#define FIREBASE_AUTH "wONJb26IDPsNu25HEPoYzkHjmQF0QLqtqdXZ9UD0"
#define WIFI_SSID "Sakshi"
#define WIFI_PASSWORD "9739082528"

int ppmhigh = 5;
int ppmlow = 4;
int temphigh = 0;
int templow = 2;
int phhigh = 14;
int phlow = 12;

String ppm = "";
String temp = "";
String ph = "";
void setup()
{

    Serial.begin(9600);
    pinMode(ppmhigh, OUTPUT);
    pinMode(ppmlow, OUTPUT);
    pinMode(temphigh, OUTPUT);
    pinMode(templow, OUTPUT);
    pinMode(phhigh, OUTPUT);
    pinMode(phlow, OUTPUT);

    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(500);
    }
    Serial.print("Connected to ");
    Serial.println(WIFI_SSID);
    Serial.print("IP Address is : ");
    Serial.println(WiFi.localIP());
    Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
}

void loop()
{

    ppm = Firebase.getString("ppm");

    if (ppm == "2")
    {
        digitalWrite(ppmlow, HIGH);
        digitalWrite(ppmhigh, LOW);
    }
    else if (ppm == "1")
    {
        digitalWrite(ppmlow, LOW);
        digitalWrite(ppmhigh, HIGH);
    }

    else
    {
        digitalWrite(ppmlow, LOW);
        digitalWrite(ppmhigh, LOW);
    }

    temp = Firebase.getString("temp");
    if (temp == "2")
    {
        digitalWrite(templow, HIGH);
        digitalWrite(temphigh, LOW);
    }
    else if (temp == "1")
    {
        digitalWrite(templow, LOW);
        digitalWrite(temphigh, HIGH);
    }

    else
    {
        digitalWrite(templow, LOW);
        digitalWrite(temphigh, LOW);
    }

    ph = Firebase.getString("pH");
    if (ph == "2")
    {
        digitalWrite(phlow, HIGH);
        digitalWrite(phhigh, LOW);
    }
    else if (ph == "1")
    {
        digitalWrite(phlow, LOW);
        digitalWrite(phhigh, HIGH);
    }

    else

    {
        digitalWrite(phlow, LOW);
        digitalWrite(phhigh, LOW);
    }
}