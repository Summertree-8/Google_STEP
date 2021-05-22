//エラー未解決です、、

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
	static String new_dictionary[] = new String [MAX];

	public static void main(String[] args) {

		// 単語を読み込む
		System.out.println("input random word\n");
		Scanner scan = new Scanner(System.in);
        String randomWord = scan.nextLine();
        scan.close();

        makeNewDictionary();

		//新しい辞書を読み込む
	    try {
	    	File file = new File("newwords.txt");
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			int i = 0;
			while (br.ready()) {
				String s = br.readLine();
				if (s == null) break;
				System.out.println("here!!\n"+i);
				new_dictionary[i] = s;
				i++;
			}
			fr.close();

		} catch (Exception e) {
		     e.printStackTrace();
	    }

	    System.out.println(betterSolution(randomWord, newDictionary));

    }

	// アナグラムを見つける
	static String betterSolution(String random_word, String new_dictionary[]) {
	    //文字列をソート
	    char[] charRandomWord = random_word.toCharArray();
	    Arrays.sort(charRandomWord);
	    String sorted_random_word = new String(charRandomWord);

	    //二分探索
	    String anagram = binarySearch(sorted_random_word, new_dictionary);

	    return anagram;
	}

	//新しい辞書を作成
    static void makeNewDictionary(){
	    try{
		    //辞書ファイルを読み込む
	        File wordsfile = new File("C:\\Users\\xingyun\\Documents\\workspace\\Temp\\src\\week1\\words.txt");
	        FileReader fileReader = new FileReader(wordsfile);
	        BufferedReader bufferedReader = new BufferedReader (fileReader);
	        ArrayList<String> sorted = new ArrayList<>();

	       //辞書ファイル内の単語をソート
	        for(int i = 0; i < MAX; i++) {
	        	 String sorte = bufferedReader.readLine();
	 	         char[] c = sorte.toCharArray();
	 	         Arrays.sort(c);
	 	         String sortword = new String(c);
	 	         sorted.add(sortword);
	        }
	        //辞書ファイルをソート
	        Collections.sort(sorted);

	        //新しい辞書ファイルに書き込む
	        File newWordsFile = new File("newwords.txt");
	        FileWriter fileWriter = new FileWriter(newWordsFile);
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

	      if (sorted_random_word == newDictionary[middle]) {
	        anagram = newDictionary[middle];
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
