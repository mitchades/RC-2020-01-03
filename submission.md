My first thought was to go through every combination of 7 letters that aren't *S*, put each of those letters in the middle, and calculate the score. There are 7 * (25 choose 7) = 3,364,900 possible boards that way. Then, I can go through the word list for each board and figure out what the score of each board is, making sure at some point that there's a pangram. Once I'm done, I just find the one that scores the most. Easy, although going through the word list millions of times might be suboptimal.

I eventually figured out that calculating all the combinations of 7 letters that yield pangrams would save a lot of time. There are 7,986 combinations of letters that yield pangrams. Therefore, there are 7,986 * 7 = 55,902 possible boards. I also figured out that I could calculate the score of each word in advance, along with the set of letters that are required to make it. So, it only took a few minutes to calculate my answer. The code is here:

https://github.com/mitchades/RC-2020-01-03

The best three honeycombs and 6 of the best 7 have the same letters which, repeated once, can spell *granite*, *gratine*, *ingrate*, *tangier*, and *tearing* from ENABLE.

|Rank|Center|Outer|Score|
|-:|:--:|--|-:|
|1|`R` | `eating`| 3898|
|2|`N` | `triage`| 3782|
|3|`E` | `rating`| 3769|
|5|`T` |`regain`| 3421|
|6|`I` | `garnet`| 3406|
|7|`A` | `engirt`| 3372|
|12|`G` | `retain`| 3095|

Fourth place was `E + indart`, with 3672 points.

Trivia about the highest scoring honeycomb, `R + eating`:
* There were only 537 words. :(
* The highest scoring words were *reaggregating* and *reintegrating* for 20 points each.
* Seven-letter words were the source of the plurality of both words and points - the five pangrams mentioned above and 126 others.
* In total, there were 50 pangrams. There were no 14-letter words or higher, so only pangrams scored 14 points or more.
* The 13-letter and 12-letter non-pangrams were *reengineering* and *ingratiating*.

|Points|Count|Product|
|---:|--:|-----|
|20  |2  |40|
|19|4|76|
|18|	8	|144|
|17|	11|	187|
|16|	15|	240|
|15|	5	|75|
|14|	5	|70|
|13|	1	|13|
|12|	1	|12|
|11|	6	|66|
|10|	18|	180|
|9|	32|	288|
|8|	59	|472|
|7|	126	|882|
|6|	117|	702|
|5|	81|	405|
|1|	46|	46|

All of that adds up to 3898.
