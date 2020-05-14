from pprint import pprint
import Plants
import Albums
import LittleAnimals
import FishOrInsect
import Clothes
import time


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

    pprint('开始采集服装...视网络状况此过程耗时可能较长，请耐心等待...')
    Clothes.GetAllClothes()

if __name__ == '__main__':
    action= input("请输入数字：0全部 1植物 2唱片 3小动物 4鱼类 5昆虫 6服装")
    t0 = time.time()
    if action== '0':
        main()
    if action == '1':
        pprint('开始采集植物...')
        Plants.GetPlants()
    if action == '2':
        pprint('开始采集唱片...')
        Albums.GetAlbums()
    if action == '3':
        pprint('开始采集小动物...视网络状况此过程耗时可能较长，请耐心等待...')
        LittleAnimals.GetLittleAnimals()
    if action == '4':
        pprint('开始采集鱼类...视网络状况此过程耗时可能较长，请耐心等待...')
        FishOrInsect.GetFishes()
    if action == '5':
        pprint('开始采集昆虫...视网络状况此过程耗时可能较长，请耐心等待...')
        FishOrInsect.GetInsects()
    if action == '6':
        pprint('开始采集服装...视网络状况此过程耗时可能较长，请耐心等待...')
        Clothes.GetAllClothes()
    pprint(f"采集完成,共用时{round((time.time()-t0),1)}秒")



    