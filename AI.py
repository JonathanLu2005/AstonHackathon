import google.generativeai as genai

genai.configure(api_key='AIzaSyDl-uTs1Fj8bAMQHuiIUWJzTsWN09efumw')

model = genai.GenerativeModel('gemini-pro')

prompt = """
Generate 10 questions which relate to the below text. The questions should be multiple choice, each of which have 4 options. Give your output as a JSON object with all questions and answers. Do not include new line characters. It should be a valid JSON object.

CS131 Mathematics for Computer Scientists II (Spring Term 2022)
Part III, Sequences and Series Note 18
DECIMAL REPRESENTATION OF REAL NUMBERS
Recall that if |r| < 1 then the geometric series (Note 17) P
n≥0
r
n has sum 1/(1 − r), i.e.,
1 + r + r
2 + r
3 + · · · =
1
1 − r
.
If a1, a2, · · · is a sequence of decimal digits, so that each ai belongs to {0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
then .a1a2a3 · · · denotes the real number
a1
10
+
a2
102
+
a3
103
+ · · · .
To see why this sum exists, note that we have an/10n ≤ 9/10n P
for each n. Now the series
1/10n
converges (r =1/10 above), so P9/10n
converges, and it follows from the Comparison
Test (Note 17) that Pan/10n
converges.
It is clear that a terminating decimal .a1a2 · · · an represents a rational number since
.a1a2 · · · an =
a1
10
+
a2
102
+ · · · +
an
10n
.
The general form of a repeating decimal is
.a1a2 · · · amb1b2 · · · bnb1b2 · · · bn · · · ,
which is denoted by .a1a2 · · · am
˙b1b2 · · · ˙bn .
Repeating decimal as rational number. A repeating decimal represents a rational number
and can be expressed as a quotient of two integers by summing an appropriate geometric series
as the following problem illustrates.
Problem. Express the repeating decimal 0.5910˙ 2 as the quotient of two integers. ˙
Solution. We have
0.5910˙ 2 = 0 ˙
.59102102 · · · =
59
100 +
102
105 +
102
108 +
102
1011 + · · ·
=
59
100 +
102
105

1 + 1
103 +
1
106 + · · · 
=
59
100 +
102
105

1
1−1/103

=
59
100 +
102
100
1
103−1

=
59
100 +
102
100
1
999 =
59×999+102
99900
= 59043/99900.
A non-zero number with a terminating decimal representation can also be written as a nonterminating decimal since we can introduce an infinity of repeating 9’s. For example 0.5 = 0.49˙
and 1 = 0.9˙
.
Problem. Show that 0.49 = 1 ˙ /2 .
Solution. From the definition of a repeating decimal we have
0.49 =˙
4
10 +
9
102 +
9
103 + · · · =
4
10 +
9
102

1
1−1/10
=
4
10 +
9
100−10 =
4
10 +
1
10 =
1
2
.

Irrational numbers such as √
2, π and e are represented by decimal expansions which do not
terminate or repeat.
The decimal expansion of an arbitrary real number, pictured at x on the real line, can be
computed to any desired accuracy in the following way. If x is not an integer then it lies
between two consecutive integers a0 and a0 + 1. Now divide the interval between these two
integers into 10 equal parts. If x is not on one of the subdivision points then it must lie between
two consecutive subdivision points. Hence we have
a0 +
a1
10
< x < a0 +
a1 + 1
10
,
where a1 ∈ {0, 1, . . . , 9}. Dividing this new interval containing x into 10 equal subintervals
(each of length 1/102
) gives an inequality of the form
a0 +
a1
10
+
a2
102
< x < a0 +
a1
10
+
a2 + 1
102
.
Continuing in this way, we obtain two sequences of finite decimals each converging to x, one
increasing from below and the other decreasing from above. By repeating this procedure sufficiently many times, the decimal expansion of x can be obtained to any desired degree of
accuracy.
Rational numbers as repeating decimals. We have seen that terminating and repeating
decimal expansions represent rational numbers. Now we show that, conversely, every rational
number has a terminating or repeating expansion.
The decimal expansion of a rational number r/s ∈ (0, 1) can be computed using the division
algorithm (generations of schoolchildren used to call this process long division).
Dividing 10r by s we have
10r = sq1 + r1 where 0 ≤ r1 < s.
Repeatedly multiplying remainders by 10 and dividing by s produces sequences q1, q2, . . . and
r1, r2, . . . with
10ri = sqi+1 + ri+1 where 0 ≤ ri < s.
Hence
ri
s
=
qi+1
10
+
1
10
ri+1
s
for each i.
Now for any n we have
r
s
=
q1
10
+
1
10
r1
s
=
q1
10
+
1
10 
q2
10
+
1
10
r2
s

=
q1
10
+
q2
102
+
1
102
r2
s
.
.
.
.
.
.
=
q1
10
+
q2
102
+ · · · +
qn
10n
+
1
10n
rn
s
.
2
Also each qi
is one of the digits 0, 1, . . . , 9 since
0 ≤ 10ri < 10s =⇒ 0 ≤ sqi+1 + ri+1 < 10s
=⇒ 0 ≤ sqi+1 < 10s − ri+1
=⇒ 0 ≤ qi+1 < 10 −
ri+1
s < 10
=⇒ 0 ≤ qi+1 < 10.
If at some stage in the division we obtain a remainder rn = 0 then
r
s
=
q1
10
+
q2
102
+ · · · +
qn
10n
= 0.q1q2 · · · qn .
Otherwise, since there are only finitely many values for the remainders (which must lie between
0 and s − 1), the sequence r1, r2, . . . must contain repetitions.
Suppose that rn is the first repeated remainder, so that rn = rm for some m < n. Dividing
10rn by s is the same as dividing 10rm by s, so the quotient and remainder are the same as
before.
Hence the process repeats and we have qn+1 = qm+1, qn+2 = qm+2 · · · , which gives
r/s = 0.q1q2 · · · q˙m · · · q˙n .
Problem. Find the decimal expansion of 5/14.
Solution.
0 · 3 5 7 1 4 2 8 5
1 4 | 5 · 0 0 0 0 0 0 0 0
4 2
8 0
7 0
1 0 0
9 8
2 0
1 4
6 0
5 6
4 0
2 8
1 2 0
1 1 2
8 0
7 0
Hence 5/14 = 0.357142 ˙ 8 since the remainder 8 is repeated. ˙
ABSTRACT
Content terminating decimals, repeating decimal as rational number, rational numbers as repeating decimals
In this Note we consider decimal numbers in terms of an associated geometric series. We also study the
relationship between repeating decimals and rational numbers and vice-versa.
3
History
The regular use of the decimal point appears to have been introduced about 1585, but the occasional use of
decimal fractions can be traced back as far as the 12th century.
Muhammad ibn-Musa Khwarizmi, [c. 780-c. 850] was a Persian mathematician who wrote a book on algebra,
from part of whose title ( al-jabr ) comes the word ‘algebra’, and a book in which he introduced to the West
the Hindu-Arabic decimal number system. The word ‘algorithm’ is a corruption of his name. He compiled
astronomical tables and was responsible for introducing the concept of zero into Arab mathematics.
Simon Stevinus [c. 1548-1620] was a Flemish scientist who, in physics, developed statics and hydrodynamics;
he also introduced decimal notation into Western mathematics.
John Napier [1550-1617], 8th Laird of Merchiston, was a Scottish mathematician who invented logarithms in
1614 and ‘Napier’s bones’, an early mechanical calculating device for multiplication and division.
Napier arranged his logarithmic calculations in convenient tables which evolved into what generations of
schoolchildren came to know as ‘log tables’. These have now been superseded by the use of hand calculators and digital computers.
It was Napier who first used and then popularised the decimal point to separate the whole part from the
fractional part of a number.
4

"""

response = model.generate_content(prompt)

print(response.parts[0].text)