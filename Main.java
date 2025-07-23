import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    private static int N,M;
    private static int[][] board;
    private static int[][] DP;
    private static int[][] direction = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    public static void main(String[] args) {
        // input
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            board = new int[N][M];
            DP = new int[N][M];
            for(int i=0; i<N; i++){
                String inputs = br.readLine();
                for(int j=0; j<M; j++){
                    if(inputs.charAt(j)=='H') // 구멍: -1
                        board[i][j]=-1;
                    else
                        board[i][j] = Character.getNumericValue(inputs.charAt(j));
                    DP[i][j] = -1; // DP -1 초기화
                }
            }
        }catch(IOException e){}

        // solve
        System.out.println(f(0,0));
    }
    private static int f(int x, int y){
        // System.out.println(String.format("start-f;;\t x: %d, y: %d, DP[x][y]: %d, board[x][y]: %d, \tvisited: %b", x, y, DP[x][y], board[x][y], DP[x][y]!=-1));
        if(DP[x][y]!=-1){ // 무한루프 -> -1
            // return DP[x][y];
            System.out.println(-1);
            System.exit(0);
        }
        for(int[] d: direction){ // DP[x][y] = (4방향 board[x][y] 만큼 떨어진 지점 DP[cx][cy] 최댓값) + 1
            int cx = x + d[0]*board[x][y];
            int cy = y + d[1]*board[x][y];
            if(cx<0 || cy<0 || cx>=N || cy>=M) continue; // 범위 밖
            if(board[cx][cy]==-1) continue; // 구멍
            DP[x][y] = Math.max(DP[x][y], f(cx,cy)+1);
        }
        if(DP[x][y]==-1)DP[x][y]=1;
        // System.out.println(String.format("end - f;;\t x: %d, y: %d, DP[x][y]: %d, board[x][y]: %d", x, y, DP[x][y], board[x][y]));
        return DP[x][y];
    }
}