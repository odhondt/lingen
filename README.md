# LINGEN :drum:
## a minimal linear drumming score generator

I always struggle to find new drumming practice ideas, so I'll let the computer do it for me. :smile:

### Example:
```python
from lingen import generate_drum_sequence
patterns = ["KRL", "RLL"]
sequence = generate_drum_sequence(patterns, num_measures=4)
print(sequence)
```
output:
> 'KRLK RLRL LKRL KRLR | LLRL LKRL KRLR LLKR | LKRL KRLK RLKR LKRL | RLLR LLRL LRLL KRLR'