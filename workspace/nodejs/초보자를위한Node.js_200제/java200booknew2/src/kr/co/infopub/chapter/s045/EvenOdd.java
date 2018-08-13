package kr.co.infopub.chapter.s045;
// while·Î »ç¿ëÇÏ´Â for
public class EvenOdd {
	public static void showOddnEvenf(int n){
		int temp=n;
		for( ; temp!=1 ; ){
			if(temp%2==1){           // È¦¼ö 
				temp=temp*3+1;       
			}else{                   // Â¦¼ö
				temp/=2;
			}
			System.out.print("["+temp+"] ");
		}
		System.out.println("\n---------------------");
	}
	public static void main(String[] args) {
		showOddnEvenf(122);
	}
}
