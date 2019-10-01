# Djenterator

### Overview
Guitar practice tool that produces "guitar tab" notation for complicated rhythm pieces. Rhythm pieces are pseudo-randomly generated and constructed, which creates an unusually un-musical and arhythmical experience. There is no selectable difficulty level, all of it is tough.

##### Guitar Tab Notation
This is general summmary of guitar tab notation.

Each string is represented, and labelled with its tuning note. The note lengths are shown across the top, and the notes themselves are represnted by a number indicating the fret that should be played. An example is shown below:

```
  |1 e + a 2 e + a 3 e + a 4 e + a |
e |--------------------------------|
b |--------------------------------|
G |--------------------------------|
D |--------------------------------|
A |--------------------------------|
E |0---------------3-------0-------|
```
The above represents playing first an open `E` half-note on the lowest string, and then playing the quarter-note at the third fret of the lowest string, which happens to be a G, and finally the low-E quarter-note.

### Basics
This tool produces four (4) meaures of 4/4 notation. It initializes the 16 permutations of "0" and "-" in 4-digit groupings... i.e.:
- 0000
- 000-
- 00--
- 0---
- 0-0-  
- etc

It then uses the random number generator to select a number in the range [1,16], which is used to select one of the 16 permutations. 

Given 16 permutations, and a length of 4 measures, there are `16 * 16 * 16 * 16` combinations. This allows for a good length of unique practice phrases.

### Future plans
I'd like to add some background key selection algorithm which would allow the generator to place notes instead of simple rhythmic markers, and would make the piece a lot easier to "understand". 

Another interesting idea would be to use digits of transcendentals such as *pi*, *phi*, or *e*. The idea would be to take enough digits from some pseudo-random section of the number trail, and then convert that number into Hex, since I need 16 permutations of 16th notes in order for each permutations of 16th note to have an equal chance of getting selected and used.
