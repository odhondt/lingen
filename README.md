# LINGEN :drum:
## a minimal random linear drumming score generator

I always struggle to find new drumming practice ideas, so I'll let the computer do it for me. 

### Example:
```python
from lingen import generate_drum_sequence
patterns = ["KRL", "RLL"]
sequence = generate_drum_sequence(patterns, num_measures=4)
print(sequence)
```
output:
> 'KRLK RLRL LKRL KRLR | LLRL LKRL KRLR LLKR | LKRL KRLK RLKR LKRL | RLLR LLRL LRLL KRLR'

_Note:_ there is a `ternary` option to generate sextuplets instead of 16th notes.

### How I use it

- I first learn a pattern using only snare / kick with a metronome
- Once I know it well enough I start
    - Adding accents on some singles
    - Orchestrating it around the snare and toms to play it as a fill
    - Trying to play it as a linear groove (right hand on hats)