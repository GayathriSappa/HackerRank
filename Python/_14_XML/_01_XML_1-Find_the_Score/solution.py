import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    cnt = 0
    for tag in root.iter():
        for attr in tag.attrib.items():
            cnt += 1
    return cnt

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
