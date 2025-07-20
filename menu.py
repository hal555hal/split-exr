import nuke

from split_layers16 import split_layers
nuke.menu('Nuke').addCommand('Scripts/Split Layers', lambda: split_layers.main())
