package kr.co.infopub.chapter.s042;
// ¹Ýº¹¹®
public class Temperature {
	public static void main(String[] args) {
		for (int i = 0; i < 101; i++) {
			double fahrenheit=9.0/5*i+32;    //for ºí·Ï º¯¼ö
			System.out.printf("¼·¾¾ %dµµ= È­¾¾ %.2fµµ.\n",i,fahrenheit);
		}
	}
}
