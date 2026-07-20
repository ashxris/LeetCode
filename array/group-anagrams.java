// https://www.youtube.com/watch?v=vzdNOK2oB2E&t=5s

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap <String, List> map = new HashMap<>();

        for(String s: strs){

            int[] count = new int[26];
            
            for (char c: s.toCharArray()){
                count[c - 'a']++;
            }

            StringBuilder sb = new StringBuilder();
            for (int i: count){
                sb.append('#');
                sb.append(i);
            }

            String key = sb.toString();

            if(!map.containsKey(key)){
                map.put(key, new ArrayList<String>());
            }

            map.get(key).add(s);

        }

        return new ArrayList(map.values());

        
    }
}