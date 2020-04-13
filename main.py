from pprint import pprint
import Plants
import Albums
import LittleAnimals


def main():
    pprint('程序开始运行...')

    pprint('开始采集植物...')
    Plants.GetPlants()

    pprint('开始采集唱片...')
    Albums.GetAlbums()

    pprint('开始采集小动物...')
    pprint('此过程耗时较长，请耐心等待...')
    LittleAnimals.GetLittleAnimals()

    pprint('全部采集完成')

if __name__ == '__main__':
    main()