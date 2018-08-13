package kr.co.infopub.chapter.s093;
import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
public class RequestFromBillboardHot {
	boolean isConnection=false;
	ArrayList<String> htmls=new ArrayList<String>();
	ArrayList<Billbaord> billbaords=new ArrayList<Billbaord>();

	public ArrayList<Billbaord> getBillbaords() {
		return billbaords;
	}
	String timedate="";
	public String getTimedate() {
		return timedate;
	}
	public RequestFromBillboardHot(){
		billbaords.clear();
	}
	public void getAllHtml(String newUrls){
		htmls.clear();
		InputStream inputStream;
		URL url=null;
		try {
			url= new URL(newUrls);
			HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
			inputStream = new BufferedInputStream(urlConnection.getInputStream());
			BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream, "euc-kr"), 8);
			String line = null;
			while ((line = reader.readLine()) != null)
			{
				if(!line.trim().equals("")){

					htmls.add(line.trim());
				}
			}
			inputStream.close();
			isConnection=true;

		} catch (Exception e) {
			isConnection = false;
			System.out.println(e);
		}
	}
	public String getTimeDate(String newUrls){
		String s="";
		InputStream inputStream;
		URL url=null;
		try {
			url= new URL(newUrls);
			HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
			inputStream = new BufferedInputStream(urlConnection.getInputStream());
			BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream, "euc-kr"), 8);
			String line = null;
			while ((line = reader.readLine()) != null)
			{
				if(!line.trim().equals("")){
					if(line.trim().contains("<time datetime=")){
						s=line.trim();
						s=s.substring(0,s.indexOf(">")-1);//<time datetime="2016-08-13
						s=s.substring(s.indexOf("\"")+1).trim();//2016-08-13
						break;
					}
				}
			}
			inputStream.close();
			isConnection=true;
		} catch (Exception e) {
			isConnection = false;
			System.out.println(e);
		}
		return s;
	}
	public synchronized void getBillboardData(String msg){
		billbaords.clear();
		for (int i=0; i<htmls.size(); i++) {
			String ss=htmls.get(i);
			if(ss.contains(msg)){
				String rank=ss.substring(ss.indexOf("chart-row--")+"chart-row--".length());
				rank=rank.substring(0,rank.indexOf("js")-1).trim();
				int j=1;
				String imageurl=htmls.get(i+j);

				while(true){
					if(imageurl.contains("chart-row__image")){
						if(imageurl.contains("https://") && imageurl.contains(".jpg")){
							break;
						}else{
							imageurl="data-imagesrc=\"https://www.billboard.com/"
									+ "images/pref_images/q__________.jpg\"";
							break;
						}
					}else{
						j++;
						imageurl=htmls.get(i+j);
					}
				}
				imageurl=imageurl.substring(imageurl.indexOf("https://"));
				imageurl=imageurl.substring(0,imageurl.indexOf(".jpg")+".jpg".length());
				int kt=1;
				String song=htmls.get(i+j+kt);
				while(true){
					if(song.contains("chart-row__song")){
						song=htmls.get(i+j+kt);
						break;
					}else{
						j++;
						song=htmls.get(i+j+kt);
					}
				}
				song=song.substring(song.indexOf(">")+1);
				song=song.substring(0, song.indexOf("<"));
				System.out.println(song);
				int k=1;
				String artisturl=htmls.get(i+j+k);
				while(true){
					if(artisturl.contains("chart-row__artist")){
						artisturl=htmls.get(i+j+k+1);
						break;
					}else{
						j++;
						artisturl=htmls.get(i+j+k);
					}
				}
				if(artisturl.contains("Featuring")){
					artisturl=artisturl.substring(0,artisturl.indexOf("Featuring"));
				}
				String artist=artisturl.substring(artisturl.lastIndexOf("/")+1);
				artist=toArtis(artist);
				int m=1;
				String lastweek=htmls.get(i+j+k+m);
				while(true){
					if(lastweek.contains("chart-row__last-week")){
						break;
					}else{
						j++;
						lastweek=htmls.get(i+j+k+m);
					}
				}
				int n=1;
				lastweek=htmls.get(i+j+k+m+n);
				while(true){
					if(lastweek.contains("chart-row__value")){
						break;
					}else{
						j++;
						lastweek=htmls.get(i+j+k+m+n);
					}
				}
				lastweek=lastweek.substring(lastweek.indexOf(">")+1);
				lastweek=lastweek.substring(0,lastweek.indexOf("<")).trim();
				Billbaord board=new Billbaord(
						toInt(rank), replace(song),
						toInt(__toStr(lastweek)),
						imageurl, replace(artisturl), replace(artist));
				billbaords.add(board);
			}
		}
	}
	public String replace(String msg){
		String ss=msg;
		ss=ss.replaceAll("&#039;", "'");
		ss=ss.replaceAll("&amp;", "&");
		ss=ss.replaceAll("&quot;", "\"");
		return ss.trim();
	}
	private String __toStr(String lastweek){
		return lastweek.contains("--")?101+"":lastweek;
	}
	private int toInt(String msg){
		return Integer.parseInt(msg==null ?"-1":msg.trim());
	}
	public String toArtis(String msg){
		return msg.replaceAll("-", " ");
	}
	public void printHtml(){
		for (String dto : htmls) {
			System.out.println(dto);
		}
	}
	public void printBillboard(){
		for (Billbaord dto : billbaords) {
			System.out.println(dto);
		}
	}
	public static void main(String[] args) {
		RequestFromBillboardHot rfw=new RequestFromBillboardHot();
		String a="https://www.billboard.com/charts/hot-100/";
		String rs=rfw.getTimeDate(a);
		System.out.println(rs);
		rfw.getAllHtml(a+rs);
		String str="<article class=\"chart-row";
		rfw.getBillboardData(str);
		rfw.printBillboard();
	}
}
