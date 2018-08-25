package kr.co.infopub.chapter.s088;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Date;
// ����
public class BillFiles {
	public static void main(String[] args) {
		File f=new File("billboard");    // billboard ���丮
		File[] fd=f.listFiles();         // �ٷ� �Ʒ� ���ϵ�(�ڽ� ����)
		for (File ff : fd) {
			String fname=ff.getName();   // ���ϸ�
			String post=fname.substring(fname.lastIndexOf(".")+1); 
			System.out.println(fname+"  "+post);  // �̸�, Ȯ����
			System.out.println(ff.getAbsolutePath());  // ��ü ���
			System.out.println(new Date(ff.lastModified()));  //������
			try(BufferedReader br=new BufferedReader(
				      new FileReader(ff.getAbsolutePath()))) {
				String msg="";
				while((msg=br.readLine())!=null){
				    System.out.println(msg);
				}
			} catch (Exception e) {
				System.out.println(e);
			}
			System.out.println("--------------------------------------");
		}
	}
}