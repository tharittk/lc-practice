class Solution {
    public String reverseWords(String s) {
        int i = 0;
        Stack<String> stack = new Stack<String>();
        while (i < s.length()){

            while ( i < s.length() && s.charAt(i) == ' '){
                //System.out.println("skipping i " + i + "/"+s.length());
                i++;
            }


            StringBuilder sb = new StringBuilder();
            while (i < s.length() && s.charAt(i) != ' '){
                //System.out.println("char " + s.charAt(i));
                sb.append(s.charAt(i));
                i++;
            }

            String word = sb.toString();
            //System.out.println("pushing  " + word + "len " + word.length());
            if (word.length() > 0) stack.push(word);
        }

        StringBuilder rev = new StringBuilder();
        while (!stack.empty()){
            rev.append(stack.pop());

            if(!stack.empty()) rev.append(' ');
        }
        return rev.toString();
        
    }
}
