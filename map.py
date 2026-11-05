from colorama import Fore, Style

MAPS = {
    "town_map": {
        "name": "Safe Haven Town",
        "grid": [
            ['#', '#', '#', '#', '#', '#', '#'],
            ['#', 'P', 'E', 'N', 'B', 'S', '#'],
            ['#', '.', '#', '#', '#', '.', '#'],
            ['#', 'G', '.', '.', 'D', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#']
        ]
    },
    "field_map": {
        "name": "Wilderness Fields",
        "grid": [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', 'P', '.', 'H', '#', 'M', '.', 'T', '#'],
            ['#', '#', '#', '.', '#', '.', '#', '#', '#'],
            ['#', 'M', '.', '.', 'M', '.', 'B', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#']
        ]
    }
}

def render_map(map_key, row, col):
    m = MAPS[map_key]
    print(f"\n--- MAP: {m['name']} ---")
    grid = [r[:] for r in m["grid"]]
    grid[row][col] = 'P'

    for r in grid:
        row_str = ""
        for cell in r:
            if cell == 'P':
                row_str += Fore.GREEN + "P " + Style.RESET_ALL
            elif cell == 'M':
                row_str += Fore.RED + "M " + Style.RESET_ALL
            elif cell == 'B' and map_key == 'field_map':
                row_str += Fore.MAGENTA + "B " + Style.RESET_ALL
            elif cell in ['E', 'N', 'H', 'G', 'B', 'S', 'D', 'T']:
                row_str += Fore.YELLOW + cell + " " + Style.RESET_ALL
            elif cell == '#':
                row_str += Fore.BLUE + "# " + Style.RESET_ALL
            else:
                row_str += ". "
        print(row_str)