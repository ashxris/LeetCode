import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() !=t.length()){
            return false;
        }

        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();

        // (character, frequency)

        for (int i = 0;i<s.length();i++){

            char char_s = s.charAt(i);
            char char_t = t.charAt(i);

            map1.put(char_s, map1.getOrDefault(char_s, 0)+1);
            map2.put(char_t, map2.getOrDefault(char_t, 0)+1);

        }


        return map1.equals(map2);
    }
}