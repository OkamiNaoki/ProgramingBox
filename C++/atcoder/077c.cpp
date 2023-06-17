#include <bits/stdc++.h>
#define rep(i, to) for (int i = 0; i < (to); i++)
#define rrep(i, to) for (int i = to - 1; i >= 0; i--)
#define repf(i, from, to) for (int i = (from); i < (to); i++)
#define all(v) v.begin(), v.end()
#define unless(cond) if (!(cond))
using namespace std;
using ll = long long;
template <typename T>
using V = vector<T>;
template <typename T, typename U>
using P = pair<T, U>;

int main() {
  int n;

  cin >> n;
vector<int>a(n);
vector<int>b(n);
vector<int>c(n);


  rep(i, n) {
    cin >> a[i];
  }
  rep(i, n) {
    cin >> b[i];
  }
  rep(i, n) {
    cin >> c[i];
  }

  sort(all(a));
  sort(all(c));

  ll ans = 0;
  rep(i, n) {
    auto low_a_it = lower_bound(all(a), b[i]);
    auto low_c_it = upper_bound(all(c), b[i]);

    ll a_num = low_a_it - a.begin();
    ll c_num = c.end() - low_c_it;

    ans += a_num * c_num;
  }

  cout << ans << endl;
}
