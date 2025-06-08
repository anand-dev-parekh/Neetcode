# 271. Encode and Decode Strings

#### Medium

https://leetcode.com/problems/encode-and-decode-strings/description/

## Solution

Its clear from the question description that we need to create some sort of delimter to encode different where the string breaks. A simple idea might just be to put a '#' character in between in each string, but this fails if the actual string contains a '#' character.

#### Fail Example

["hi", "helllo", "red#blue"] -> encode -> "hi#hello#red#blue" -> decode -> ["hi", "helllo", "red", "blue"]

#### New idea?

So maybe instead we could put the length of the string as our delimter? But this once again fails if the string also starts with a number. How would we know when the length encoding is done and it isn't the actual string?

#### Combine Ideas

We can do this by combining both of our ideas! We encode the length of each string and then put a '#' character to symbolize when the string is starting. This fixes both of the issues we encountered above because the length gets rid decoding and counting seperating strings that contain '#'. And the combined '#' delimiter prevents us from getting wrong length values when decoding.
