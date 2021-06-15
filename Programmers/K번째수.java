class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] resultArr = new int[commands.length];
        for (int i = 0; i < commands.length; i++) {
            int[] save = new int[commands[i][1]-commands[i][0]+1];
            int index = 0;
            for (int j = commands[i][0]-1; j < commands[i][1]; j++) {
                save[index] = array[j];
                index++;
            }
            for (int j = 0; j < save.length-1; j++) {
                for (int k = 0; k < save.length-1; k++) {
                    if (save[k] > save[k+1]) {
                        int tmp = save[k];
                        save[k] = save[k+1];
                        save[k+1] = tmp;
                    }
                }
            }
            resultArr[i] = save[commands[i][2]-1];
        }
        return resultArr;
    }
}
