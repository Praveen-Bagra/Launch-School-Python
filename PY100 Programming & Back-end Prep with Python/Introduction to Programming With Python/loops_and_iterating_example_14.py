cats_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange',
}

names = [ name.upper()
          for name in cats_colors
          if cats_colors[name] == 'orange'
          if name[0] == 'L' ]

print(names)
