#include <Arduino.h>
#include <BluetoothSerial.h>

BluetoothSerial SerialBT;  // 创建蓝牙串口对象

// 定义小车运动控制引脚
#define A1 14
#define A2 27
#define B1 26
#define B2 25

// put function declarations here:
void Turn_left();
void Turn_right();
void Go_straight();
void Go_backward();
void Turn_around();
void Stop();

void setup() {
  Serial.begin(9600);  // 串口调试
  SerialBT.begin("ESP32_Car2");  // 初始化蓝牙并设置设备名称
  Serial.println("Bluetooth device is ready to pair.");

  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(B1, OUTPUT);
  pinMode(B2, OUTPUT);
}

void loop() {
  // 检查蓝牙是否有数据可读
  if (SerialBT.available()) {
    String label = SerialBT.readStringUntil('\n');  // 读取分类标签（以换行符为结束符）
    Serial.print("Received label: ");
    Serial.println(label);

    // 根据接收到的分类标签控制小车
    if (label == "qianjin") {  // 前进
      Go_straight();
      Stop(1);
    } else if (label == "houtui") {  // 后退
      Go_backward();
      Stop(1);
    } else if (label == "zuozhuan") {  // 左转
      Turn_left();
      Stop(1);
    } else if (label == "youzhuan") {  // 右转
      Turn_right();
      Stop(1);
    } else if (label == "diaotou") {  // 掉头
      Turn_around();
      Stop(1);
    } else if (label == "tingzhi") {  // 停止
      Stop(1);
    } else {
      Serial.println("Unknown label received.");
    }
  }

  delay(1000);  // 延时以避免处理过于频繁
}

void Turn_left(){
  Stop(1);//先停止
  delay(200);
  digitalWrite(A1, 0); //右轮正转
  digitalWrite(A2, 1);
  digitalWrite(B1, 0); //左轮反转
  digitalWrite(B2, 1);
  delay(300);
  // Go_straight();//前进
}

void Turn_right(){
  Stop(1);
  delay(200);
  digitalWrite(A1, 1); //右轮反转
  digitalWrite(A2, 0);
  digitalWrite(B1, 1); //左轮正转
  digitalWrite(B2, 0);
  delay(300);
  // Go_straight();//前进
}

void Go_straight(){
  digitalWrite(A1, 0); //右轮正转
  digitalWrite(A2, 1);
  digitalWrite(B1, 1); //左轮正转
  digitalWrite(B2, 0);
  delay(2000);
}

void Go_backward(){
  digitalWrite(A1, 1); //右轮反转
  digitalWrite(A2, 0);
  digitalWrite(B1, 0); //左轮反转
  digitalWrite(B2, 1);
  delay(2000);
}

void Turn_around(){
  Stop(1);//先停止
  delay(200);
  digitalWrite(A1, 0); //右轮正转
  digitalWrite(A2, 1);
  digitalWrite(B1, 0); //左轮反转
  digitalWrite(B2, 1);
  delay(600);
  // Go_straight();//前进
}

void Stop(int t){
  digitalWrite(A1, 0); 
  digitalWrite(A2, 0);
  digitalWrite(B1, 0); 
  digitalWrite(B2, 0);
  delay(t);
}
