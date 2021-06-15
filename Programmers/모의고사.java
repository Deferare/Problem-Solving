class Solution {
    public int[] solution(int[] answers) {
        int[] player1 = {1,2,3,4,5}; int[] player2 = {2,1,2,3,2,4,2,5}; int[] player3 = {3,3,1,1,2,2,4,4,5,5};
        int player1Cnt = 0; int player2Cnt = 0; int player3Cnt = 0;
        int play1Index = 0; int play2Index = 0;  int play3Index = 0;
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == player1[play1Index]) {
                player1Cnt++;
            }
            if (play1Index == 4)
                play1Index = 0;
            else play1Index++;

            if (answers[i] == player2[play2Index]) {
                player2Cnt++;
            }
            if (play2Index == 7)
                play2Index = 0;
            else play2Index++;

            if (answers[i] == player3[play3Index]) {
                player3Cnt++;
            }
            if (play3Index == 9)
                play3Index = 0;
            else play3Index++;

        }
        if (player1Cnt > player2Cnt && player1Cnt > player3Cnt) {
            int[] result = {1};
            return result;
        }
        else if (player2Cnt > player1Cnt && player2Cnt > player3Cnt) {
            int[] result = {2};
            return result;
        }
        else if (player3Cnt > player1Cnt && player3Cnt > player2Cnt) {
            int[] result = {3};
            return result;
        }
        else if (player1Cnt == player2Cnt && player1Cnt == player3Cnt){
            int[] result = {1,2,3};
            return result;
        }
        else if (player1Cnt == player2Cnt && player1Cnt != player3Cnt){
            int[] result = {1,2};
            return result;
        }
        else if (player2Cnt == player3Cnt && player1Cnt != player3Cnt){
            int[] result = {2,3};
            return result;
        }
        else if (player1Cnt == player3Cnt && player1Cnt != player2Cnt){
            int[] result = {1,3};
            return result;
        }
        int[] result = {1,2,3};
        return result;
    }
}
