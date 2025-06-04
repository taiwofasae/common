import sys
from jinja2 import Environment, FileSystemLoader

DEST_FILE = 'output.html'

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <name1=url1> <name2=url2> ...")
        sys.exit(1)

    title = None
    pairs = []
    for arg in sys.argv[1:]:
        if '=' not in arg:
            print(f"Invalid argument: {arg}. Expected format: name=url")
            sys.exit(1)
        name, url = arg.split('=', 1)
        if name.lower() == 'title' and url:
            title = url
            continue
        pairs.append((name, url))

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('url-table.html')
    output = template.render(items=pairs, title=title)

    with open(DEST_FILE, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"page generated successfully, saved to {DEST_FILE}")

if __name__ == '__main__':
    main()