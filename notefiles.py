from pathlib import Path
from typing import Iterable

import click
from marko import Parser


def _get_files(markdown_note: str) -> Iterable:
    document = Parser().parse(markdown_note)
    for i, node in enumerate(document.children):
        if (
            node.get_type() == 'Heading'
            and node.children[0].children.startswith('./')
            and len(document.children) >= i + 1
            and document.children[i + 1].get_type() == 'FencedCode'
        ):
            filename = node.children[0].children
            content = document.children[i + 1].children[0].children
            yield Path(filename), content


@click.command()
@click.argument('markdown_note')
def main(markdown_note: str):
    for filename, content in _get_files(markdown_note):
        if filename.exists():
            click.echo(f'File {filename} already exists. Ignore')
            continue

        click.echo(f'Creating {filename}')
        filename.parent.mkdir(exist_ok=True, parents=True)
        with filename.open('w') as f:
            f.write(content)


if __name__ == '__main__':
    main()
