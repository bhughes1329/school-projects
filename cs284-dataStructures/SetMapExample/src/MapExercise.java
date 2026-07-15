import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class MapExercise {
    public static void main(String[] args){
        File f = new File("README.txt");
        Scanner scanner;
        HashMap<String, Integer> wordList = new HashMap<String, Integer>();
        try {
            scanner = new Scanner(f);
            while(scanner.hasNextLine()){
                String line = scanner.nextLine();
                String[] words = line.replaceAll("\\p{Punct}", "").split("\\s+");
                for(int i = 0; i<words.length; i++)
                {
//                    System.out.println(words[i]);
                    if(wordList.containsKey(words[i].toLowerCase())) {
                        int count = wordList.get(words[i].toLowerCase());
                        wordList.put(words[i].toLowerCase(), ++count);
                    }else wordList.put(words[i].toLowerCase(), 1);
                }
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        scanner.close();
        for(String key : wordList.keySet()){
            System.out.println(key+" "+wordList.get(key));
        }

    }
}
