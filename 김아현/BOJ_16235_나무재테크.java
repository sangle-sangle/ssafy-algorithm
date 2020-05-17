import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class BOJ_16235_나무재테크 {
	static int N, M, K;
	static int[][] A;
	static List<Tree> tree;
	static int[][] food;
	static int[] di = {-1,-1,-1,0,0,1,1,1};
	static int[] dj = {-1,0,1,-1,1,-1,0,1};
	
	public static void spring() {
		for (int i = 0; i < tree.size(); i++) {
			Tree tmp = tree.get(i);
			if(food[tmp.x][tmp.y]>=tmp.age) {
				food[tmp.x][tmp.y] = food[tmp.x][tmp.y] - tmp.age;
				tree.get(i).age++;
			}else {
				tree.get(i).age *= -1;
			}
		}
	}
	public static void summer() {
		Collections.sort(tree,new Comparator<Tree>() {
			@Override
			public int compare(Tree o1, Tree o2) {
				return o1.age-o2.age;
			}
		});	
		int list_cut = tree.size();
		for (int i = 0; i < tree.size(); i++) {
			Tree tmp = tree.get(i);
			if(tmp.age>0) {
				list_cut = i;
				break;
			}else {
				food[tmp.x][tmp.y] += (-1*tmp.age)/2;
			}
		}
		tree = tree.subList(list_cut, tree.size());
	}
	public static void fall() {
		for (int i = 0; i < tree.size(); i++) {
			Tree tmp = tree.get(i);
			if(tmp.age%5==0) {
				for (int d = 0; d < 8; d++) {
					int ni = tmp.x + di[d];
					int nj = tmp.y + dj[d];
					if(!isOut(ni,nj)) {
						tree.add(new Tree(ni,nj,1));
					}
				}
			}
		}
	}
	public static void winter() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				food[i][j] += A[i][j];
			}
		}
	}

	public static boolean isOut(int i, int j) {
		if(i<0 || j<0 || i>=N || j>=N) {
			return true;
		}else return false;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt(); // M개의 나무
		K = sc.nextInt(); // K년이 지난 후 살아있는 나무 개수 구하기
		
		A = new int[N][N];
		food = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				A[i][j] = sc.nextInt();
				food[i][j] = 5;
			}
		}
		
		tree = new ArrayList<>();
		
		for (int i = 0; i < M; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			int z = sc.nextInt();
			
			tree.add(new Tree(x-1,y-1,z));
		}
		Collections.sort(tree,new Comparator<Tree>() {
			@Override
			public int compare(Tree o1, Tree o2) {
				return o1.age-o2.age;
			}
		});		
		
		for (int i = 0; i < K; i++) {
			spring();
			summer();
			fall();
			winter();
		}
		
		int ans = 0;
		
		for (int i = 0; i < tree.size(); i++) {
			if(tree.get(i).age>0) {
				ans++;
			}
		}
		
		System.out.println(ans);
	}
	
	public static class Tree{
		int x;
		int y;
		int age;
		
		public Tree() {
		}
		
		public Tree(int x, int y, int z) {
			this.x = x;
			this.y = y;
			age = z;
		}
	}
}
