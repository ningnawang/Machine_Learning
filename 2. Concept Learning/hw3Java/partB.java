import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class partB {
	private static String USAGE = "Please insert valid location path";
	@SuppressWarnings("resource")
	public static void main(String[] args) throws IOException {
			
		//Shrink VS using traing data
		String[] VS = new String[16];
		int countLine = 0;
		try {
			Scanner scanner = new Scanner(new File("4Cat-Train.labeled"));
			
			//write result to a file
			File output = new File("partB5.txt");
			FileWriter fw = new FileWriter(output);
			BufferedWriter bw = new BufferedWriter(fw);
			
			//read file line by line
			while (scanner.hasNextLine()) {
				String line = scanner.nextLine();
				countLine++;
				String[] eachLine = line.split("\\s");
				String[] instance = deleteAttribute(eachLine, 5);
					
				//List-Then-Eliminate Algorithm
				int[] temp = ListThenEliminateAlgo(instance);
				VS[temp[0]] = temp[1] + "";				
			}
			bw.close();
		} catch (FileNotFoundException e) {
			System.err.print(USAGE);
			return;
		}
		VSSize(VS);
		
		
		
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
				String[] instance = deleteAttribute(lineNoRisk, 4);
				
				//store the vote;
				int temp = ListThenEliminateAlgo(instance)[0];
				if (VS[temp].equals("0")) {
					sb.append("0" + " " + (int)VSSize(VS) + ",");
				} else if (VS[ListThenEliminateAlgo(instance)[0]].equals("1")) {
					sb.append((int)VSSize(VS) + " " + "1" + ",");
				} else {
					sb.append((int)(VSSize(VS)/2)  + " " + (int)(VSSize(VS)/2) + ",");
				}
			}	
		} catch (FileNotFoundException e) {
			System.err.println("File Not Found" + args[0]);
			System.err.print(USAGE);
			return;
		}
		
		
		//print out the size of the input space
		System.out.println((int)Math.pow(2, 4));
		
		//print out the number of concept space
		double conceptSize = Math.pow(2, Math.pow(2, 4));
		System.out.println((int)conceptSize);
		
		//print out the size of version space
		System.out.println((int)VSSize(VS));
		
		//print out the vote
		String[] vote = sb.toString().split(",");
		for (int i = 0; i < vote.length; i++) {
			System.out.println(vote[i]);
		}		
	}
	
	//Deleting all attributes and only leaving values
	public static String[] deleteAttribute(String[] line, int resultSize) {
		String[] instance = new String[resultSize];
		int index = 0;
		for (int i = 1; i < line.length; i++) {
			if (i % 2 != 0) {
				instance[index] = line[i];
				index++;
			}
		}
		return instance;
	}

	//List-Then-Eliminate Algorithm
	public static int[] ListThenEliminateAlgo(String[] instance) {
		int result[] = new int[2];
		if (instance[0].equals("Male")) {
			result[0] = 0;
		} else {
			result[0] = 1;
		}
		if (instance[1].equals("Young")) {
			result[0] <<= 1;
		} else {
			result[0] <<= 1;
			result[0] += 1;
		}
		if (instance[2].equals("No")) {
			result[0] <<= 1;
		} else {
			result[0] <<= 1;
			result[0] += 1;
		}
		if (instance[3].equals("No")) {
			result[0] <<= 1;
		} else {
			result[0] <<= 1;
			result[0] += 1;
		}
		if (instance.length == 5) {
			if (instance[4].equals("low")) {
				result[1] = 0;
			} else {
				result[1] = 1;
			}
		} else {
			result[1] = -1;
		}
		return result;
	}
	
	//count the size of version space 
	public static double VSSize(String[] VS) {
		int pow = 0;
		for (int i = 0; i < VS.length; i++) {
			if (VS[i] == null || VS[i] == "?") {
				VS[i] = "?";
				pow++;
			}
		}
		return Math.pow(2, pow);
	}
}
