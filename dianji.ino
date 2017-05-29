/*
为了看清电机的转动，使用了带齿轮减速箱的微型马达，
由于它的需要的电压低，可以直接使用Arduino板上的5伏电压。
L298N也使Arduino板载 5伏电压
L298N电机驱动自己焊的
*/
//这个电机驱动板使用数字端口4 5 6 7 控制电机
//正确连接你的电机到M1+ M1- M2+ M2-
//数字端口10 11 连接到L298N的使能端接口
//下载代码到Arduino/
// 控制两个直流电机的正反转
//本程序作用两个直流电机先正转一秒 暂停一秒 反转一秒 如此反复
 
 
int IN1=4;
int IN2=5;
int IN3=6;
int IN4=7;

void sport(int direction,int del){
  int i=0;
  if(direction=='f'){
    //正
    Serial.println(direction);
    Serial.println("FFFF");
    while(i<del){
      forward();
      i++;
    }
      stopp();
  }
  else if(direction=='b'){
    //正转
    Serial.println(direction);
    Serial.println("BBBB");
    while(i<3*del){
      back();
      i++;
    }
      stopp();
  }
  else if(direction=='l'){
    //正转
    Serial.println("LLL");
    while(i<del){
      left();
      i++;
    }
      stopp();
  }
  else if(direction=='r'){
    //正转
    Serial.println("RRRR");
    while(i<3*del){
      right();
      i++;
    }
      stopp();
  }
}
void Motor1(boolean flag){
  if(flag)
  {   //正转
      digitalWrite(IN1,HIGH);
      digitalWrite(IN2,LOW);
  }
  else
  {   //反转
      digitalWrite(IN1,LOW);
      digitalWrite(IN2,HIGH);
  }
}
void Motor2(boolean flag){
  if(flag)
  {   //正转
      digitalWrite(IN3,HIGH);
      digitalWrite(IN4,LOW); 
  }
  else
  {   //反转
      digitalWrite(IN3,LOW);
      digitalWrite(IN4,HIGH);
  }
}
void forward(){
     Motor1(true);
     Motor2(true);
}
void back(){
     Motor1(false);
     Motor2(false);
}
void left(){
     Motor1(false);
     Motor2(true);
}
void right(){
     Motor1(true);
     Motor2(false);
}
void stopp(){
      digitalWrite(IN1,LOW);
      digitalWrite(IN2,LOW);
      digitalWrite(IN3,LOW);
      digitalWrite(IN4,LOW); 
}
void setup()
{
  int i;
  for (i=4;i<=7;i++) //为Ardunio 电机驱动板
    pinMode(i,OUTPUT); //设置数字端口4,5,6,7为输出模式
  for (i=4;i<=7;i++) 
    digitalWrite(i,HIGH); //设置数字端口4,5,6,7为HIGH,电机保持不动
  Serial.begin(9600);
}
 
void loop()
{
  if(Serial.available()>0)
  {
    char flag=Serial.read();
    sport(flag,5000);
  }
} 
