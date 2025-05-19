#include <SoftwareSerial.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define bt_RX 2
#define bt_TX 3
#define bt_Vin 4
#define led 13
#define buzzer 12

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

Adafruit_SSD1306 oled1(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
SoftwareSerial BTSerial(bt_RX, bt_TX);

struct Item {
  const char* code;
  const char* name;
  int price;
};

Item items[] = {
  {"ITEM001", "Sabun Mandi", 5000},
  {"ITEM002", "Sampo", 10000},
  {"ITEM003", "Mie Instan", 3500},
  {"ITEM004", "Sabun Cuci", 27000},
  {"ITEM005", "air putih", 5000},
  {"ITEM006", "tissue", 8000},
};

const int itemCount = sizeof(items) / sizeof(items[0]);
int totalHarga = 0;

String daftarBarang[10];
int daftarHarga[10];
int jumlahBarang = 0;

void setup() {
  Serial.begin(9600);
  BTSerial.begin(9600);
  pinMode(bt_RX, INPUT);
  pinMode(bt_TX, OUTPUT);
  pinMode(bt_Vin, OUTPUT);
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  digitalWrite(bt_Vin, HIGH);

  if (!oled1.begin(SSD1306_SWITCHCAPVCC, 0x3C)) while (1);

  tampilkanOLED1("📦 Scan Barcode...");
  tampilkanDaftar();

  Serial.println("📦 Input kode (contoh: ITEM001) atau 'BATAL ITEM002'");
}

void loop() {
  static String input = "";
  if (Serial.available()) {
    char c = Serial.read();
    if (c == '\n' || c == '\r') {
      input.trim();
      input.toUpperCase();

      if (input.startsWith("BATAL ")) {
        String kode = input.substring(6);
        batalkanBarang(kode);
      } else {
        prosesBarcode(input);
      }
      input = "";
    } else {
      input += c;
    }
  }
}

void prosesBarcode(String code) {
  for (int i = 0; i < itemCount; i++) {
    if (code == items[i].code) {
      if (jumlahBarang < 10) {
        daftarBarang[jumlahBarang] = items[i].name;
        daftarHarga[jumlahBarang] = items[i].price;
        jumlahBarang++;
        totalHarga += items[i].price;

        Serial.println("✅ Ditambahkan: " + String(items[i].name) + " - Rp" + String(items[i].price));
        tampilkanOLED1("Ditambah:\n" + String(items[i].name) + "\nRp" + String(items[i].price));
        tampilkanDaftar();
        buzz();
        return;
      }
    }
  }
  Serial.println("❌ Kode tidak ditemukan: " + code);
  tampilkanOLED1("❌ Tidak ditemukan:\n" + code);
}

void batalkanBarang(String kode) {
  bool ditemukan = false;
  for (int i = 0; i < jumlahBarang; i++) {
    for (int j = 0; j < itemCount; j++) {
      if (kode == items[j].code && daftarBarang[i] == items[j].name) {
        String nama = daftarBarang[i];
        int harga = daftarHarga[i];

        totalHarga -= harga;
        for (int k = i; k < jumlahBarang - 1; k++) {
          daftarBarang[k] = daftarBarang[k + 1];
          daftarHarga[k] = daftarHarga[k + 1];
        }
        jumlahBarang--;
        ditemukan = true;

        Serial.println("❌ Dibatalkan: " + nama + " - Rp" + String(harga));
        tampilkanOLED1("❌ Dibatalkan:\n" + nama + "\nRp" + String(harga));
        tampilkanDaftar();
        return;
      }
    }
  }

  if (!ditemukan) {
    Serial.println("⚠️ Barang tidak ditemukan untuk dibatalkan: " + kode);
    tampilkanOLED1("⚠️ Tidak ditemukan:\n" + kode);
  }
}

void tampilkanOLED1(String teks) {
  oled1.clearDisplay();
  oled1.setTextSize(1);
  oled1.setTextColor(SSD1306_WHITE);
  oled1.setCursor(0, 0);
  oled1.println(teks);
  oled1.display();
}

void tampilkanDaftar() {
  oled1.clearDisplay();
  oled1.setTextSize(1);
  oled1.setTextColor(SSD1306_WHITE);
  oled1.setCursor(0, 0);
  oled1.println("Daftar Belanja:");
  for (int i = 0; i < jumlahBarang; i++) {
    oled1.print(daftarBarang[i]);
    oled1.print(" - Rp");
    oled1.println(daftarHarga[i]);
  }
  oled1.println("Total: Rp" + String(totalHarga));
  oled1.display();
}

void buzz() {
  digitalWrite(buzzer, HIGH);
  delay(100);
  digitalWrite(buzzer, LOW);
}
