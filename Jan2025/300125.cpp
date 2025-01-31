class Solution {
public:
    bool isBipartite(vector<int> adj[], int curNode, vector<int>& color, int iniColor) {
        color[curNode] = iniColor;
        for (auto it : adj[curNode]) {
            if (color[it] == iniColor) {
                return false;
            } else if (color[it] == -1) {
                if (!isBipartite(adj, it, color, 1 - iniColor)) {
                    return false;
                }
            }
        }
        return true;
    }

    int bfs(vector<int> adj[], int curNode, int n) {
        vector<bool> vis(n, false);
        queue<int> q;
        q.push(curNode);
        vis[curNode] = true;
        int level = 1;
        while (!q.empty()) {
            int size = q.size();
            while (size--) {
                int node = q.front();
                q.pop();
                for (auto it : adj[node]) {
                    if (!vis[it]) {
                        vis[it] = true;
                        q.push(it);
                    }
                }
            }
            level++;
        }
        return level - 1;
    }

    int getMaxGroup(vector<int> adj[], int n, vector<bool>& vis, int node, vector<int>& levels) {
        int maxgrp = levels[node];
        vis[node] = true;
        for (auto it : adj[node]) {
            if (!vis[it]) {
                maxgrp = max(maxgrp, getMaxGroup(adj, n, vis, it, levels));
            }
        }
        return maxgrp;
    }

    int magnificentSets(int n, vector<vector<int>>& edges) {
        vector<int> adj[n]; 
        for (auto it : edges) {
            int u = it[0] - 1;
            int v = it[1] - 1;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        vector<int> color(n, -1);
        for (int i = 0; i < n; i++) {
            if (color[i] == -1) {  
                if (!isBipartite(adj, i, color, 1)) {
                    return -1;
                }
            }
        }

        vector<int> levels(n, 0);
        for (int i = 0; i < n; i++) {
            levels[i] = bfs(adj, i, n);
        }

        int maxi = 0;
        vector<bool> vis(n, false);
        for (int i = 0; i < n; i++) {
            if (!vis[i]) {
                maxi += getMaxGroup(adj, n, vis, i, levels);
            }
        }
        return maxi;
    }
};