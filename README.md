# Fantasy Name Generator
Using a Markov chain, it learns from all Magic: the Gathering cards in existence to generate fantasy 
names of either characters, creatures, spells, enchantments, artifacts, or lands.

The order of the Markov chain can be specified by the user. Lower orders will create output that is 
more significantly different than the training data, at the cost of it being less intelligible. An order
of around 2-3 is usually best, from my experience.

## Installation
This can be installed in **Python 3.9** with `pip install -e .` in the root of the directory. This will
also install the tool `generate_name`. This is the tool that allows you to get the fantasy names.

The first time the tool is run, it will take ~5-10 minutes to download the dataset via API calls.

### Example Usage

```
>>> generate_name
Smonquin
Summoodsontiontruff
Volf
Ing Wity
Lov'S Re
Dinfoodbald Ge
Fald
Right
Weison-Kageisilderuth
May

>>> generate_name -n 2 -t spell
Jadly
Dowersk

>>> generate_name -n 5 -t spell -mo 4
Leaver
Reason
Shattered Skyruins
Silverflamethrower Symbiosis
Revel In Silent Arms
```

### Example Outputs

#### CREATURES
```
Distrangel
Wolf Of Wishes
Alter Skull
Tovolar's Huntagon
Allisher
Infestvale Abominox
```

#### SPELLS
```
Cons of Arcave
Ember Rush
Brig Cauldercrypt
Brazen Silverlorder
Breakir Might
Nevel In Ned
Memothe Bloodpit
```

#### ENCHANTMENTS
```
Vising Star
Remnant Grasp
The Rismation
Reflect of Truth
Propagach
The Kiki-Jiki-Jiki-Jiki-Jiki-Jiki-Jiki-Jiki-Jiki
Adisman Deaths
```

#### CHARACTERS
```
Orren's Her
Telawnhadmnalki, Sperow
Dorotectim
Alvarmer
Ki, Coladom
Nichadeance
King Ludeshorompost
Val Hop
Stres Alt, Peer
Rupter
The Mastridnic
Avathe Moon
```


## Dataset
The dataset is all Magic: the Gathering cards in existence. It is taken from 
[here](https://magicthegathering.io/) (https://magicthegathering.io/).