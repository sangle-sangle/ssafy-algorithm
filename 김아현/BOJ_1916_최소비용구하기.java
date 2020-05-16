import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1916_최소비용구하기 {
	static int N, M;
	static int start,end;
	static int[][] bus;
	static boolean[][] connect;
	static int ans;
	
	public static int dijkstra(int s, int e) {
		int[] cost = new int[N+1];
		boolean[] check = new boolean[N+1];
		
		for (int i = 1; i < N+1; i++) {
			cost[i] = Integer.MAX_VALUE;
		}
		
		cost[s] = 0;
		check[s] = true;
		
		for (int i = 1; i < N+1; i++) {
			if(!check[i] && connect[s][i]) {
				cost[i] = bus[s][i];
			}
		}
			
		for (int j = 0; j < N-1; j++) {
			
			int min = Integer.MAX_VALUE;
			int min_index = -1;

			for (int i = 1; i < N+1; i++) {
				if(!check[i] && cost[i] != Integer.MAX_VALUE) {
					if(min > cost[i]) {
						min = cost[i];
						min_index = i;
					}
				}				
			}
			check[min_index] = true;
			
			for (int i = 1; i < N+1; i++) {
				if(!check[i] && connect[min_index][i]) {
					cost[i] = Integer.min(cost[i], cost[min_index]+bus[min_index][i]);
				}
			}
		}
		return cost[e];
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		bus = new int[N+1][N+1];
		connect = new boolean[N+1][N+1];
		
		int a, b, c;
		for (int i = 0; i < M; i++) { //두 정점 사이에 간선이 여러개 올 수 있음. 최소비용일 때만 저장
			st = new StringTokenizer(br.readLine()," ");
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			if(!connect[a][b] && bus[a][b]==0) {
				bus[a][b]=c;
			}else {
				bus[a][b] = Integer.min(bus[a][b], c);
			}
			connect[a][b] = true;
		}
		
		st = new StringTokenizer(br.readLine()," ");
		start = Integer.parseInt(st.nextToken());
		end = Integer.parseInt(st.nextToken());
		
		ans = dijkstra(start, end);
		System.out.println(ans);
	}
}
