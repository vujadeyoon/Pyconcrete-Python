import argparse
import numpy as np
import cv2
import torch
from resnet import resnet18

parser = argparse.ArgumentParser(description='Pyconcrete-PyTorch-Image_Classifier')
parser.add_argument('--path_image_input', type=str, default='./image.png', help='Path for an input image')
parser.add_argument('--path_ckpt', type=str, default='./resnet18-5c106cde.pth', help='Path for a pretrained weights.')
args = parser.parse_args()

if __name__ == "__main__":
    if torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')

    model = resnet18()
    model.load_state_dict(torch.load(args.path_ckpt))
    model.eval()

    ndarr_image = cv2.resize(cv2.imread(filename=args.path_image_input), dsize=(224, 224), interpolation=cv2.INTER_LINEAR).astype(np.float32)
    ndarr_image -= [0.485, 0.456, 0.406]
    ndarr_image /= [0.229, 0.224, 0.225]

    tensor_image = torch.from_numpy(np.expand_dims(ndarr_image, 0)).permute((0, 3, 1, 2))

    if torch.cuda.is_available():
        tensor_image = tensor_image.to(device)
        model.to(device)

    with torch.no_grad():
        output = model(tensor_image)\

    print(torch.nn.functional.softmax(output[0], dim=0).shape)
    print(torch.argmax(torch.nn.functional.softmax(output[0], dim=0)))
