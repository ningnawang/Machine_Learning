import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class question1 {
	public static String USAGE = "Please input the correct location path of a text file.";
	
	public static void main(String[] args) {
		if (args.length == 0) {
			System.err.println(USAGE);
			return;
		}
		
		HashSet<String> set = new HashSet<String>();
		try {
			Scanner scanner = new Scanner(new File(args[0]));
			while (scanner.hasNextLine()) {
				String line = scanner.nextLine();
				String[] sentence = line.split("\\s");
				for (String word : sentence) {
					word = word.toLowerCase();
					if (set.contains(word)) {
						continue;
					}
					else {
						set.add(word);
					}
				}
				String[] result = set.toArray(new String[0]);
				Arrays.sort(result);
				for (int i = 0; i < result.length; i++) {
					if (i == result.length - 1) {
						System.out.print(result[i]);
					}
					else {
						System.out.print(result[i] + ",");
					}
				}
			}

		} catch (FileNotFoundException e) {
			System.err.println("File Not Found" + args[0]);
			System.err.println(USAGE);
			return;
		}
		
	}
}
