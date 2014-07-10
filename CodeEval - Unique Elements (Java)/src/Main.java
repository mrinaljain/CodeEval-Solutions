import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {
	public static void main(String[] args) throws IOException {
		File file = new File(args[0]);
		BufferedReader in = null;
		try {
			in = new BufferedReader(new FileReader(file));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		String line;
	
			while ((line = in.readLine()) != null) {
				String[] nums = line.split(",");
				Set<String> numSet = new HashSet<String>(Arrays.asList(nums));
				if (line.length() > 0) {
					String ans = "";
					for (String num : numSet) {
						ans += num+',';
					}
					ans = ans.substring(0, ans.length()-1);
					System.out.println(ans);
				}
			}
		
	}
}