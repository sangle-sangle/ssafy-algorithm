import java.util.Scanner;

public class BOJ_1238_파티 {
	static int N, M, X;
	static int[][] map;
	static int[] distance;
	
	public static void dijkstra(int v) {
		distance = new int[N+1];
		boolean[] check = new boolean[N+1];
		
		for (int i = 1; i < N+1; i++) {
			distance[i] = Integer.MAX_VALUE;
		}
		
		distance[v] = 0;
		check[v] = true;
		
		for (int i = 1; i < N+1; i++) {
			if(!check[i] && map[v][i]!=0) {
				distance[i] = map[v][i];
			}
		}
		
		for (int j = 0; j < N-1; j++) { //N-1번 돌면 됨
			//최소 index 찾기
			int min = Integer.MAX_VALUE;
			int min_index = -1;
					
			for (int i = 1; i < N+1; i++) {
				if(!check[i] && distance[i]!=Integer.MAX_VALUE) {
					if(min>distance[i]) {
						min = distance[i];
						min_index = i;
					}
				}
			}
			
			check[min_index] = true;
			
			for (int i = 1; i < N+1; i++) {
				if(!check[i] && map[min_index][i]!=0) {
					distance[i] = Integer.min(distance[i], distance[min_index]+map[min_index][i]);
				}
			}
		}
	}
	
	public static int dijkstra_2(int v, int K) {
		int[] distance = new int[N+1];
		boolean[] check = new boolean[N+1];
		
		for (int i = 1; i < N+1; i++) {
			distance[i] = Integer.MAX_VALUE;
		}
		
		distance[v] = 0;
		check[v] = true;
		
		for (int i = 1; i < N+1; i++) {
			if(!check[i] && map[v][i]!=0) {
				distance[i] = map[v][i];
			}
		}
		
		for (int j = 0; j < N-1; j++) { //N-1번 돌면 됨
			//최소 index 찾기
			int min = Integer.MAX_VALUE;
			int min_index = -1;
					
			for (int i = 1; i < N+1; i++) {
				if(!check[i] && distance[i]!=Integer.MAX_VALUE) {
					if(min>distance[i]) {
						min = distance[i];
						min_index = i;
					}
				}
			}
			check[min_index] = true;
			
			for (int i = 1; i < N+1; i++) {
				if(!check[i] && map[min_index][i]!=0) {
					distance[i] = Integer.min(distance[i], distance[min_index]+map[min_index][i]);
				}
			}
			if(min_index==K) {
				break;
			}
		}
		return distance[K];
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		X = sc.nextInt();
		map = new int[N+1][N+1];
		
		for (int i = 1; i < M+1; i++) {
			map[sc.nextInt()][sc.nextInt()]=sc.nextInt();
		}
		int max = 0;
		dijkstra(X); // X에서 각자 집으로 가는것
		
		// X로 가는것
		int[] go = new int[N+1];
		for (int i = 1; i < N+1; i++) {
			go[i]=dijkstra_2(i,X); // X에 도달하면 멈추고 값 반환하는 dijkstra
		}
		
		// 각 인덱스 오고가는것 합 중 max 찾기
		for (int i = 1; i < N+1; i++) {
			max = Integer.max(max, go[i]+distance[i]);
		}
		System.out.println(max);
	}
}


