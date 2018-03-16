# shadowthis

- The function `shadow(msg, userid)` hides a `userid` (integer) in the string `msg` using (almost) invisible unicode spaces.
- The function `deshadow(msg)` gets the id back from a previously encoded string with the shadow function.

```python
>>> shadow('ciao, come stai?', 9666)
'ciao, ​﻿﻿​﻿​​​﻿﻿ come stai?'
>>> deshadow('ciao, ​﻿﻿​﻿​​​﻿﻿ come stai?')
9666
```
