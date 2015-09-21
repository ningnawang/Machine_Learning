import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class question3 {
	
	public static String USAGE = "Please input the correct location path of a text file.";
		
	public static void main(String[] args) {
		//special condition
		if (args.length == 0) {
			System.err.println(USAGE);
			return;
		}
		//set stop words list
		try {
			HashSet<String> stopWords = new HashSet<String>();
			Scanner scan = new Scanner(new File(args[1]));
			while (scan.hasNextLine()) {
				String stop = scan.nextLine();
				stop = stop.toLowerCase();
				stopWords.add(stop);
			}
			
			//set frequency and remove stop words
			HashMap<String, Integer> map = new HashMap<String, Integer>();
			try {
				Scanner scanner = new Scanner(new File(args[0]));
				while (scanner.hasNextLine()) {
					String line = scanner.nextLine();
					String[] sentence = line.split("\\W");
					for (String word : sentence) {
						if (!word.matches("[a-zA-Z]+")) {//remove stop words
							continue;
						}
						word = word.toLowerCase();
						if (stopWords.contains(word)) {
							continue;
						}
						if (map.containsKey(word)) {
							map.put(word, map.get(word) + 1);
						}
						else {
							map.put(word, 1);
						}
					}
					Set<String> keySet = map.keySet();
					String[] result = keySet.toArray(new String[0]);
					Arrays.sort(result);
					for (int i = 0; i < result.length; i++) {
						if (i == result.length - 1) {
							System.out.print(result[i] + ":" + map.get(result[i]));
						}
						else {
							System.out.print(result[i] + ":" + map.get(result[i]) + ",");
						}
					}
				}
			} catch (FileNotFoundException e) {
				System.err.println("Input file Not Found" + args[0]);
				System.err.println(USAGE);
				return;
			}
			
		} catch (FileNotFoundException e1) {
			System.err.println("StopWords file Not Found" + args[0]);
			System.err.println(USAGE);
			return;
		}		
	}
}
