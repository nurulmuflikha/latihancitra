import torch
from torchvision import transforms
import utils

model_path = 'fruit_detector_checkpoint.pth'  # ubah sesuai dengan path dari model yang telah dilatih

model = get_model_instance_segmentation(num_classes)
checkpoint = torch.load(model_path, map_location=torch.device('cpu'))
model.load_state_dict(checkpoint['model'])
model.eval()

transform = transforms.Compose([transforms.ToTensor()])

image_path = 'hslcabe.png'  # ubah sesuai dengan path dari gambar yang akan diuji
image = Image.open(image_path).convert('RGB')
input_image = transform(image)

with torch.no_grad():
    prediction = model([input_image.to(device)])

print(f"Jumlah buah: {len(prediction[0]['boxes'])}")
