package kr.co.infopub.chapter.s072;
import java.util.Iterator;
import java.util.Map;
public class SystemPropertyTest {
	public static void main(String[] args) {
		long namotime=System.nanoTime();
		for(int i=0;i<100000;i++){
			System.out.print("");
		}
		long namotime2=System.nanoTime();//10^-9 nano java5 �߰�
		System.out.println((namotime2-namotime));//1/1000000000��			
		System.out.println(System.getenv("JAVA_HOME")); // ȯ�溯��
		//��� env���ϱ�
		Map<String, String> map=System.getenv();  // ȯ�溯��
		Iterator<String> iter= map.keySet().iterator(); // Map���� Ű ���
		int j=0;
		while(iter.hasNext()){
			String keys=iter.next();
			System.out.println((++j+" ")+keys+" : "+map.get(keys));
		}
	}//main
}
