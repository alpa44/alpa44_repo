package kr.co.infopub.chapter.s089;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

public class BillboardMain3 {
 public static void main(String[] args) {
	String newUrls="https://www.billboard.com/charts/hot-100/";
	URL url=null;
	try {
		url= new URL(newUrls);    // �ּ� ã��
		// �ּ����� ���� �ȱ�
		BufferedReader reader = new BufferedReader(  
				     new InputStreamReader(url.openStream(), "euc-kr"), 8);
		String line = null;
		while ((line = reader.readLine()) != null){  // �� �پ� �о 
			if(!line.trim().equals("")){             // ������ �ƴϸ� ����Ѵ�.
				System.out.println(line.trim());
			}
		}
	} catch (Exception e) {
		System.out.println("Billboard Parsing error !!! ");
	} 
 }
}