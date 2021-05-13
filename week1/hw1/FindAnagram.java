package week1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class FindAnagram {

	static int MAX = 84093;
	static String array1[];
	static String array2[];

	public static void main(String[] args) {

		// 単語ファイル読み込む
		try {

		} catch (Exception e) {
		     e.printStackTrace();
	    }
		String betterSolution(RandomWord, Dictionary);


    }

	// アナグラムを見つける
	static String betterSolution(String RandomWord, String Dictionary) {
	    //文字列をソート
	    char[] charRandomWord = RandomWord.toCharArray();
	    Arrays.sort(charRandomWord);
	    String SortedRandomWord = new String(charRandomWord);

	    //新しい辞書を読み込む

	    //二分探索
	    return (BinarySearch(SortedRandomWord, NewDictionary));
	}

	//新しい辞書を作成
    static void makeNewDictionary(File newwordsFile){
	    try{
		    //辞書ファイルを読み込む
	        File wordsfile = new File("C:\\Users\\xingyun\\Documents\\workspace\\Temp\\src\\week1\\words.txt");
	        FileReader fileReader = new FileReader(wordsfile);
	        BufferedReader bufferedReader = new BufferedReader (fileReader);
	        String data= bufferedReader.readLine();

	        //辞書ファイルをソート
	        while(data != null) {
	        	data
	        }

	        //新しい辞書ファイルに書き込む
	        FileWriter fileWriter = new FileWriter("test.txt");
	        BufferedWriter bw=new BufferedWriter(new FileWriter(newwordsFile));
	        for() {
	        	fileWriter.write();
	        }
	        fileWriter.close();
	        fileReader.close();

	    }catch(IOException e){
	        e.printStackTrace();
	    }
    }

	//二分探索
	static String BinarySearch(String SortedRandomWord, String NewDictionary) {
    	int left = 0;
	    int right = MAX;
	    String anagram = "";

	    while (left <= right) {
	      int middle = (left + right) / 2;

	      if (SortedRandomWord == NewDictionary) {
	        anagram = NewDictionary[middle];
	        break;
	      }
	      else if (SortedRandomWord < NewDictionary) {
	        right = middle;
	      }
	      else {
	        left = middle;
	      }
	    }
	    return anagram;
    }


}
