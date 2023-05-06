import os, shutil, glob

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from pypinyin import lazy_pinyin
import image.models as models

name_modified = ""
uploaded_image_path = ""


# 递归删除特定文件夹的所有文件或文件夹
def del_files(path):
    del_list = os.listdir(path)
    for file in del_list:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def upload(request):
    if request.method == 'POST':
        del_files('D:\\deepface\\my_dataset_out\\test')
        name = "test_1"
        upload_path = "D:\\deepface\\my_dataset\\test"
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        position = os.path.join(upload_path, name + ".jpg")
        storage = open(position, 'wb+')
        for chunk in request.FILES.get('file'):
            storage.write(chunk)
        storage.close()
        return JsonResponse({'code': 200, 'data': "Upload Successfully."})


def getExistedPhotoNum(request):
    if request.method == 'GET':
        path_dir_index = f'D:/deepface/my_dataset_out/{name_modified}'
        index = len(os.listdir(path_dir_index))
        return JsonResponse({'code': 200, 'face_nums': index})


def register(request):
    if request.method == 'POST':
        name = str(request.FILES.get("file").name).split(".")[0]
        name_chinese_word_list = lazy_pinyin(name)
        for word in name_chinese_word_list:
            global name_modified
            name_modified = name_modified + word
        path_dir = f'D:/deepface/my_dataset/{name_modified}'
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
        path_dir_index = f'D:/deepface/my_dataset_out/{name_modified}'
        if not os.path.exists(path_dir_index):
            os.makedirs(path_dir_index)
        index = len(os.listdir(path_dir_index)) + len(os.listdir(path_dir)) + 1
        position = os.path.join(path_dir, name_modified + "_" + str(index) + ".jpg")
        storage = open(position, 'wb+')
        for chunk in request.FILES.get('file'):
            storage.write(chunk)
        storage.close()
        global uploaded_image_path
        uploaded_image_path = f'D:/deepface/my_dataset_out/{name_modified}/{name_modified}_{str(index)}.png'
        name_modified = ""
        return JsonResponse({'code': 200, 'data': uploaded_image_path})
    else:
        return JsonResponse({'code': 405, 'data': 'Method Not Available'})


def align(request):
    # Start face align.
    if request.method == 'GET':
        os.system('python D:/deepface/align/align_dataset_mtcnn.py')
        del_files('D:/deepface/my_dataset')
        return JsonResponse({'code': 200, "data": 'Successfully aligned face.'})


def train(request):
    if request.method == 'GET':
        mode = request.GET.get('mode')
        os.system(
            f'python D:/deepface/deepface/main.py {mode} {True} "D:/deepface/my_dataset_out/test/test_1.png"')
        with open("D:/deepface/backend/recognition_result.txt") as file:
            result_str = file.read()
            result_tuple = eval(result_str)
            print(result_tuple[0])
        del_files("D:\\deepface\\my_dataset_out\\test")
        return JsonResponse(
            {'code': 200, "data": 'Successfully.', "name": str(result_tuple[0]), "cosine": str(result_tuple[1])})


def recognize(request):
    if request.method == 'GET':
        mode = request.GET.get('mode')
        os.system(
            f'python D:/deepface/deepface/main.py {mode} {False} "D:/deepface/my_dataset_out/test/test_1.png"')
        with open("D:/deepface/backend/recognition_result.txt") as file:
            result_str = file.read()
            result_tuple = eval(result_str)
            print(result_tuple[0])
        del_files("D:\\deepface\\my_dataset_out\\test")
        return JsonResponse(
            {'code': 200, "data": 'Successfully.', "name": str(result_tuple[0]), "cosine": str(result_tuple[1])})
