# BetterStats
Demo for developing a middle-stage between proportions.py and Proportions.

[SizeBot](https://www.github.com/sizedev/SizeBot) currently uses [*proportions.py*](https://github.com/sizedev/SizeBot/blob/master/sizebot/lib/proportions.py) (and to an unfortunate extent, [*userdb.py*](https://github.com/sizedev/SizeBot/blob/master/sizebot/lib/userdb.py)) to calculate stats for users. The plan is to use a library known as *Proportions* (to be written) in SizeBot4, but until then, a stop gap solution would be nice. Eneter *BetterStats.*

The simple `Player` class in this project is a trimmed down form of SB3½'s User, and SV and WV are replaced by a call to the SizeBot API.
