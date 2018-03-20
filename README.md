# shadowthis

- The function `shadow(msg, userid)` hides a `userid` (integer) in the string `msg` using (almost) invisible unicode spaces.
- The function `deshadow(msg)` gets the id back from a previously encoded string with the shadow function.

```python
>>> shadow('"Hello, hope everything is going great overthere!', 9666)
'Hello, ​﻿﻿hope ​﻿​everything ​​﻿is ﻿﻿﻿going ​﻿great overthere!'
>>> deshadow('Hello, ​﻿﻿hope ​﻿​everything ​​﻿is ﻿﻿﻿going ​﻿great overthere!')
9666
```
