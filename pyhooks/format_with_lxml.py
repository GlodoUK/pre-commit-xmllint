import argparse
from lxml import etree
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='XML filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        with open(filename, 'r+') as xml_file:
            try:
                data = etree.tostring(
                    etree.parse(xml_file), pretty_print=True
                ).decode('utf-8')

                xml_file.seek(0)
                xml_file.truncate()
                xml_file.write(data)
            except etree.XMLSyntaxError:
                print(f'{filename} is not well-formed XML.')
                retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
