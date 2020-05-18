import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class BOJ_16235_��������ũ {
	static int N, M, K;
	static int[][] A;
	static List<Tree> tree;
	static List<Tree> dtree, newtree;
	static int[][] food;
	static int[] di = {-1,-1,-1,0,0,1,1,1};
	static int[] dj = {-1,0,1,-1,1,-1,0,1};
	
	public static void spring() {
		for(Iterator<Tree> itt = tree.iterator();itt.hasNext();) { // iterator ����� ����
			Tree t = itt.next();
			if(food[t.x][t.y]>=t.age) {
				food[t.x][t.y] = food[t.x][t.y] - t.age;
				t.age++;
			}else {
				dtree.add(t);
				itt.remove(); // iterator ���� ��ȯ�߿� ����Ʈ ���� ����
			}
		}
	}
	public static void summer() {
		for(Tree t:dtree) {
			food[t.x][t.y] += t.age/2;
		}
		dtree.clear();
	}
	public static void fall() {
		for(Tree t:tree) {
			if(t.age%5==0) {
				for (int d = 0; d < 8; d++) {
					int ni = t.x + di[d];
					int nj = t.y + dj[d];
					if(!isOut(ni,nj)) {
						newtree.add(new Tree(ni,nj,1));
					}
				}
			}
		}
		tree.addAll(0, newtree);
		newtree.clear();
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
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] strArr = str.split(" ");
		
		N = Integer.parseInt(strArr[0]);
		M = Integer.parseInt(strArr[1]); // M���� ����
		K = Integer.parseInt(strArr[2]); // K���� ���� �� ����ִ� ���� ���� ���ϱ�
		
		A = new int[N][N];
		food = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			str = br.readLine();
			strArr = str.split(" ");
			for (int j = 0; j < N; j++) {
				A[i][j] = Integer.parseInt(strArr[j]);
				food[i][j] = 5;
			}
		}
		
		tree = new LinkedList<>();
		dtree = new LinkedList<>();
		newtree = new LinkedList<>();
		
		for (int i = 0; i < M; i++) {
			str = br.readLine();
			strArr = str.split(" ");
			int x = Integer.parseInt(strArr[0]);
			int y = Integer.parseInt(strArr[1]);
			int z = Integer.parseInt(strArr[2]);
			
			tree.add(new Tree(x-1,y-1,z));
		}
		
		Collections.sort(tree);
		
		for (int i = 0; i < K; i++) {
			spring();
			summer();
			fall();
			winter();
		}
		
		System.out.println(tree.size());
	}
	
	public static class Tree implements Comparable<Tree>{
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

		@Override
		public int compareTo(Tree o) {
			return this.age-o.age;
		}
	}
}
