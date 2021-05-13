//かなり混沌としています。ごめんなさい、、！

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

public class FindAnagramUpdated {

	static String wordsfile;

	public static void main(String[] args) {

		System.out.println("input file name\n");
		//単語ファイルの指定
		wordsfile = args[0];

		//実行
		find_higher_score();

	}

	static void find_higher_score() {

		ArrayList<String> random_words = new ArrayList<String>();
		ArrayList<String> anagram = new ArrayList<String>();
		//単語ファイルから読み込み
		try {
	    	File file = new File(wordsfile);
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			while (br.ready()) {
				String s = br.readLine();
				random_words.add(s);
			}
			br.close();
		} catch (Exception e) {
		     e.printStackTrace();
	    }

		// 辞書の各単語に対してアナグラムを見つける
		for() {
			find_anagram(random_words,)
		}
	}

	//アナグラムであれば出力
	static void find_anagram(String ramdom_word, String dictionary_word) {
		int i = 0;

		for(int j = 0; j < ramdom_word.length(); j++) {
			if(ramdom_word.charAt(i) != dictionary_word.charAt(i)) {
				break;
			}
			i++;
		}
		if(i == ramdom_word.length()) {
			//新しいファイルに出力
			try{
			    File file = new File("new"+wordsfile+".txt");
			    FileWriter filewriter = new FileWriter(file);
			    BufferedWriter bw = new BufferedWriter(filewriter);
			    String s = dictionary_word;
			    anagram.add(s);
			    filewriter.close();
			}catch(IOException e){
			     System.out.println(e);
			}
	    }
	}

	//アルファベットも個数をカウント
	static int[] count_char(String x) {
		int count []= new int[26];
		char c[] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
			      'v', 'w', 'x', 'y', 'z' };
		for(int i = 0; i < x.length(); i++) {
			for(int j = 0; j < 26; j++) {
				if(x.charAt(i) == c[j]) {
					count[j]++;
				}
			}
		}
		return count;
	}

	//アルファベットごとの点数
	int char_score[] = {1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4};

}