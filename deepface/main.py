import os
import sys
import DeepFace
import pandas as pd

models_name = ["VGG-Face", "Facenet", "Facenet512", "OpenFace",
               "DeepFace", "DeepID", "ArcFace", "SFace"]


def selectModel(modelType, isRenewed, imgPath):
    if modelType == 0:
        # Update model
        if isRenewed:
            deleteModel(modelType)
        # Face Recognition
        result0 = DeepFace.find(img_path=imgPath,
                                db_path='D:\\deepface\\my_dataset_out', model_name=models_name[0],
                                enforce_detection=False)
        print(result0)
        # Deal with the result set
        face_list = result0[0]['identity'].tolist()
        # If empty, it means no one match in the face db
        if len(face_list) == 0:
            return 'Unknown'
        # Choose the most similar face in db
        face = face_list[1]
        cosine = result0[0]['VGG-Face_cosine'].tolist()
        # Split to get the face name
        info_list = face.split("/")
        # Return the name
        info = info_list[1]
        name = info.split("_")[0]
        return name, cosine[1]

    if modelType == 1:
        # Update model
        if isRenewed:
            deleteModel(modelType)
        # Face Recognition
        result1 = DeepFace.find(img_path=imgPath,
                                db_path='D:\\deepface\\my_dataset_out', model_name=models_name[1],
                                enforce_detection=False)
        # Deal with the result set
        print(result1)
        face_list = result1[0]['identity'].tolist()
        cosine = result1[0]['Facenet_cosine'].tolist()
        # If empty, it means no one match in the face db
        if len(face_list) == 0:
            return 'Unknown'
        # Choose the most similar face in db
        face = face_list[1]
        # Split to get the face name
        info_list = face.split("/")
        # Return the name
        info = info_list[1]
        name = info.split("_")[0]
        return name, cosine[1]

    if modelType == 2:
        # Update model
        if isRenewed:
            deleteModel(modelType)
        # Face Recognition
        result2 = DeepFace.find(img_path=imgPath,
                                db_path='D:\\deepface\\my_dataset_out', model_name=models_name[2],
                                enforce_detection=False)
        # Deal with the result set
        print(result2)
        face_list = result2[0]['identity'].tolist()
        cosine = result2[0]['Facenet512_cosine'].tolist()
        # If empty, it means no one match in the face db
        if len(face_list) == 0:
            return 'Unknown'
        # Choose the most similar face in db
        face = face_list[1]
        # Split to get the face name
        info_list = face.split("/")
        # Return the name
        info = info_list[1]
        name = info.split("_")[0]
        return name, cosine[1]

    if modelType == 3:
        # Update model
        if isRenewed:
            deleteModel(modelType)
        # Face Recognition
        result3 = DeepFace.find(img_path=imgPath,
                                db_path='D:\\deepface\\my_dataset_out', model_name=models_name[3],
                                enforce_detection=False)
        # Deal with the result set
        print(result3)
        face_list = result3[0]['identity'].tolist()
        # If empty, it means no one match in the face db
        if len(face_list) == 0:
            return 'Unknown'
        # Choose the most similar face in db
        face = face_list[1]
        cosine = result3[0]['OpenFace_cosine'].tolist()
        # Split to get the face name
        info_list = face.split("/")
        # Return the name
        info = info_list[1]
        name = info.split("_")[0]
        return name, cosine[1]

    if modelType == 4:
        # Update model
        if isRenewed:
            deleteModel(modelType)
        # Face Recognition
        result4 = DeepFace.find(img_path=imgPath,
                                db_path='D:\\deepface\\my_dataset_out', model_name=models_name[4],
                                enforce_detection=False)
        # Deal with the result set
        print(result4)
        face_list = result4[0]['identity'].tolist()
        cosine = result4[0]['DeepFace_cosine'].tolist()
        # If empty, it means no one match in the face db
        if len(face_list) == 0:
            return 'Unknown'
        # Choose the most similar face in db
        face = face_list[1]
        # Split to get the face name
        info_list = face.split("/")
        # Return the name
        info = info_list[1]
        name = info.split("_")[0]
        return name, cosine[1]

    if modelType == 5:
        # Update model
        if isRenewed:
            deleteModel(modelType)
        # Face Recognition
        result5 = DeepFace.find(img_path=imgPath,
                                db_path='D:\\deepface\\my_dataset_out', model_name=models_name[5],
                                enforce_detection=False)
        # Deal with the result set
        print(result5)
        face_list = result5[0]['identity'].tolist()
        cosine = result5[0]['DeepID_cosine'].tolist()
        # If empty, it means no one match in the face db
        if len(face_list) == 0:
            return 'Unknown'
        # Choose the most similar face in db
        face = face_list[1]
        # Split to get the face name
        info_list = face.split("/")
        # Return the name
        info = info_list[1]
        name = info.split("_")[0]
        return name, cosine[1]

    if modelType == 6:
        # Update model
        if isRenewed:
            deleteModel(modelType)
        # Face Recognition
        result6 = DeepFace.find(img_path=imgPath,
                                db_path='D:\\deepface\\my_dataset_out', model_name=models_name[6],
                                enforce_detection=False)
        # Deal with the result set
        print(result6)
        face_list = result6[0]['identity'].tolist()
        cosine = result6[0]['ArcFace_cosine'].tolist()
        # If empty, it means no one match in the face db
        if len(face_list) == 0:
            return 'Unknown'
        # Choose the most similar face in db
        face = face_list[1]
        # Split to get the face name
        info_list = face.split("/")
        # Return the name
        info = info_list[1]
        name = info.split("_")[0]
        return name, cosine[1]

    if modelType == 7:
        # Update model
        if isRenewed:
            deleteModel(modelType)
        # Face Recognition
        result7 = DeepFace.find(img_path=imgPath,
                                db_path='D:\\deepface\\my_dataset_out', model_name=models_name[7],
                                enforce_detection=False)
        # Deal with the result set
        print(result7)
        face_list = result7[0]['identity'].tolist()
        cosine = result7[0]['SFace_cosine'].tolist()
        # If empty, it means no one match in the face db
        if len(face_list) == 0:
            return 'Unknown'
        # Choose the most similar face in db
        face = face_list[1]
        # Split to get the face name
        info_list = face.split("/")
        # Return the name
        info = info_list[1]
        name = info.split("_")[0]
        return name, cosine[1]


def deleteModel(modelType):
    if modelType == 0:
        os.remove('D:\\deepface\\my_dataset_out\\representations_vgg_face.pkl')
    if modelType == 1:
        os.remove('D:\\deepface\\my_dataset_out\\representations_facenet.pkl')
    if modelType == 2:
        os.remove('D:\\deepface\\my_dataset_out\\representations_facenet512.pkl')
    if modelType == 3:
        os.remove('D:\\deepface\\my_dataset_out\\representations_openface.pkl')
    if modelType == 4:
        os.remove('D:\\deepface\\my_dataset_out\\representations_deepface.pkl')
    if modelType == 5:
        os.remove('D:\\deepface\\my_dataset_out\\representations_deepid.pkl')
    if modelType == 6:
        os.remove('D:\\deepface\\my_dataset_out\\representations_arcface.pkl')
    if modelType == 7:
        os.remove('D:\\deepface\\my_dataset_out\\representations_sface.pkl')


if __name__ == '__main__':
    # selectModel(0, False, "D:\deepface\my_dataset_out\liruijie\liruijie_11.png")
    recognition_result = selectModel(int(sys.argv[1]), bool(sys.argv[2]), str(sys.argv[3]))
    fileName = "recognition_result.txt"
    with open(fileName, 'w', encoding='utf-8') as file:
        file.write(str(recognition_result))
    # record: good models:0,1,2,4(depending on training set),6,8
    # models_name = ["VGG-Face", "Facenet", "Facenet512", "OpenFace",
    #                "DeepFace", "DeepID", "ArcFace", "SFace"]
