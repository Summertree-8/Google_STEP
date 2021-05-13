package week1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

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

		//単語ファイルから読み込み
		try {
	    	File file = new File(wordsfile);
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			while (br.ready()) {
				String s = br.readLine();
			}
			br.close();
		} catch (Exception e) {
		     e.printStackTrace();
	    }
	}

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

	int charScore[] = {1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4};

		//ファイルから文字列に
		//文字列からcharに
	    //アルファベットごとの点数
		//単語を作る
		//点数が高いものがあるか判定
		//更新
		//新しいファイルに出力

}