package week1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class FindAnagram {

	static int MAX = 84093;
	static String array1[];
	static String array2[];

	public static void main(String[] args) {

		// 単語を読み込む
		Scanner scan = new Scanner(System.in);
        String random_word = scan.nextLine();
        scan.close();

		//新しい辞書を読み込む
	    try {
	    	File file = new File("newwords.txt");
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			String str = "";
			while (true) {
				String s = br.readLine();
				System.out.println(betterSolution(random_word, new_dictionary));
				if (s==null) break;
			}
			fr.close();

		} catch (Exception e) {
		     e.printStackTrace();
	    }

    }

	// アナグラムを見つける
	static String betterSolution(String random_word, String new_dictionary[]) {
	    //文字列をソート
	    char[] charRandomWord = random_word.toCharArray();
	    Arrays.sort(charRandomWord);
	    String sorted_random_word = new String(charRandomWord);

	    //二分探索
	    String anagram = BinarySearch(sorted_random_word, new_dictionary);

	    return anagram;
	}

	//新しい辞書を作成
    static void makeNewDictionary(File newwordsFile){
	    try{
		    //辞書ファイルを読み込む
	        File wordsfile = new File("https://github.com/xharaken/step2/tree/master/anagram/words.txt");
	        FileReader fileReader = new FileReader(wordsfile);
	        BufferedReader bufferedReader = new BufferedReader (fileReader);
	        ArrayList<String> sorted = new ArrayList<>();

	       //辞書ファイル内の単語をソート
	        for(int i = 0; i < MAX; i++) {
	        	 String data= bufferedReader.readLine();
	 	         char[] c = data.toCharArray();
	 	         Arrays.sort(c);
	 	         String sortword = new String(c);
	 	         sorted.add(sortword);
	        }
	        //辞書ファイルをソート
	        Collections.sort(sorted);

	        //新しい辞書ファイルに書き込む
	        File newwordsfile = new File("newwords.txt");
	        FileWriter fileWriter = new FileWriter(newwordsfile);
	        BufferedWriter bw = new BufferedWriter(fileWriter);

            FileInputStream inStream = new FileInputStream(wordsfile);
            FileOutputStream outStream = new FileOutputStream(newwordsfile);
            byte[] buf = new byte[256];
            int len;
            while((len = inStream.read(buf)) != -1){
            	outStream.write(buf);
            }
            outStream.flush();
	        fileWriter.close();
	        fileReader.close();

	    }catch(IOException e){
	        e.printStackTrace();
	    }
    }

	//二分探索
	static String BinarySearch(String sorted_random_word, String new_dictionary[]) {
    	int left = 0;
	    int right = MAX;
	    String anagram = "";

	    while (left <= right) {
	      int middle = (left + right) / 2;

	      if (sorted_random_word == new_dictionary[middle]) {
	        anagram = new_dictionary[middle];
	        break;
	      }
	      else if (sorted_random_word.compareTo(new_dictionary[middle]) < 0) {
	        right = middle;
	      }
	      else {
	        left = middle;
	      }
	    }
	    return anagram;
    }


}
