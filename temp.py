import xml.etree.ElementTree as ET
import subprocess, os, glob
import sys
import xml.dom.minidom
from xml.etree.ElementTree import ElementTree


mp = '/projects/temporary/automates/er/gaurav/rough/p/*'
mt = '/projects/temporary/automates/er/gaurav/rough/t/*'

for m in [mp,mt]:
    for f in glob.glob(m):

        # converting text file to xml formatted file
        basename = os.path.basename(f).split('.')[0]
        tree1 = ElementTree()
        tree1.parse(f)
        typ_m = 'p' if m == mp else typ_m = 't'
        sample_path = open('/projects/temporary/automates/er/gaurav/rough/sample/sample.xml', 'w')
        tree1.write(sample_path)

        # Writing etree for the xml files
        tree = ET.parse(sample_path)
        xml_data = tree.getroot()
        xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')
        input_string=xml.dom.minidom.parseString(xmlstr)
        xmlstr = input_string.toprettyxml()
        xmlstr= os.linesep.join([s for s in xmlstr.splitlines() if s.strip()])

        with open('/projects/temporary/automates/er/gaurav/rough/sample/{typ_m}/{basename}.xml', "wb") as file_out:
            file_out.write(xmlstr.encode(sys.stdout.encoding, errors='replace'))
