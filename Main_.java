import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// class Point{
//     int x, y;
//     Point(int x, int y){
//         this.x=x;
//         this.y=y;
//     }
// }

public class Main_ {
    private static int R,C,T;
    private static int[][] home;
    private static int airPurifier1; // i좌표 (j==0)
    private static int airPurifier2;
    private static final int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}};
    public static void main(String args[]){
        getInputs();
        int answer = solve();
        System.out.println(answer);
    }
    private static void getInputs(){
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            String[] inputs = br.readLine().split(" ");
            R = Integer.parseInt(inputs[0]);
            C = Integer.parseInt(inputs[1]);
            T = Integer.parseInt(inputs[2]);
            for(int i=0; i<R; i++){
                inputs = br.readLine().split(" ");
                for(int j=0; j<C; j++){
                    home[i][j] = Integer.parseInt(inputs[j]);
                }
            }
        }catch(IOException e){
            System.out.println(e);
        }
    }
    private static int solve(){
        setAirPurifier();
        for(int i=0; i<T; i++){ // T초 흐름
            spreadsDustForOneSecond();
            airPurifierWorksForOneSecond();
        }
        // getSumOfDust();;;;;;;;;
        return -1;
    }
    // 공기청정기 위치 저장
    private static void setAirPurifier(){
        for(int i=0; i<R; i++){
            if(home[i][0]==-1){
                airPurifier1 = i;
                airPurifier2 = i+1;
                break;
            }
        }
    }
    // 1초 동안 먼지 확산
    private static void spreadsDustForOneSecond(){
        for(int i=0; i<R; i++){
            for(int j=0; j<C; j++){
                if(home[i][j]!=-1 && home[i][j]!=0){ // 확산할 먼지가 있는 칸
                    int dustToSpread = home[i][j]/5; // 확산되는 먼지 값
                    int spreadDirCount = 0; // 확산된 방향 수
                    for(int[] dir: directions){ // 4방향으로 확산
                        int nextI = i+dir[0];
                        int nextJ = j+dir[1];
                        if(!isValidDust(nextI, nextJ)) continue; // 확산 불가능한 칸 건너뜀
                        spreadDirCount++;
                        home[nextI][nextJ] += dustToSpread;
                    }
                    home[i][j] = home[i][j] - dustToSpread * spreadDirCount; // 확산된 칸 남은 먼지 계산
                }
            }
        }
    }
    // 1초 동안 공기청정기 작동
    private static void airPurifierWorksForOneSecond(){
        home[airPurifier1-1][0] = home[airPurifier1-2][0];
        //....................................................
    }
    // 먼지가 확산 가능한 위치인지 판별
    private static boolean isValidDust(int i, int j){
        return !(i<0 || j<0 || i>=R || j>=C || (j==0 && (i==airPurifier1 || i==airPurifier2)));
    }
}
