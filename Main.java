import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
    private static boolean isNum(char c){
        return c!='+' && c!='-' && c!='*' && c!='/';
    }
    public static void main(String args[]){
        String[] chars = {"a", "+", "b", "*", "c", "*", "d", "+", "e", "-", "h"};
        String[] s2;
        for(int i=1; i<chars.length; i+=2){
            if(chars[i]=="/"||chars[i]=="*"){
                String sss = chars[i-1]+chars[i+1]+chars[i];
                chars[i-1]="";
                chars[i]="";
                chars[i+1]=sss;
            }
        }
        String[] filtered = Arrays.stream(chars)
                            .filter(s -> !s.isEmpty())
                            .toArray(String[]::new);
        System.out.println(Arrays.toString(filtered));


        for(int i=1; i<filtered.length; i+=2){
            if(filtered[i]=="+"||filtered[i]=="-"){
                String sss = filtered[i-1]+filtered[i+1]+filtered[i];
                filtered[i-1]="";
                filtered[i]="";
                filtered[i+1]=sss;
            }
        }
        System.out.println(Arrays.toString(filtered));
    }
}
