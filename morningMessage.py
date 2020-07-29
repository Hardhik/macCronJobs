#! /usr/bin/python

import osascript, random

# List of nice quotes.

morningMessages = ["The two most powerful warriors are patience and time.",
"Lost time is never found again.",
"Time is the most valuable thing a man can spend.",
"You can't have a better tomorrow if you are thinking about yesterday all the time.",
"All we have to decide is what to do with the time that is given us.",
"Your time is limited, so don't waste it living someone else's life."
]


randomVal = int(random.uniform(0, len(morningMessages) - 1))

osascript.run('display notification "' + morningMessages[randomVal] + '" with title "Good Morning" sound name "Submarine"')


