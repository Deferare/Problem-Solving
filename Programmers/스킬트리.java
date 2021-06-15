class Solution {
    public static int solution(String skill, String[] skill_trees) {
        int cnt = 0;
        for (int i = 0; i < skill_trees.length; i++) {
            String save = "";int check2 = 0;
            for (int j = 0; j < skill_trees[i].length(); j++) {
                for (int k = 0; k < skill.length(); k++) {
                    if (skill_trees[i].charAt(j) == skill.charAt(k)) {
                        check2 = 1;
                        save += skill_trees[i].charAt(j);
                        break;
                    }
                }
            }
            if (check2 == 0) {
                cnt++; continue;
            }
            if (save.length() > 0) {
                int check = 0;
                for (int j = 1; j <= skill.length(); j++) {
                    String saveSub = "";
                    for (int k = 0; k < j; k++) {
                        saveSub += skill.charAt(k);
                    }
                    if (save.equals(saveSub)) {
                        cnt++;
                        break;
                    }
                }
            }
        }
        return cnt;
    }
}
