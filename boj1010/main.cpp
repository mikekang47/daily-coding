#include <iostream>

using namespace std;
int t;
int n, m;
int dp[30][31];

int main() {
    cin >> t;
    while (t--) {
        cin >> n >> m;
        for (int i = 1; i <= m; i++) {
            dp[1][i] = i;
        }

        for (int i = 2; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1];
            }
        }
        cout << dp[n][m] << "\n";
    }
    return 0;
}
