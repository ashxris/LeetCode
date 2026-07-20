class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        HashMap <Integer, Integer> map = new HashMap<>();

        for (int i = 0; i<nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i],0)+1);
        }

        List<Integer>[] bucket = new List[nums.length+1];
        for (int c =0; c<bucket.length;c++){
            bucket[c]= new ArrayList<>();
        }

        for(int key : map.keySet()){
            int freq = map.get(key);
            bucket[freq].add(key);
        }

        int[] result = new int [k];
        int count=0;

        for(int bk = bucket.length-1; bk>=0 && count<k; bk--){
            if(!bucket[bk].isEmpty()){
                for (int item : bucket[bk]){
                    result[count++]=item;
                    
                    if(count==k){
                        return result;
                    }
                }
            
            }
        }

        return result;

        
    }
}