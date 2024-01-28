import os

from natsort import natsorted
from get_chatgpt_caption import get_chatgpt_caption
from settings import settings

def main():
    for filename in natsorted(os.listdir(settings['images_directory'])):
        image_path = os.path.join(settings['images_directory'], filename)
        base_file_name, _ = os.path.splitext(image_path)
        output_file_name = base_file_name + '.txt'

        if not os.path.exists(output_file_name) \
        and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f'Processing file: {filename}')
            caption = get_chatgpt_caption(image_path)
            if (caption):
                with open(output_file_name, 'w') as file:
                    file.write(caption)


if __name__ == "__main__":
    main()
    print('Done')
