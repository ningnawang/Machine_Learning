import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class partA {
	private static String USAGE = "Please insert valid location path";
	@SuppressWarnings("resource")
	public static void main(String[] args) throws IOException {
			
		//Learn a hypothesis using traing data
		String[] hypo = {null, null, null, null, null, null, null, null, null};
		int countLine = 0;
		try {
			Scanner scanner = new Scanner(new File("9Cat-Train.labeled"));
			
			//write result to a file
			File output = new File("partA4.txt");
			FileWriter fw = new FileWriter(output);
			BufferedWriter bw = new BufferedWriter(fw);
			
			//read file line by line
			while (scanner.hasNextLine()) {
				String line = scanner.nextLine();
				countLine++;
				String[] eachLine = line.split("\\s");
				if (eachLine[eachLine.length - 1].equals("high")) {
					
					//Deleting the attribute and value of risk
					String[] lineNoRisk = Arrays.copyOf(eachLine, eachLine.length - 2);
					
					//Deleting all attributes and only leaving values
					String[] instance = new String[9];
					int index = 0;
					for (int i = 1; i < lineNoRisk.length; i++) {
						if (i % 2 != 0) {
							instance[index] = lineNoRisk[i];
							index++;
						}
					}
					
					//Find-S Algorithm
					hypo = findS(hypo, instance);
				}
				
				if (countLine % 30 == 0) {
					for (int i = 0; i < hypo.length; i++) {
						if (i == hypo.length - 1) {
							bw.write(hypo[i]);
							bw.flush();
							bw.newLine();
							break;
						}
						bw.write(hypo[i] + "\t");
						bw.flush();
					}
				}
			}
			bw.close();
		} catch (FileNotFoundException e) {
			System.err.print(USAGE);
			return;
		}
		
		
		
		
		//Test code using development dataset
		if (args[0].length() == 0) {
			System.err.print(USAGE);
			return;
		}
		
		StringBuffer sb = new StringBuffer();
		try {
			Scanner scannerTest = new Scanner(new File(args[0]));
			while(scannerTest.hasNextLine()) {
				String line = scannerTest.nextLine();
				String[] eachLine = line.split("\\s");
				
				//Deleting the attribute and value of risk
				String[] lineNoRisk = Arrays.copyOf(eachLine, eachLine.length - 2);
				
				//Deleting all attributes and only leaving values
				String[] instance = new String[9];
				int index = 0;
				for (int i = 1; i < lineNoRisk.length; i++) {
				if (i % 2 != 0) {
					instance[index] = lineNoRisk[i];
					index++;
					}
				}
				//print out the result;
				sb.append(resultFromFindS(hypo, instance) + " ");
			}	
		} catch (FileNotFoundException e) {
			System.err.println("File Not Found" + args[0]);
			System.err.print(USAGE);
			return;
		}
		
		
		//print out the size of the input space
		System.out.println((int)Math.pow(2, 9));
		
		//print out the number of decimal digits in |C|
		double conceptSize = Math.pow(2, Math.pow(2, 9));
		int decimalDigit = 1;
		while ((long) conceptSize / 10 > 0) {
			decimalDigit++;
			conceptSize = conceptSize / 10;
		}
		System.out.println(decimalDigit);
		
		//print out the size of hypothesis space
		System.out.println((int)(Math.pow(3, 9)) + 1);
		
		//print the misclassification rate
		String[] classification = sb.toString().split("\\s");
		double rate = misclassificationRate(new File(args[0]), classification);
		System.out.println(rate);
		
		//print the classification of each instance
		for (int i = 0; i < classification.length; i++) {
			System.out.println(classification[i]);
		}
		
	}
	
	//Find S algorithm
	public static String[] findS(String[] hypo, String[] instance) {
		if (hypo[0] == null) {
			hypo = instance;
			return hypo;
		}
		for (int i = 0; i < hypo.length; i++) {
			if (!hypo[i].equals(instance[i])) {
				hypo[i] = "?";
			}
		}
		return hypo;
	}
	
	//Test dataset based on Find S algorithm
	public static String resultFromFindS(String[] hypo, String[] instance) {
		for (int i = 0; i < instance.length; i++) {
			if (hypo[i] == "?") continue;
			else if (!instance[i].equals(hypo[i])) {
				return "low";
			}
		}
		return "high";
	}
	
	//calculate the misclassification rate
	public static double misclassificationRate(File correctInput, String[] classification) throws FileNotFoundException {
		int index = 0;
		double wrongCounter = 0.0;
		Scanner scannerTest = new Scanner(correctInput);
		while(scannerTest.hasNextLine()) {
			String line = scannerTest.nextLine();
			String[] eachLine = line.split("\\s");
			if (!eachLine[eachLine.length - 1].equals(classification[index])) {
				wrongCounter++;
			}
			index++;			
		}
		double rate = (wrongCounter / (double) index);
		return rate;
	}
}
