import processing.serial.*; // seri port kütüphanesi
import java.awt.event.KeyEvent; 
import java.io.IOException;

Serial serialPort;
String angle = "", distance = "", data = "";
String noObject;
float pixsDistance;
int iAngle, iDistance;
int index1 = 0, index2 = 0;
PFont orcFont;

void setup() {  
 size (1366, 700);
 smooth();
 serialPort = new Serial(this, "COM5", 57600); // seri port ayarı
 serialPort.bufferUntil('.');
}

void draw() {
  fill(98,245,31);
  noStroke();
  fill(0,4); 
  rect(0, 0, width, 1010); 
  fill(98,245,31); // yeşil renk
  drawRadar(); 
  drawLine();
  drawObject();
  drawText();
}

void serialEvent (Serial serialPort) { 
  data = serialPort.readStringUntil('.');
  data = data.substring(0,data.length()-1);
  index1 = data.indexOf(","); 
  angle= data.substring(0, index1); 
  distance= data.substring(index1+1, data.length()); 
  iAngle = Integer.valueOf(angle);
  iDistance = Integer.valueOf(distance);
}

void drawRadar() {
  pushMatrix();
  translate(683,700); 
  noFill();
  strokeWeight(2);
  stroke(98,245,31);
  // draws the arc lines
  arc(0,0,1300,1300,PI,TWO_PI);
  arc(0,0,1000,1000,PI,TWO_PI);
  arc(0,0,700,700,PI,TWO_PI);
  arc(0,0,400,400,PI,TWO_PI);
  // draws the angle lines
  line(-700,0,700,0);
  line(0,0,-700*cos(radians(30)),-700*sin(radians(30)));
  line(0,0,-700*cos(radians(60)),-700*sin(radians(60)));
  line(0,0,-700*cos(radians(90)),-700*sin(radians(90)));
  line(0,0,-700*cos(radians(120)),-700*sin(radians(120)));
  line(0,0,-700*cos(radians(150)),-700*sin(radians(150)));
  line(-700*cos(radians(30)),0,700,0);
  popMatrix();
}

void drawObject() {
  pushMatrix();
  translate(683,700); 
  strokeWeight(9);
  stroke(255,10,10); // kırmızı renk
  pixsDistance = iDistance*22.5; 
  // 40 cm ye kadar ölçer
  if(iDistance<40)
    line(pixsDistance*cos(radians(iAngle)),-pixsDistance*sin(radians(iAngle)),700*cos(radians(iAngle)),-700*sin(radians(iAngle)));
  popMatrix();
}

void drawLine() {
  pushMatrix();
  strokeWeight(9);
  stroke(30,250,60);
  translate(683,700); 
  line(0,0,700*cos(radians(iAngle)),-700*sin(radians(iAngle))); 
  popMatrix();
}

void drawText() { 
  pushMatrix();
  if(iDistance>40)
    noObject = "Out of Range";
  else
    noObject = "In Range";
  fill(0,0,0);
  noStroke();
  rect(0, 1010, width, 1080);
  fill(98,245,31);
  textSize(25);
  text("10cm", 800,690);
  text("20cm", 950,690);
  text("30cm", 1100,690);
  text("40cm", 1250,690);
  textSize(40);
  text("Object: " + noObject, 240, 1050);
  text("Angle: " + iAngle +" °", 1050, 1050);
  text("Distance: ", 1380, 1050);
  if(iDistance<40)
    text("        " + iDistance +" cm", 1400, 1050);
  textSize(25);
  fill(98,245,60);
  translate(390+960*cos(radians(30)),780-960*sin(radians(30)));
  rotate(-radians(-60));
  text("30°",0,0);
  resetMatrix();
  translate(490+960*cos(radians(60)),920-960*sin(radians(60)));
  rotate(-radians(-30));
  text("60°",0,0);
  resetMatrix();
  translate(630+960*cos(radians(90)),990-960*sin(radians(90)));
  rotate(radians(0));
  text("90°",0,0);
  resetMatrix();
  translate(760+960*cos(radians(120)),1000-960*sin(radians(120)));
  rotate(radians(-38));
  text("120°",0,0);
  resetMatrix();
  translate(840+900*cos(radians(150)),920-960*sin(radians(150)));
  rotate(radians(-60));
  text("150°",0,0);
  popMatrix(); 
}