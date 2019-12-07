import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def txt_to_csv(path):
    txt_list = []
    for txt_file in glob.glob(path + '/*.txt'):
        tree = ET.parse(txt_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            txt_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    txt_df = pd.DataFrame(txt_list, columns=column_name)
    return txt_df


def main():
    for folder in ['train','test']:
        image_path = os.path.join(os.getcwd(), ('images/' + folder))
        txt_df = txt_to_csv(image_path)
        txt_df.to_csv(('images/' + folder + '_labels.csv'), index=None)
        print('Successfully converted txt to csv.')


main()
