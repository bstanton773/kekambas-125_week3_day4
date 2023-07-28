from ascii_magic import AsciiArt

try:
    my_art = AsciiArt.from_url('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/100.png')
except OSError as e:
    print(f'Could not load the image, server said: {e.code} {e.msg}')
my_art.to_terminal(columns=100)