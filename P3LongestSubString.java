class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.equals("") || s==null) return 0;
        int maxlen = 1;
        int len;
        int begin = 0;
        String sub;
        char c;
        for (int end = 1; end < s.length(); end++){
            c = s.charAt(end);
            sub = s.substring(begin, end);
            if (sub.contains(Character.toString(c))){
                len = sub.length();
                begin = begin + sub.indexOf(c) + 1;
            } else {
                len = sub.length() + 1;
            }
            if (len > maxlen) maxlen = len;
            System.out.println("subString " +sub + " :: " + c + " maxlen " + maxlen);

        }
        return maxlen;
    }
}


// Solution using HashSet
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character>set=new HashSet<>();
        int maxLength=0;
        int left=0;
        for(int right=0;right<s.length();right++){
           
            if(!set.contains(s.charAt(right))){
                set.add(s.charAt(right));
                maxLength=Math.max(maxLength,right-left+1);
                
            }else{
                while(s.charAt(left)!=s.charAt(right)){
                    set.remove(s.charAt(left));
                    left++;
                }
                set.remove(s.charAt(left));left++;
                set.add(s.charAt(right));
            }
            
        }
        return maxLength;
    }
}
