from pprint import pprint
import Plants
import Albums
import LittleAnimals
import FishOrInsect


def main():
    pprint('程序开始运行...')

    pprint('开始采集植物...')
    Plants.GetPlants()

    pprint('开始采集唱片...')
    Albums.GetAlbums()

    pprint('开始采集小动物...视网络状况此过程耗时可能较长，请耐心等待...')
    LittleAnimals.GetLittleAnimals()

    pprint('开始采集鱼类...视网络状况此过程耗时可能较长，请耐心等待...')
    FishOrInsect.GetFishes()

    pprint('开始采集昆虫...视网络状况此过程耗时可能较长，请耐心等待...')
    FishOrInsect.GetInsects()

    pprint('全部采集完成')

if __name__ == '__main__':
    main()