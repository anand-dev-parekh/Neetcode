#include <string>

class Solution {
public:
  bool isPalindrome(std::string s) {

    for (int bottom = 0, top = s.size() - 1; bottom < top; bottom++, top--) {

      // Move right pointer till alphanumeric character
      while (isalnum(s[top]) == false && bottom < top) {
        top--;
      }
      // Move left pointer till alphanumeric character
      while (isalnum(s[bottom]) == false && bottom < top) {
        bottom++;
      }

      if (tolower(s[top]) != tolower(s[bottom])) {
        return false;
      }
    }
    return true;
  }
};
