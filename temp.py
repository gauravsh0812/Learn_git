import xml.etree.ElementTree as ET
import subprocess, os, glob, multiprocessing
import sys
import xml.dom.minidom
from xml.etree.ElementTree import ElementTree
from multiprocessing import Pool, Lock

lock = Lock()

mp = '/projects/temporary/automates/er/gaurav/rough/p/*'
mt = '/projects/temporary/automates/er/gaurav/rough/t/*'

temp = []
for m in [mp,mt]:
    for f in glob.glob(m):
        temp.append([f, m])
with Pool(multiprocessing.cpu_count()-10) as pool:
            result = pool.map(pooling, temp)

def pooling(args_list):
    f, m = args_list
    # converting text file to xml formatted file
    basename = os.path.basename(f).split('.')[0]
    tree1 = ElementTree()
    tree1.parse(f)
    if m==mp:
        typ_m = 'p'
        typ_sm = 'sp'
    else: 
        typ_m = 't'
        typ_sm = 'st'
    sample_path = '/projects/temporary/automates/er/gaurav/rough/sample/{typ_sm}/{basename}.xml'
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
