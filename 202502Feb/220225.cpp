/**
 * https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/submissions/1551496098/?envType=daily-question&envId=2025-02-22
 * 
 * 
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    public:
        TreeNode* recoverFromPreorder(string& T) {
            TreeNode* root=NULL;
            vector<pair<TreeNode*, int>> st;
            const int n=T.size();
            int D=0;
            for(int i=0; i<n; i++){
                int x=0;
                while(isdigit(T[i])){
                    x=10*x+T[i]-'0';
                    i++;
                }
            //    cout<<x<<"| ";
                TreeNode* node=new TreeNode(x);
                if (D==0) root=node;
                else{
                    // find the correct depth
                    while (st.back().second != D-1) 
                        st.pop_back();
                    if (st.back().first->left==NULL)
                        st.back().first->left=node;
                    else
                        st.back().first->right=node;
                }
                st.emplace_back(node, D);
                D=0;
                while(T[i]=='-') D++, i++;
                i--;
            //    cout<<D<<", ";
            }
            return root;
        }
    };